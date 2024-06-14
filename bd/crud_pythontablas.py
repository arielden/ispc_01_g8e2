# este módulo muestra el contenido de todas las tablas de la base de datos.
import mysql.connector
from conexion_basedatos import conectar_base

conexion = conectar_base()

def mostrar_tablas(conexion):
    try:
        cursor = conexion.cursor()

        # Usuario
        print("\n--- Tabla Usuario ---")
        cursor.execute("SELECT * FROM Usuario")
        usuarios = cursor.fetchall()
        if usuarios:
            print("{:<5} {:<30} {:<15} {:<15} {:<15}".format("ID", "Email", "Nombre", "Apellido", "Membresia (1: Std, 2:Plus)"))
            for usuario in usuarios:
                print(f"{usuario[0]:<5} {usuario[1]:<30} {usuario[3]:<15} {usuario[4]:<15} {usuario[5]:<15}")
        else:
            print("No hay usuarios registrados.")

        # Juego
        print("\n--- Tabla Juego ---")
        query = "SELECT * FROM Juego"
        cursor.execute(query)
        resultados = cursor.fetchall()
        if not resultados:
            print("No hay juegos registrados.")
            return
        print("{:<5} {:<30} {:<10} {:<10}".format("ID", "Nombre", "Precio", "Categoría ID"))
        for fila in resultados:
            print("{:<5} {:<30} {:<10.2f} {:<10}".format(fila[0], fila[1], fila[2], fila[3]))

        # Categoria
        print("\n--- Tabla Categoria ---")
        cursor.execute("SELECT * FROM Categoria")
        categorias = cursor.fetchall()
        if categorias:
            print("{:<5} {:<25}".format("ID", "Tipo"))
            for categoria in categorias:
                print(f"{categoria[0]:<5} {categoria[1]:<25}")
        else:
            print("No hay categorías registradas.")

    except mysql.connector.Error as err:
        print(f"ERROR: No se pueden mostras las tablas: {err}")
    finally:
        cursor.close()
        conexion.close()

        
mostrar_tablas(conexion)
