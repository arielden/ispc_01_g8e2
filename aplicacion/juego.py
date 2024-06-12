import mysql.connector

def agregar_juego(conexion):
    try:
        cursor = conexion.cursor()

        nombre = input("Ingrese el nombre del juego: ")
        precio = float(input("Ingrese el precio del juego: "))
        categoria_id = int(input("Ingrese el ID de la categoría: "))

        # Se valida que se hayan ingresado todos los datos pedidos
        if not nombre or not precio or not categoria_id:
            raise ValueError("ERROR: Todos los campos son obligatorios.")

        # Se verifica si el nombre del juego ya existe
        cursor.execute("SELECT * FROM Juego WHERE nombre = %s", (nombre,))
        juego_existente = cursor.fetchone()
        if juego_existente:
            raise ValueError("ERROR: Ya existe un juego con ese nombre.")

        # Se verifica si la categoría existe
        cursor.execute("SELECT * FROM Categoria WHERE idCategoria = %s", (categoria_id,))
        categoria_existente = cursor.fetchone()
        if not categoria_existente:
            raise ValueError("ERROR: La categoría no existe.")

        # Se inserta el juego en la base de datos
        insertar_query = """
            INSERT INTO Juego (nombre, precio, Categoria_idCategoria)
            VALUES (%s, %s, %s)
        """
        valores = (nombre, precio, categoria_id)
        cursor.execute(insertar_query, valores)
        conexion.commit()

        print("Juego agregado correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al agregar juego: {err}")
        conexion.rollback()
    except ValueError as ve:
        print(ve)
    finally:
        cursor.close()

def modificar_juego(conexion):
    try:
        cursor = conexion.cursor()
        mostrar_juego(conexion)  # Se muestran todos los juegos

        id_juego = int(input("Ingrese el ID del juego a modificar: "))

        # Se verifica si el juego existe
        cursor.execute("SELECT * FROM Juego WHERE idJuego = %s", (id_juego,))
        juego_existente = cursor.fetchone()
        if not juego_existente:
            raise ValueError("ERROR: El juego no existe.")

        nombre = input("Nuevo nombre (dejar en blanco para no modificar): ")
        precio = input("Nuevo precio (dejar en blanco para no modificar): ")
        categoria_id = input("Nuevo ID de categoría (dejar en blanco para no modificar): ")

        actualizar_campos = []
        valores = []

        if nombre:
            actualizar_campos.append("nombre = %s")
            valores.append(nombre)
        if precio:
            actualizar_campos.append("precio = %s")
            valores.append(float(precio))
        if categoria_id:
            # Se verifica si la categoría existe
            cursor.execute("SELECT * FROM Categoria WHERE idCategoria = %s", (int(categoria_id),))
            categoria_existente = cursor.fetchone()
            if not categoria_existente:
                raise ValueError("ERROR: La categoría no existe.")
            actualizar_campos.append("Categoria_idCategoria = %s")
            valores.append(int(categoria_id))

        if not actualizar_campos:
            print("No se ingresaron cambios.")
            return

        actualizar_query = f"UPDATE Juego SET {', '.join(actualizar_campos)} WHERE idJuego = %s"
        valores.append(id_juego)
        cursor.execute(actualizar_query, valores)
        conexion.commit()

        print("Juego modificado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al modificar juego: {err}")
        conexion.rollback()
    except ValueError as errorDeValor:
        print(errorDeValor)
    finally:
        cursor.close()

def eliminar_juego(conexion):
    try:
        cursor = conexion.cursor()
        mostrar_juego(conexion)  # se muestran los juegos para que el usuario elija cuál eliminar

        id_juego = int(input("Ingrese el ID del juego a eliminar: "))

        # Se verifica si el juego existe
        cursor.execute("SELECT * FROM Juego WHERE idJuego = %s", (id_juego,))
        juego_existente = cursor.fetchone()
        if not juego_existente:
            raise ValueError("Error: El juego no existe.")

        # Se verifica si el juego tiene compras asociadas
        cursor.execute("SELECT * FROM Compra WHERE Juego_idJuego = %s", (id_juego,))
        compras = cursor.fetchall()
        if compras:
            print("No se puede eliminar el juego porque tiene compras asociadas.")
            return

        # Se elimina el juego
        eliminar_query = "DELETE FROM Juego WHERE idJuego = %s"
        cursor.execute(eliminar_query, (id_juego,))
        conexion.commit()

        print("Juego eliminado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar juego: {err}")
        conexion.rollback()
    except ValueError as errorDeValor:
        print(errorDeValor)
    finally:
        cursor.close()

def mostrar_juego(conexion):
    try:
        cursor = conexion.cursor()

        # Se obtienen todos los datos de los juegos, también la categoría
        query = """
            SELECT j.idJuego, j.nombre, j.precio, c.tipo AS Categoria
            FROM Juego j
            INNER JOIN Categoria c ON j.Categoria_idCategoria = c.idCategoria
        """
        cursor.execute(query)

        resultados = cursor.fetchall()
        if not resultados:
            print("No hay juegos registrados.")
            return

        # Se muestran los resultados
        print("Juegos registrados:")
        print("-" * 60)  # Línea de separación
        print("{:<5} {:<30} {:<10} {:<15}".format("ID", "Nombre", "Precio", "Categoría"))
        print("-" * 60)  # Línea de separación
        for fila in resultados:
            print("{:<5} {:<30} {:<10} {:<15}".format(fila[0], fila[1], fila[2], fila[3]))

    except mysql.connector.Error as err:
        print(f"Error al mostrar juegos: {err}")
    finally:
        cursor.close()
