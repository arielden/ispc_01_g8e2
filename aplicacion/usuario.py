import mysql.connector

def registrar_usuario(conexion):
    try:
        cursor = conexion.cursor()
        #cursor.execute("START TRANSACTION")  # Iniciar transacción

        email = input("Ingrese el correo electrónico del usuario: ")
        password = input("Ingrese la contraseña del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        apellido = input("Ingrese el apellido del usuario: ")
        id_membresia = int(input("Ingrese el ID de la membresía: "))

        # Se validan datos obligatorios
        if not email or not password or not nombre or not apellido:
            raise ValueError("ERROR: Todos los campos son obligatorios.")

        # Se verifica si el correo electrónico ya está registrado
        cursor.execute("SELECT * FROM Usuario WHERE email = %s", (email,))
        usuario_existente = cursor.fetchone()
        if usuario_existente:
            raise ValueError("ERROR: El correo electrónico ya está registrado.")

        # Se verifica si el ID de membresía existe
        cursor.execute("SELECT * FROM Membresia WHERE idMembresia = %s", (id_membresia,))
        membresia_existente = cursor.fetchone()
        if not membresia_existente:
            raise ValueError("ERROR: El ID de membresía no es válido.")

        # Se inserta el usuario en la base de datos
        insertar_query_usuario = """
            INSERT INTO Usuario (email, password, nombre, apellido, Membresia_idMembresia) 
            VALUES (%s, %s, %s, %s, %s)
        """
        valores_usuario = (email, password, nombre, apellido, id_membresia)
        cursor.execute(insertar_query_usuario, valores_usuario)

        # Se obtiene el ID del usuario recién insertado
        usuario_id = cursor.lastrowid

        # y se crea un carrito para el nuevo usuario
        insertar_carrito_query = "INSERT INTO Carrito (Usuario_idUsuario) VALUES (%s)"
        valores_carrito = (usuario_id,)  # acá pasamos el usuario_id como parámetro
        cursor.execute(insertar_carrito_query, valores_carrito)

        conexion.commit()

        print("Usuario y carrito creados correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al registrar usuario: {err}")
        conexion.rollback()
    except ValueError as ve:
        print(ve)
    finally:
        cursor.close()

def modificar_usuario(conexion):
    try:
        cursor = conexion.cursor()

        # Se muestran usuarios para que el usuario elija cuál modificar
        mostrar_usuario(conexion)

        id_usuario = int(input("Ingrese el ID del usuario a modificar: "))

        # Verificar si el usuario existe
        cursor.execute("SELECT * FROM Usuario WHERE idUsuario = %s", (id_usuario,))
        usuario_existente = cursor.fetchone()
        if not usuario_existente:
            raise ValueError("ERROR: El usuario no existe.")

        email = input("Nuevo correo electrónico (dejar en blanco para no modificar): ")
        password = input("Nueva contraseña (dejar en blanco para no modificar): ")
        nombre = input("Nuevo nombre (dejar en blanco para no modificar): ")
        apellido = input("Nuevo apellido (dejar en blanco para no modificar): ")
        id_membresia = input("Nuevo ID de membresía (dejar en blanco para no modificar): ")

        actualizar_campos = []
        valores = []

        if email:
            # Se verifica si el nuevo correo electrónico ya está registrado (se omite el del usuario actual)
            cursor.execute("SELECT * FROM Usuario WHERE email = %s AND idUsuario != %s", (email, id_usuario))
            email_existente = cursor.fetchone()
            if email_existente:
                raise ValueError("ERROR: El correo electrónico ya está registrado por otro usuario.")

            actualizar_campos.append("email = %s")
            valores.append(email)
        if password:
            actualizar_campos.append("password = %s")
            valores.append(password)
        if nombre:
            actualizar_campos.append("nombre = %s")
            valores.append(nombre)
        if apellido:
            actualizar_campos.append("apellido = %s")
            valores.append(apellido)
        if id_membresia:
            # Se verifica si el nuevo ID de membresía es válido
            cursor.execute("SELECT * FROM Membresia WHERE idMembresia = %s", (int(id_membresia),))
            membresia_existente = cursor.fetchone()
            if not membresia_existente:
                raise ValueError("ERROR: El ID de membresía no es válido.")

            actualizar_campos.append("Membresia_idMembresia = %s")
            valores.append(int(id_membresia))

        if not actualizar_campos:
            print("No se ingresaron cambios.")
            return

        actualizar_query = f"UPDATE Usuario SET {', '.join(actualizar_campos)} WHERE idUsuario = %s"
        valores.append(id_usuario)
        cursor.execute(actualizar_query, valores)
        conexion.commit()

        print("Usuario modificado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al modificar usuario: {err}")
        conexion.rollback()
    except ValueError as ve:
        print(ve)
    finally:
        cursor.close()


def eliminar_usuario(conexion):
    try:
        cursor = conexion.cursor()
        mostrar_usuario(conexion)  # Se muestran usuarios para que el usuario elija cuál eliminar

        id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))

        # Se verifica si el usuario existe
        cursor.execute("SELECT * FROM Usuario WHERE idUsuario = %s", (id_usuario,))
        usuario_existente = cursor.fetchone()
        if not usuario_existente:
            raise ValueError("ERROR: El usuario no existe.")

        # Se verifica si el usuario tiene compras asociadas
        cursor.execute("SELECT * FROM Compra WHERE Usuario_idUsuario = %s", (id_usuario,))
        compras = cursor.fetchall()
        if compras:
            print("No se puede eliminar el usuario porque tiene compras asociadas.")
            return

        # Se emilina el carrito del usuario (si existe)
        cursor.execute("DELETE FROM Carrito WHERE Usuario_idUsuario = %s", (id_usuario,))

        # Se elinina el usuario
        eliminar_query = "DELETE FROM Usuario WHERE idUsuario = %s"
        cursor.execute(eliminar_query, (id_usuario,))
        conexion.commit()

        print("Usuario eliminado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar usuario: {err}")
        conexion.rollback()
    except ValueError as ve:
        print(ve)
    finally:
        cursor.close()


def mostrar_usuario(conexion):
    try:
        cursor = conexion.cursor()

        # Consulta para obtener los datos de los usuarios y el tipo de membresía
        query = """
            SELECT u.idUsuario, u.email, u.Nombre, u.Apellido, m.tipo AS TipoMembresia
            FROM Usuario u
            INNER JOIN Membresia m ON u.Membresia_idMembresia = m.idMembresia
        """
        cursor.execute(query)

        resultados = cursor.fetchall()
        if not resultados:
            print("No hay usuarios registrados.")
            return

        # Se muestran los resultados
        print("Usuarios registrados:")
        print("-" * 65)  # Línea de separación
        print("{:<5} {:<30} {:<15} {:<15} {:<15}".format("ID", "Email", "Nombre", "Apellido", "Tipo de Membresia"))
        print("-" * 65)  # Línea de separación
        for fila in resultados:
            print("{:<5} {:<30} {:<15} {:<15} {:<15}".format(fila[0], fila[1], fila[2], fila[3], fila[4]))

    except mysql.connector.Error as err:
        print(f"Error al mostrar usuarios: {err}")
    finally:
        cursor.close()