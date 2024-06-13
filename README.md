# ISPC - Grupo 8 - Evidencia 2 y 3

Módulo Programador - TSCDIA - 2024

<!-- Detallar los datos de los integrantes del grupo: Nombre, Apellido, DNI, Correo Electrónico y link (url) de la cuenta personal de github. -->

## Integrantes:

| Nombre        | DNI           | email                     | Github                       |
| ------------- |:-------------:| -------------------------:|-----------------------------:|
| Ariel DENARO  | 29583416      | arieldenaro@gmail.com     |https://github.com/arielden   |
| Javier GAUNA  | 31041850      | gjavier1905@gmail.com     |https://github.com/gjavier07  |
| Pablo BAJAR   | 33599313      | pabloalejabajar@gmail.com |https://github.com/PabloBajar |

<!-- Descripción de la propuesta de proyecto elegida: -->
## Sistema de Venta de Juegos para PC
### Descripción

Este sistema de venta de juegos para PC está diseñado para facilitar la adquisición de juegos digitales por parte de los usuarios, así como la gestión integral de usuarios, juegos, carritos de compra y compras por parte de los administradores. El sistema ofrece dos modalidades de cuenta para los usuarios:

* Estándar: Sin costo, los usuarios adquieren los juegos a su precio completo.
* Plus: Los usuarios obtienen descuentos en los juegos de 40% en el precio final del juego.

### Funcionalidades Principales

#### Para Usuarios:

* Registro e inicio de sesión seguros.
* Exploración del catálogo de juegos, organizado por categorías.
* Visualización detallada de cada juego (nombre, compañía, peso, categoría).
* Adición de juegos al carrito de compra.
* Realización de compras con aplicación automática de descuentos según la membresía.
* Consulta del historial de compras.

#### Para Administradores:

* Gestión completa de usuarios (altas, bajas, modificaciones).
* Gestión del catálogo de juegos (altas, bajas, modificaciones).
* Arquitectura del Sistema

#### Módulos

* usuario.py: Contiene el código para gestionar los usuarios.
* juego.py: Contiene el código para gestionar los juegos.
* carrito.py: Contiene el código para gestionar el carrito de compras.
* compra.py: Contiene el lógica para concretar la compra.
* main.py: Menú principal de la aplicación, muestra un menú interactivo para acceder a las diferentes funcionalidades. (Creación, Lectura, Modificación y Borrado de registros en las distintas tablas.)

# Explicacion Archivos .py

## main.py

El archivo main.py es el punto de entrada principal de la aplicación de ventas de juegos para PC. Su objetivo principal es proporcionar una interfaz de usuario basada en texto que permita a los usuarios y administradores interactuar con el sistema de gestión de ventas de juegos. Este archivo maneja el flujo de la aplicación, presentando menús y submenús que permiten realizar diversas operaciones según el rol del usuario (ya sea un usuario estándar o un administrador).

### Contenido del archivo main.py

### 1-	Importaciones:
Importa funciones y módulos necesarios para la gestión de la base de datos y las operaciones específicas (usuarios, juegos, carrito, compras y categorías).

### 2-	Conexión a la base de datos:
Establece una conexión con la base de datos.

### 3-	Bucle principal:
Presenta el menú principal y permite al usuario seleccionar diferentes opciones.
Las opciones incluyen la gestión de usuarios, juegos, categorías, y el carrito de compras.

### 4-	Gestión de usuarios:
Permite registrar, modificar, eliminar y mostrar usuarios.

### 5-	Gestión de juegos:
Permite agregar, modificar, eliminar y mostrar juegos.

### 6-	Gestión de categorías:
Permite agregar, modificar, eliminar y mostrar categorías.

### 7-	Gestión de carrito y compras:
Permite agregar juegos al carrito, eliminar juegos del carrito, mostrar el contenido del carrito, realizar compras y mostrar el historial de compras.

### 8-	Salir del sistema:
Cierra la conexión con la base de datos y termina el programa.

## Objetivo del archivo main.py

El objetivo de este archivo es proporcionar una interfaz de usuario simple y funcional que permita:
A los administradores: gestionar usuarios, juegos, y categorías.
A los usuarios: explorar juegos, administrar su carrito de compras y realizar compras.

## Archivo carrito.py

El archivo carrito.py contiene funciones que permiten gestionar el contenido del carrito de compras de los usuarios en una aplicación de ventas de juegos para PC. Estas funciones permiten agregar juegos al carrito, eliminar juegos del carrito y mostrar el contenido del carrito de un usuario específico.

### Funciones en carrito.py
### agregar_al_carrito:
Propósito: Agrega un juego al carrito de un usuario.
Proceso:
Obtiene el ID del usuario y el ID del juego.
Verifica que ambos ID sean válidos.
Comprueba si el usuario y el juego existen en la base de datos.
Verifica si el usuario tiene un carrito y si el juego ya está en el carrito.
Si todo es válido, inserta el juego en el carrito del usuario.

Manejo de errores:

Gestiona errores de conexión y transacciones a la base de datos.
Verifica errores de valor (p.ej., ID no válidos).

### eliminar_del_carrito:

Propósito: Elimina un juego del carrito de un usuario.
Proceso:
Obtiene el ID del usuario y el ID del juego.
Verifica que ambos ID sean válidos.
Comprueba si el usuario tiene un carrito.
Si todo es válido, elimina el juego del carrito del usuario.

Manejo de errores:
Gestiona errores de conexión y transacciones a la base de datos.
Verifica errores de valor (p.ej., ID no válidos).

### mostrar_carrito:

Propósito: Muestra el contenido del carrito de un usuario.
Proceso:
Obtiene el ID del usuario.
Verifica si el usuario tiene juegos en su carrito.
Si hay juegos en el carrito, muestra el ID, nombre y precio de cada juego.
Calcula y muestra el total del precio de los juegos en el carrito.

Manejo de errores:
Gestiona errores de conexión a la base de datos.

## Objetivo del archivo carrito.py

El archivo carrito.py tiene como objetivo proporcionar funcionalidades específicas para la gestión del carrito de compras en la aplicación. Permite a los usuarios:

Agregar juegos al carrito: Los usuarios pueden añadir juegos que desean comprar más tarde.
Eliminar juegos del carrito: Los usuarios pueden eliminar juegos que ya no desean comprar.
Mostrar el contenido del carrito: Los usuarios pueden ver los juegos que han agregado a su carrito, junto con el precio total de los juegos.
Estas funciones interactúan con la base de datos MySQL para realizar las operaciones necesarias, asegurando que la información del carrito esté siempre actualizada y sea precisa.

## Archivo categoria.py

El archivo categoria.py contiene funciones para gestionar las categorías de juegos en una aplicación de ventas. Estas funciones permiten agregar, modificar, eliminar y mostrar las categorías.

### Funciones en categoria.py
### agregar_categoria:

Propósito: Agregar una nueva categoría de juego a la base de datos.
Proceso:
Obtiene el nombre de la categoría del usuario.
Verifica que se haya ingresado un nombre válido.
Comprueba si la categoría ya existe en la base de datos.
Inserta la nueva categoría en la base de datos.

Manejo de errores:
Gestiona errores de conexión y transacciones a la base de datos.
Verifica errores de valor (p.ej., nombre de categoría vacío o existente).

### modificar_categoria:

Propósito: Modificar una categoría existente en la base de datos.
Proceso:
Muestra las categorías existentes.
Obtiene el ID de la categoría a modificar.
Verifica que la categoría exista.
Obtiene el nuevo nombre de la categoría del usuario.
Verifica si el nuevo nombre de la categoría ya existe.
Actualiza el nombre de la categoría en la base de datos.

Manejo de errores:
Gestiona errores de conexión y transacciones a la base de datos.
Verifica errores de valor (p.ej., ID de categoría no existente o nombre de categoría ya existente).

### eliminar_categoria:

Propósito: Eliminar una categoría existente de la base de datos.
Proceso:
Muestra las categorías existentes.
Obtiene el ID de la categoría a eliminar.
Verifica que la categoría exista.
Comprueba si la categoría tiene juegos asociados.
Elimina la categoría si no tiene juegos asociados.

Manejo de errores:
Gestiona errores de conexión y transacciones a la base de datos.
Verifica errores de valor (p.ej., ID de categoría no existente o categoría con juegos asociados).

### mostrar_categoria:

Propósito: Mostrar todas las categorías registradas en la base de datos.
Proceso:
Recupera todas las categorías de la base de datos.
Muestra las categorías en formato de tabla con ID y nombre.

Manejo de errores:
Gestiona errores de conexión a la base de datos.

## Objetivo del archivo categoria.py

El objetivo de este archivo es proporcionar las funcionalidades necesarias para gestionar las categorías de los juegos en la aplicación. Permite:

Agregar nuevas categorías: Facilita la expansión del catálogo de juegos clasificándolos en nuevas categorías.
Modificar categorías existentes: Permite actualizar la información de las categorías según sea necesario.
Eliminar categorías: Permite mantener la base de datos organizada eliminando categorías no deseadas, siempre y cuando no tengan juegos asociados.
Mostrar todas las categorías: Proporciona una visión general de las categorías disponibles para facilitar la gestión y la navegación.
Estas funciones interactúan con la base de datos MySQL para realizar las operaciones necesarias, asegurando que la información de las categorías esté siempre actualizada y sea precisa.

## Archivo compra.py

El archivo compra.py contiene dos funciones principales que manejan la lógica de las compras en una aplicación de ventas de juegos. 

### Funciones en compra.py
### realizar_compra:

Propósito: Procesar la compra de los juegos agregados al carrito de un usuario.
Proceso:
Muestra los usuarios disponibles y solicita al usuario que realiza la compra.
Verifica que el usuario exista.
Obtiene el carrito del usuario.
Verifica que el carrito no esté vacío.
Calcula el precio final de cada juego, aplicando descuentos si el usuario tiene una membresía.
Registra la compra en la base de datos.
Vacía el carrito después de realizar la compra.

Manejo de errores:
Gestiona errores de conexión y transacciones a la base de datos.
Verifica errores de valor (p.ej., usuario no existente, carrito vacío)

### mostrar_compras:

Propósito: Mostrar todas las compras registradas en la base de datos.
Proceso:
Obtiene todas las compras, incluyendo información del usuario y del juego.
Verifica si hay compras registradas.
Formatea y muestra los resultados de manera legible.

Manejo de errores:
Gestiona errores de conexión a la base de datos

## Objetivo:

realizar_compra se encarga de procesar la compra de juegos en el carrito de un usuario, incluyendo la aplicación de descuentos y el registro de la compra en la base de datos.
mostrar_compras proporciona una vista completa de todas las compras realizadas, mostrando detalles sobre el usuario, el juego, la fecha y el total de cada compra.

## Archivo juego.py

El archivo juego.py contiene funciones que manejan la lógica relacionada con la administración de juegos en la base de datos. Las funciones permiten agregar, modificar, eliminar y mostrar juegos, así como validar entradas y relaciones de datos.

### Funciones en juego.py
### agregar_juego:

Propósito: Agregar un nuevo juego a la base de datos.
Proceso:
Solicita al usuario que ingrese el nombre, precio y categoría del juego.
Valida que todos los campos estén completos.
Verifica que el nombre del juego no exista ya en la base de datos.
Verifica que la categoría ingresada exista.
Inserta el nuevo juego en la base de datos.

Manejo de errores:
Maneja errores de conexión y transacciones a la base de datos.
Verifica errores de valor (p.ej., campos vacíos, nombre de juego duplicado)

### modificar_juego:

Propósito: Modificar los detalles de un juego existente.
Proceso:
Muestra todos los juegos para facilitar la selección.
Solicita al usuario que ingrese el ID del juego a modificar.
Verifica que el juego exista.
Permite al usuario actualizar el nombre, precio y categoría del juego, verificando que la categoría exista.
Actualiza el juego en la base de datos.

Manejo de errores:
Maneja errores de conexión y transacciones a la base de datos.
Verifica errores de valor (p.ej., juego inexistente, categoría inexistente).

### eliminar_juego:

Propósito: Eliminar un juego de la base de datos.
Proceso:
Muestra todos los juegos para facilitar la selección.
Solicita al usuario que ingrese el ID del juego a eliminar.
Verifica que el juego exista.
Verifica si el juego tiene compras asociadas.
Elimina el juego de la base de datos.

Manejo de errores:
Maneja errores de conexión y transacciones a la base de datos.
Verifica errores de valor (p.ej., juego inexistente, compras asociadas).

### mostrar_juego:

Propósito: Mostrar todos los juegos registrados en la base de datos.
Proceso:
Obtiene todos los juegos y sus categorías asociadas.
Muestra los juegos en un formato legible.

Manejo de errores:
Maneja errores de conexión a la base de datos.

## Objetivo: 

agregar_juego: Agrega un nuevo juego a la base de datos después de validar los datos ingresados.
modificar_juego: Permite modificar los detalles de un juego existente, validando cada cambio.
eliminar_juego: Elimina un juego de la base de datos después de verificar que no tenga compras asociadas.
mostrar_juego: Muestra todos los juegos registrados junto con sus categorías.
Estas funciones proporcionan una gestión completa de los juegos en la aplicación, asegurando la integridad de los datos y proporcionando mensajes claros de error y confirmación.

## Archivo usuario.py

El archivo usuario.py contiene funciones que permiten gestionar usuarios dentro de una aplicación utilizando una base de datos.

### Funciones en usuario.py
### registrar_usuario:

Propósito: Registrar un nuevo usuario en la base de datos.
Proceso:
Solicita al usuario que ingrese el correo electrónico, contraseña, nombre, apellido y el ID de la membresía del nuevo usuario.
Valida que todos los campos obligatorios estén completos.
Verifica que el correo electrónico no esté registrado previamente.
Verifica que el ID de membresía sea válido.
Inserta el usuario en la tabla Usuario y crea un carrito asociado.

Manejo de errores:
Captura excepciones de MySQL y de valor (por ejemplo, campos obligatorios faltantes, correo electrónico duplicado, membresía no válida).

### modificar_usuario:

Propósito: Modificar los datos de un usuario existente.
Proceso:
Muestra todos los usuarios registrados para que el usuario elija cuál modificar.
Solicita al usuario que ingrese el ID del usuario a modificar.
Verifica que el usuario exista en la base de datos.
Permite al usuario actualizar el correo electrónico, contraseña, nombre, apellido y ID de membresía del usuario.
Actualiza los datos del usuario en la base de datos.

Manejo de errores:
Captura excepciones de MySQL y de valor (p.ej., usuario inexistente, correo electrónico duplicado, membresía no válida).

### eliminar_usuario:

Propósito: Eliminar un usuario de la base de datos.
Proceso:
Muestra todos los usuarios registrados para que el usuario elija cuál eliminar.
Solicita al usuario que ingrese el ID del usuario a eliminar.
Verifica que el usuario exista en la base de datos.
Verifica si el usuario tiene compras asociadas.
Elimina el usuario y su carrito asociado de la base de datos.

Manejo de errores:
Captura excepciones de MySQL y de valor (p.ej., usuario inexistente, compras asociadas).

### mostrar_usuario:

Propósito: Mostrar todos los usuarios registrados en la base de datos.
Proceso:
Ejecuta una consulta SQL para obtener los datos de los usuarios y el tipo de membresía asociada.
Muestra los usuarios en un formato legible.

Manejo de errores:
- Captura excepciones de MySQL.

## Objetivo:

Estas funciones (registrar_usuario, modificar_usuario, eliminar_usuario, mostrar_usuario) permiten realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre la tabla de usuarios (Usuario) en una base de datos MySQL. Son fundamentales para la gestión de usuarios dentro de una aplicación, proporcionando funcionalidades desde el registro inicial hasta la modificación y eliminación posterior.

Cada función incluye validaciones para asegurar la integridad de los datos que se insertan, modifican o eliminan en la base de datos. Esto incluye verificar que los campos obligatorios estén completos, que los correos electrónicos no se repitan, que las membresías sean válidas, entre otros.

Se proporcionan mensajes al usuario sobre el estado de las operaciones realizadas (éxito o error), lo cual mejora la experiencia de usuario y facilita la depuración en caso de problemas.

Estas funciones, en conjunto con las de otros archivos como compra.py y juego.py (que gestionan compras y juegos respectivamente), forman un sistema básico pero completo para administrar una tienda de juegos en línea con usuarios, juegos, categorías y transacciones.

## Archivo conexion_basedatos.py

El archivo conexion_basedatos.py contiene el código necesario para establecer la conexión con una base de datos MySQL llamada ventadejuegos. Su objetivo principal es proporcionar una función que maneje la conexión a la base de datos de manera segura y eficiente.

### Función conectar_base()
Objetivo: Establecer una conexión con la base de datos ventadejuegos.

### Funcionamiento:

Utiliza la biblioteca mysql.connector para conectarse a MySQL.
Se especifican los parámetros de conexión como host (localhost), user (root), password (root) y database (ventadejuegos).
Intenta establecer la conexión y maneja posibles errores utilizando un bloque try-except.
Si la conexión se establece correctamente (conexion.is_connected()), imprime un mensaje de "Conexión exitosa!" y devuelve el objeto de conexión conexion.
Si no se puede establecer la conexión, imprime un mensaje de error específico y devuelve None.

Manejo de errores:

Captura cualquier excepción de tipo mysql.connector.Error que pueda ocurrir durante la conexión.
En caso de error, imprime el mensaje de error específico para ayudar en la depuración.

Este archivo es necesario para interactuar con la base de datos ventadejuegos utilizando Python y MySQL. Proporciona una capa de abstracción para manejar la conexión, lo cual es fundamental para mantener un código limpio, seguro y fácil de mantener. La función conectar_base() encapsula toda la lógica necesaria para la conexión, permitiendo a otros módulos de la aplicación utilizarla sin preocuparse por los detalles de implementación de la conexión MySQL.

## Archivo crud_pythontablas.py

El archivo crud_pythontablas.py tiene como objetivo mostrar el contenido de todas las tablas de la base de datos ventadejuegos.

### Contenido del archivo crud_pythontablas.py
### Imports y conexión a la base de datos:

Importa la función conectar_base() del módulo conexion_basedatos para establecer la conexión con la base de datos ventadejuegos.
Importa funciones de otros módulos (mostrar_carrito, mostrar_categoria, mostrar_compras, mostrar_juego, mostrar_usuario) que están en el directorio aplicacion.

### Conexión a la base de datos:

Llama a la función conectar_base() para establecer la conexión con la base de datos ventadejuegos y asigna el objeto de conexión a la variable conexion.
Llamadas a las funciones de mostrar contenido:
Cada una de estas líneas llama a la función correspondiente para mostrar el contenido de las tablas de la base de datos ventadejuegos.
Estas funciones están definidas en otros módulos (usuario.py, juego.py, categoria.py, compra.py, carrito.py en el directorio aplicacion) y tienen la lógica para ejecutar consultas SQL y mostrar los resultados.

### Objetivo del archivo crud_pythontablas.py

El objetivo principal de este archivo es reunir y mostrar de manera conjunta el contenido de todas las tablas importantes de la base de datos ventadejuegos. Utiliza funciones específicas de otros módulos para obtener y presentar estos datos, lo que permite una visión global del estado actual de la base de datos en relación con usuarios, juegos, categorías, compras y carritos.

