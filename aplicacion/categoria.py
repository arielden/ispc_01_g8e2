import mysql.connector

def agregar_categoria(conexion):
    try:
        cursor = conexion.cursor()

        tipo = input("Ingrese el nombre de la categoría: ")

        # Valida que se ingrese un nombre
        if not tipo:
            raise ValueError("ERROR: El nombre de la categoría es obligatorio.")

        # Se verifica si la categoría ya existe
        cursor.execute("SELECT * FROM Categoria WHERE tipo = %s", (tipo,))
        categoria_existente = cursor.fetchone()
        if categoria_existente:
            raise ValueError("ERROR: La categoría ya existe.")

        # Se inserta la categoría en la base de datos
        insertar_query = "INSERT INTO Categoria (tipo) VALUES (%s)"
        cursor.execute(insertar_query, (tipo,))
        conexion.commit()

        print("Categoría agregada correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al agregar categoría: {err}")
        conexion.rollback()
    except ValueError as ve:
        print(ve)
    finally:
        cursor.close()

def modificar_categoria(conexion):
    try:
        cursor = conexion.cursor()
        mostrar_categoria(conexion)  # mostramos las categorías para facilitar la elección del id

        id_categoria = int(input("Ingrese el ID de la categoría a modificar: "))

        # Se verifica si la categoría existe
        cursor.execute("SELECT * FROM Categoria WHERE idCategoria = %s", (id_categoria,))
        categoria_existente = cursor.fetchone()
        if not categoria_existente:
            raise ValueError("ERROR: La categoría no existe.")

        nuevo_tipo = input("Nuevo nombre de la categoría (dejar en blanco para no modificar): ")

        if not nuevo_tipo:
            print("No se ingresaron cambios.")
            return

        # Se verifica si el nuevo nombre de categoría ya existe, omitiendo la que se acaba de crear
        cursor.execute("SELECT * FROM Categoria WHERE tipo = %s AND idCategoria != %s", (nuevo_tipo, id_categoria))
        categoria_existente = cursor.fetchone()
        if categoria_existente:
            raise ValueError("ERROR: Ya existe una categoría con ese nombre.")

        actualizar_query = "UPDATE Categoria SET tipo = %s WHERE idCategoria = %s"
        cursor.execute(actualizar_query, (nuevo_tipo, id_categoria))
        conexion.commit()

        print("Categoría modificada correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al modificar categoría: {err}")
        conexion.rollback()
    except ValueError as ve:
        print(ve)
    finally:
        cursor.close()

def eliminar_categoria(conexion):
    try:
        cursor = conexion.cursor()
        mostrar_categoria(conexion)  # mostramos las categorías para facilitar la elección del id

        id_categoria = int(input("Ingrese el ID de la categoría a eliminar: "))

        # Se verifica si la categoría existe
        cursor.execute("SELECT * FROM Categoria WHERE idCategoria = %s", (id_categoria,))
        categoria_existente = cursor.fetchone()
        if not categoria_existente:
            raise ValueError("ERROR: La categoría no existe.")

        # Se verifica si la categoría tiene juegos asociados
        cursor.execute("SELECT * FROM Juego WHERE Categoria_idCategoria = %s", (id_categoria,))
        juegos = cursor.fetchall()
        if juegos:
            print("No se puede eliminar la categoría porque tiene juegos asociados.")
            return

        # Eliminar la categoría
        eliminar_query = "DELETE FROM Categoria WHERE idCategoria = %s"
        cursor.execute(eliminar_query, (id_categoria,))
        conexion.commit()

        print("Categoría eliminada correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar categoría: {err}")
        conexion.rollback()
    except ValueError as ve:
        print(ve)
    finally:
        cursor.close()

def mostrar_categoria(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Categoria")
        categorias = cursor.fetchall()

        if not categorias:
            print("No hay categorías registradas.")
            return

        print("Categorías registradas:")
        print("-" * 30)  # Línea de separación, 30 guiones
        print("{:<5} {:<25}".format("ID", "Tipo")) # Trunca y alínea a la izquierda
        print("-" * 30)  # Línea de separación
        for categoria in categorias:
            print("{:<5} {:<25}".format(categoria[0], categoria[1]))

    except mysql.connector.Error as err:
        print(f"Error al mostrar categorías: {err}")
    finally:
        cursor.close()