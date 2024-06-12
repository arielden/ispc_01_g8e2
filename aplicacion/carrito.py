import mysql.connector
from usuario import mostrar_usuario
from juego import mostrar_juego

def agregar_al_carrito(conexion):
    try:
        cursor = conexion.cursor()

        id_usuario = int(input("Ingrese el ID del usuario: "))
        mostrar_usuario()
        id_juego = int(input("Ingrese el ID del juego a agregar: "))
        mostrar_juego()

        # Si no ingresa usuario o juego...
        if not id_usuario or not id_juego:
            raise ValueError("ERROR: El ID de usuario y el ID de juego son obligatorios.")

        # Se verifica si el usuario existe
        cursor.execute("SELECT * FROM Usuario WHERE idUsuario = %s", (id_usuario,)) # <-- esto es una tupla, por eso la ","
        usuario = cursor.fetchone()
        if not usuario:
            raise ValueError("ERROR: El usuario no existe.")

        # Se verifica si el juego existe
        cursor.execute("SELECT * FROM Juego WHERE idJuego = %s", (id_juego,))
        juego = cursor.fetchone()
        if not juego:
            raise ValueError("ERROR: El juego no existe.")

        # Se obtiene el ID del carrito del usuario
        cursor.execute("SELECT idCarrito FROM Carrito WHERE Usuario_idUsuario = %s", (id_usuario,))
        carrito = cursor.fetchone()
        if not carrito:
            raise ValueError("ERROR: El usuario no tiene un carrito.")

        carrito_id = carrito[0]

        # Se verifica si el juego ya está en el carrito
        cursor.execute("SELECT * FROM Carrito_has_Juego WHERE Carrito_idCarrito = %s AND Juego_idJuego = %s",
                       (carrito_id, id_juego))
        juego_en_carrito = cursor.fetchone()
        if juego_en_carrito:
            raise ValueError("ERROR: El juego ya está en el carrito.")

        # Se agrega un juego al carrito
        insertar_query = "INSERT INTO Carrito_has_Juego (Carrito_idCarrito, Juego_idJuego) VALUES (%s, %s)"
        cursor.execute(insertar_query, (carrito_id, id_juego))
        conexion.commit()

        print("Juego agregado al carrito correctamente!")

    except mysql.connector.Error as err:
        print(f"Error al agregar juego al carrito: {err}")
        conexion.rollback()
    except ValueError as errorDeValor:
        print(errorDeValor)
    finally:
        cursor.close()

def eliminar_del_carrito(conexion):
    try:
        cursor = conexion.cursor()
        mostrar_carrito(conexion)  # Muestra el carrito actual del usuario

        id_usuario = int(input("Ingrese el ID del usuario: "))
        id_juego = int(input("Ingrese el ID del juego a eliminar: "))

        # Verifica que se hayan introducido id's válidos
        if not id_usuario or not id_juego:
            raise ValueError("ERROR: El ID de usuario y el ID de juego son obligatorios.")

        # Se obtiene el ID del carrito del usuario pasado como arg.
        cursor.execute("SELECT idCarrito FROM Carrito WHERE Usuario_idUsuario = %s", (id_usuario,))
        carrito = cursor.fetchone()
        if not carrito:
            raise ValueError("ERROR: El usuario no tiene un carrito.")

        carrito_id = carrito[0]

        # Se eliminar el juego del carrito
        eliminar_query = "DELETE FROM Carrito_has_Juego WHERE Carrito_idCarrito = %s AND Juego_idJuego = %s"
        cursor.execute(eliminar_query, (carrito_id, id_juego))
        conexion.commit()

        print("Juego eliminado del carrito correctamente!")

    except mysql.connector.Error as err:
        print(f"Error al eliminar juego del carrito: {err}")
        conexion.rollback()
    except ValueError as ve:
        print(ve)
    finally:
        cursor.close()

def mostrar_carrito(conexion):
    try:
        cursor = conexion.cursor()
        id_usuario = int(input("Ingrese el ID del usuario: "))

        # Se obtienen los juegos del carrito del usuario, nombre y precio
        query = """
            SELECT j.idJuego, j.nombre, j.precio
            FROM Carrito_has_Juego chj
            INNER JOIN Juego j ON chj.Juego_idJuego = j.idJuego
            INNER JOIN Carrito c ON chj.Carrito_idCarrito = c.idCarrito
            WHERE c.Usuario_idUsuario = %s
        """
        cursor.execute(query, (id_usuario,))

        resultados = cursor.fetchall()
        # Si no encuentra nada...
        if not resultados:
            print("El carrito está vacío.")
            return

        # Se muestran los resultados
        print("Contenido del carrito:")
        print("-" * 45)
        print("{:<5} {:<30} {:<10}".format("ID", "Nombre", "Precio"))
        print("-" * 45)
        total = 0
        for fila in resultados:
            print("{:<5} {:<30} {:<10.2f}".format(fila[0], fila[1], fila[2]))
            total += fila[2]
        print("-" * 45)
        print(f"Total: {total:.2f}")

    except mysql.connector.Error as err:
        print(f"Error al mostrar el carrito: {err}")
    finally:
        cursor.close()