from usuario import registrar_usuario, modificar_usuario, eliminar_usuario, mostrar_usuario
from juego import agregar_juego, modificar_juego, eliminar_juego, mostrar_juego
from carrito import agregar_al_carrito, eliminar_del_carrito, mostrar_carrito
from compra import realizar_compra, mostrar_compras

while True:
    print("\n----Bienvenido/a! ------")
    print("----Elije una opción----\n")
    print("1. Usuarios")
    print("2. Juegos")
    print("3. Gestión de Carrito y Compras")
    print("4. Salir")
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
                registrar_usuario()
            elif opcion_usuarios == 2:
                modificar_usuario()
            elif opcion_usuarios == 3:
                eliminar_usuario()
            elif opcion_usuarios == 4:
                mostrar_usuario()
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
                agregar_juego()
            elif opcion_juegos == 2:
                modificar_juego()
            elif opcion_juegos == 3:
                eliminar_juego()
            elif opcion_juegos == 4:
                mostrar_juego()
            elif opcion_juegos == 5:
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    elif opcion_menu == 3:
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
                agregar_al_carrito()
            elif opcion_carrito == 2:
                eliminar_del_carrito()
            elif opcion_carrito == 3:
                mostrar_carrito()
            elif opcion_carrito == 4:
                realizar_compra()
            elif opcion_carrito == 5:
                mostrar_compras()
            elif opcion_carrito == 6:
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    elif opcion_menu == 4:
        print("Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")