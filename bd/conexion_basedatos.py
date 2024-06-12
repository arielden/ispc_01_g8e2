# Código de conexión a base de datos.
import mysql.connector

def conectar_base():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ventadejuegos" # Nombre de la base de datos
        )

        if conexion.is_connected():
            print("Conexión exitosa!")
            return conexion
        else:
            print("No se pudo conectar con la base de datos")
            return None

    except mysql.connector.Error as err:
        print(f"Ocurrió el siguiente error: {err}")
        return None