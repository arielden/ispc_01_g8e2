import mysql.connector

def realizar_compra(conexion):
    try:
        cursor = conexion.cursor()

        id_usuario = int(input("Ingrese el ID del usuario que realiza la compra: "))

        # Se valida si el usuario existe
        cursor.execute("SELECT * FROM Usuario WHERE idUsuario = %s", (id_usuario,))
        usuario = cursor.fetchone()
        if not usuario:
            raise ValueError("Error: El usuario no existe.")

        # Se obtiene el carrito del usuario
        cursor.execute("SELECT idCarrito FROM Carrito WHERE Usuario_idUsuario = %s", (id_usuario,))
        carrito = cursor.fetchone()
        if not carrito:
            raise ValueError("ERROR: El usuario no tiene un carrito! ")
        carrito_id = carrito[0]

        # Se obtienen los juegos agregados al carrito
        cursor.execute("""
            SELECT Juego_idJuego, precio
            FROM Carrito_has_Juego
            INNER JOIN Juego ON Carrito_has_Juego.Juego_idJuego = Juego.idJuego
            WHERE Carrito_idCarrito = %s
        """, (carrito_id,))
        juegos_carrito = cursor.fetchall()

        if not juegos_carrito:
            raise ValueError("ERROR: El carrito está vacío!")

        total = 0
        for juego_id, precio in juegos_carrito:

            # Se calcula el precio final y se aplica descuento si corresponde
            precio_final = precio
            if usuario[5]:  # Si el usuario tiene asignada una membresía esta columna no sería Null
                cursor.execute("SELECT descuento FROM Membresia WHERE idMembresia = %s", (usuario[5],))
                descuento = cursor.fetchone()[0]
                precio_final *= (1 - descuento / 100)
            total += precio_final

            # y registramos la compra en la base de datos
            insertar_query = """
                INSERT INTO Compra (Usuario_idUsuario, Juego_idJuego, fecha, total)
                VALUES (%s, %s, NOW(), %s)
            """
            valores = (id_usuario, juego_id, precio_final)
            cursor.execute(insertar_query, valores)

        conexion.commit()

        # vaciamos el carrito una vez realizada la compra
        cursor.execute("DELETE FROM Carrito_has_Juego WHERE Carrito_idCarrito = %s", (carrito_id,))
        conexion.commit()

        print(f"La compra se realizó correctamente. Total: {total:.2f}") #acá formateamos para que muestre float de dos dígitos

    except mysql.connector.Error as err:
        print(f"Error al realizar la compra: {err}")
        conexion.rollback()
    except ValueError as errorDeValor:
        print(errorDeValor)
    finally:
        cursor.close()

def mostrar_compras(conexion):
    try:
        cursor = conexion.cursor()

        # Obtenemos todas las compras con información del usuario y del juego
        query = """
            SELECT c.idCompra, u.email, j.nombre, c.fecha, c.total
            FROM Compra c
            INNER JOIN Usuario u ON c.Usuario_idUsuario = u.idUsuario
            INNER JOIN Juego j ON c.Juego_idJuego = j.idJuego
        """
        cursor.execute(query)

        resultados = cursor.fetchall()
        if not resultados:
            print("No hay compras registradas.")
            return

        # Mostramos los resultados
        print("Compras registradas:")
        print("-" * 80)
        print("{:<10} {:<30} {:<30} {:<20} {:<10}".format("ID Compra", "Email Usuario", "Nombre Juego", "Fecha", "Total"))
        print("-" * 80)
        for fila in resultados:
            # Le datos formato a la fecha
            fecha_formateada = fila[3].strftime("%Y-%m-%d %H:%M:%S")  
            print("{:<10} {:<30} {:<30} {:<20} {:<10.2f}".format(fila[0], fila[1], fila[2], fecha_formateada, fila[4]))

    except mysql.connector.Error as err:
        print(f"Error al mostrar compras: {err}")
    finally:
        cursor.close()