Algoritmo VentaJuegosPC
	
    Repetir
        Escribir "1- Usuarios"
        Escribir "2- Juegos"
        Escribir "3- Mi Carrito"
        Escribir "4- Salir"
        Leer opcionMenu
		
        Segun opcionMenu Hacer
            1: 
				// En esta opcion realizamos un CRUD en la tabla Usuarios
                Repetir
                    Escribir "1- Registrar usuario"
                    Escribir "2- Modificar usuario"
                    Escribir "3- Eliminar usuario"
                    Escribir "4- Salir"
                    Leer opcionUsuarios
					
                    Segun opcionUsuarios Hacer
                        1:
                            Escribir "Bloque de codigo para registrar usuarios nuevos"
                        2:
                            Escribir "Bloque de codigo para modificar datos de un usuario existente"
                        3:
                            Escribir "Bloque de codigo para eliminar usuarios"
                    FinSegun
                Hasta Que opcionUsuarios = 4
            2:
                // En esta opcion realizamos un CRUD en la tabla Juegos
                Repetir
                    Escribir "1- Agregar juego"
                    Escribir "2- Modificar juego"
                    Escribir "3- Eliminar juego"
                    Escribir "4- Salir"
                    Leer opcionJuegos
					
                    Segun opcionJuegos Hacer
                        1:
                            Escribir "Codigo para agregar un nuevo juego (nombre, compa��a, categor�a)"
                        2:
                            Escribir "Codigo para modificar datos de un juego existente"
                        3:
                            Escribir "Codigo para eliminar un juego"
                    FinSegun
                Hasta Que opcionJuegos = 4
            3:
                // Carrito de compras
                Repetir
                    Escribir "1- Agregar juego al carrito"
                    Escribir "2- Eliminar juego del carrito"
                    Escribir "3- Ver carrito"
                    Escribir "4- Realizar compra"
                    Escribir "5- Salir"
                    Leer opcionCarrito
					
                    Segun opcionCarrito Hacer
                        1:
                            Escribir "Codigo para agregar un juego al carrito del usuario"
                        2:
                            Escribir "Codigo para eliminar un juego del carrito"
                        3:
                            Escribir "Codigo para mostrar los juegos que estan en el carrito"
                        4:
                            Escribir "Codigo para procesar la compra (verificar tipo de cuenta, etc)"
                    FinSegun
                Hasta Que opcionCarrito = 5
        FinSegun
    Hasta Que opcionMenu = 4
FinAlgoritmo