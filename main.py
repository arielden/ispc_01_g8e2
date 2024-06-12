from bd.conexion_basedatos import conectar_base
from aplicacion.usuario import registrar_usuario, modificar_usuario, eliminar_usuario, mostrar_usuario
from aplicacion.juego import agregar_juego, modificar_juego, eliminar_juego, mostrar_juego
from aplicacion.carrito import agregar_al_carrito, eliminar_del_carrito, mostrar_carrito
from aplicacion.compra import realizar_compra, mostrar_compras
from aplicacion.categoria import agregar_categoria, modificar_categoria, eliminar_categoria, mostrar_categoria

conexion = conectar_base()

while True:
    print("\n----Bienvenido/a! ------")
    print("----Elije una opción----\n")
    print("1. Usuarios")
    print("2. Juegos")
    print("3. Categorías") 
    print("4. Gestión de Carrito y Compras")
    print("5. Salir")
    print("-----------------------")
    print("-----Fin del Menu------\n")

    opcion_menu = int(input("Seleccione una opción: "))

    if opcion_menu == 1:
        while True:
            print("\n--- Usuarios ---\n")
            print("1. Registrar usuario")
            print("2. Modificar usuario")
            print("3. Eliminar usuario")
            print("4. Mostrar usuario")
            print("5. Salir")
            print("-----------------------\n")

            opcion_usuarios = int(input("Seleccione una opción: "))

            if opcion_usuarios == 1:
                registrar_usuario(conexion)
            elif opcion_usuarios == 2:
                modificar_usuario(conexion)
            elif opcion_usuarios == 3:
                eliminar_usuario(conexion)
            elif opcion_usuarios == 4:
                mostrar_usuario(conexion)
            elif opcion_usuarios == 5:
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    elif opcion_menu == 2:
        while True:
            print("\n----Juegos----\n")
            print("1. Agregar juego")
            print("2. Modificar juego")
            print("3. Eliminar juego")
            print("4. Mostrar juego")
            print("5. Salir")
            print("-----------------------\n")

            opcion_juegos = int(input("Seleccione una opción: "))

            if opcion_juegos == 1:
                agregar_juego(conexion)
            elif opcion_juegos == 2:
                modificar_juego(conexion)
            elif opcion_juegos == 3:
                eliminar_juego(conexion)
            elif opcion_juegos == 4:
                mostrar_juego(conexion)
            elif opcion_juegos == 5:
                break
            else:
                print("Opción inválida. Intente de nuevo.")
    
    elif opcion_menu == 3:  # Nueva sección para CRUD de categorías
        while True:
            print("\n--- Categorías ---\n")
            print("1. Agregar categoría")
            print("2. Modificar categoría")
            print("3. Eliminar categoría")
            print("4. Mostrar categorías")
            print("5. Salir")
            print("-----------------------\n")

            opcion_categorias = int(input("Seleccione una opción: "))

            if opcion_categorias == 1:
                agregar_categoria(conexion)
            elif opcion_categorias == 2:
                modificar_categoria(conexion)
            elif opcion_categorias == 3:
                eliminar_categoria(conexion)
            elif opcion_categorias == 4:
                mostrar_categoria(conexion)
            elif opcion_categorias == 5:
                break
            else:
                print("Opción inválida. Intente de nuevo.")


    elif opcion_menu == 4:  # Gestión de Carrito y Compras (ahora es la opción 4)
        while True:
            print("\n----Gestión de Carrito y Compras----\n")
            print("1. Agregar juego al carrito")
            print("2. Eliminar juego del carrito")
            print("3. Mostrar carrito")
            print("4. Realizar compra")
            print("5. Mostrar compras")
            print("6. Salir")
            print("-----------------------\n")

            opcion_carrito = int(input("Seleccione una opción: "))

            if opcion_carrito == 1:
                agregar_al_carrito(conexion)
            elif opcion_carrito == 2:
                eliminar_del_carrito(conexion)
            elif opcion_carrito == 3:
                mostrar_carrito(conexion)
            elif opcion_carrito == 4:
                realizar_compra(conexion)
            elif opcion_carrito == 5:
                mostrar_compras(conexion)
            elif opcion_carrito == 6:
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    elif opcion_menu == 5:
        print("Hasta luego!")
        print("Se cierra la conexión con la base de datos!")
        conexion.close()
        break
    else:
        print("Opción inválida. Intente de nuevo.")
