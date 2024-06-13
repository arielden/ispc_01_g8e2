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

Explicacion Archivos .py
main.py
El archivo main.py es el punto de entrada principal de la aplicación de ventas de juegos para PC. Su objetivo principal es proporcionar una interfaz de usuario basada en texto que permita a los usuarios y administradores interactuar con el sistema de gestión de ventas de juegos. Este archivo maneja el flujo de la aplicación, presentando menús y submenús que permiten realizar diversas operaciones según el rol del usuario (ya sea un usuario estándar o un administrador).
Contenido del archivo main.py

1-	Importaciones:
Importa funciones y módulos necesarios para la gestión de la base de datos y las operaciones específicas (usuarios, juegos, carrito, compras y categorías).

2-	Conexión a la base de datos:
Establece una conexión con la base de datos.

3-	Bucle principal:
Presenta el menú principal y permite al usuario seleccionar diferentes opciones.
Las opciones incluyen la gestión de usuarios, juegos, categorías, y el carrito de compras.

4-	Gestión de usuarios:
Permite registrar, modificar, eliminar y mostrar usuarios.
5-	Gestión de juegos:
Permite agregar, modificar, eliminar y mostrar juegos.

6-	Gestión de categorías:
Permite agregar, modificar, eliminar y mostrar categorías.

7-	Gestión de carrito y compras:
Permite agregar juegos al carrito, eliminar juegos del carrito, mostrar el contenido del carrito, realizar compras y mostrar el historial de compras.

8-	Salir del sistema:
Cierra la conexión con la base de datos y termina el programa.

Objetivo del archivo main.py

El objetivo de este archivo es proporcionar una interfaz de usuario simple y funcional que permita:
A los administradores: gestionar usuarios, juegos, y categorías.
A los usuarios: explorar juegos, administrar su carrito de compras y realizar compras.



