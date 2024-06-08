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

El sistema está desarrollado en Python y utiliza una base de datos para almacenar la información de usuarios, juegos, carritos y compras. La estructura de la base de datos se basa en el siguiente diagrama entidad-relación (ER):

[Imagen del diagrama ER simplificado con 4 tablas]

#### Módulos

* usuario.py: Contiene el código para gestionar los usuarios.
* juego.py: Contiene el código para gestionar los juegos.
* carrito.py: Contiene el código para gestionar el carrito de compras.
* compra.py: Contiene el lógica para concretar la compra.
* main.py: Menú principal de la aplicación, muestra un menú interactivo para acceder a las diferentes funcionalidades. (Creación, Lectura, Modificación y Borrado de registros en las distintas tablas.)

