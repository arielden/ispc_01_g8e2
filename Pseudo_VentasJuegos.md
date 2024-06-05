Algoritmo Venta_DeJuegos_PC
    // Diccionario para almacenar información de usuarios
    Definir usuarios como Diccionario

    // Función para registrar usuario
    Funcion registrar_usuario(email, contraseña)
        Si email en usuarios Entonces
            Escribir "Email ya está registrado."
        SiNo
            usuarios[email] <- {contraseña: contraseña, tipo_cuenta: "Standard"}
            Escribir "Usuario registrado con éxito."
        FinSi
    FinFuncion

    // Función para seleccionar tipo de cuenta
    Funcion seleccionar_tipo_cuenta(email, tipo_cuenta)
        Si email en usuarios Entonces
            usuarios[email].tipo_cuenta <- tipo_cuenta
            Escribir "Tipo de cuenta actualizado."
        SiNo
            Escribir "Usuario no encontrado."
        FinSi
    FinFuncion

    // Función para iniciar sesión
    Funcion iniciar_sesion(email, contraseña)
        Si email en usuarios y usuarios[email].contraseña = contraseña Entonces
            Escribir "Inicio de sesión exitoso."
        SiNo
            Escribir "Email o contraseña incorrectos."
        FinSi
    FinFuncion

    // Estructura de datos para los juegos (ficticia)
    Definir juegos como Lista de Diccionarios
    juegos.Agregar({nombre: "Juego1", compañía: "Compañía1", peso: 5, precio: 50, categoría: "Acción"})
    juegos.Agregar({nombre: "Juego2", compañía: "Compañía2", peso: 8, precio: 60, categoría: "Aventura"})
    

    // Función para visualizar juegos
    Funcion visualizar_juegos(juegos)
        Para cada juego en juegos Hacer
            Escribir "Nombre:", juego.nombre
            Escribir "Compañía:", juego.compañía
            Escribir "Peso:", juego.peso, "GB"
            Escribir "Categoría:", juego.categoría
            Escribir "Precio:", juego.precio, "USD"
        FinPara
    FinFuncion

    // Función para agregar juegos al carrito
    Funcion agregar_al_carrito(carrito, nombre_juego)
        Para cada juego en juegos Hacer
            Si juego.nombre = nombre_juego Entonces
                carrito.Agregar(juego)
                Escribir "Juego agregado al carrito."
                Retornar
            FinSi
        FinPara
        Escribir "Juego no encontrado."
    FinFuncion

    // Función para realizar compra
    Funcion realizar_compra(carrito, email)
        total <- 0
        Para cada juego en carrito Hacer
            Si usuarios[email].tipo_cuenta = "Plus" Entonces
                total <- total + (juego.precio * 0.40)
            SiNo
                total <- total + juego.precio
            FinSi
        FinPara
        Escribir "Compra realizada. Total a pagar:", total, "USD"
        carrito.Limpiar()
    FinFuncion

    // Programa principal
    Definir menu como Entero
    Definir email como Cadena
    Definir contraseña como Cadena
    Definir tipo_cuenta como Cadena
    Definir nombre_juego como Cadena
    Definir carrito como Lista
    carrito <- []

    Repetir
        Escribir "1- Registrar Usuario"
        Escribir "2- Seleccionar Tipo de Cuenta"
        Escribir "3- Iniciar Sesión"
        Escribir "4- Visualizar Juegos"
        Escribir "5- Agregar Juego al Carrito"
        Escribir "6- Realizar Compra"
        Escribir "7- Salir"
        Leer menu

        Segun menu Hacer
            1:
                Escribir "Ingrese email:"
                Leer email
                Escribir "Ingrese contraseña:"
                Leer contraseña
                registrar_usuario(email, contraseña)
            2:
                Escribir "Ingrese email:"
                Leer email
                Escribir "Ingrese tipo de cuenta (Standard o Plus):"
                Leer tipo_cuenta
                seleccionar_tipo_cuenta(email, tipo_cuenta)
            3:
                Escribir "Ingrese email:"
                Leer email
                Escribir "Ingrese contraseña:"
                Leer contraseña
                iniciar_sesion(email, contraseña)
            4:
                Escribir "Lista de juegos disponibles:"
                visualizar_juegos(juegos)
            5:
                Escribir "Ingrese el nombre del juego a agregar al carrito:"
                Leer nombre_juego
                agregar_al_carrito(carrito, nombre_juego)
            6:
                Escribir "Ingrese su email para realizar la compra:"
                Leer email
                realizar_compra(carrito, email)
            7:
                Escribir "Gracias por Eleccion..."
        FinSegun
    Hasta Que menu == 7
FinAlgoritmo
