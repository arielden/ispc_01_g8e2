# ANÁLISIS ENTRADA-PROCESO-SALIDA (EPS) para el Sistema de Venta de Juegos para PC


## ENTRADA

El sistema recibe los siguientes datos e información:

### CRUD Usuarios:

Registrar usuario: email, contraseña, tipo de cuenta (Standard o Plus).
Modificar usuario: email (para identificar al usuario), nuevos datos (contraseña, tipo de cuenta).
Eliminar usuario: email (para identificar al usuario).

### CRUD Juegos:

Agregar juego: nombre, precio, categoría.
Modificar juego: ID del juego, nuevos datos (nombre, precio, categoría).
Eliminar juego: ID del juego.


### Gestión de Carrito y Compras:

Agregar al carrito: ID del usuario, ID del juego.
Eliminar del carrito: ID del usuario, ID del juego.
Realizar compra: ID del usuario.


## PROCESO

El sistema procesa los datos de entrada de la siguiente manera:

### Usuarios:

Registrar usuario: valida los datos (correo único, contraseña segura), crea un nuevo registro de usuario en la base de datos.
Modificar usuario: busca al usuario por correo electrónico, actualiza los datos en la base de datos.
Eliminar usuario: busca al usuario por correo electrónico, elimina el registro de la base de datos (si no tiene compras asociadas).

### Juegos:

Agregar juego: valida los datos (nombre único), crea un nuevo registro de juego en la base de datos.
Modificar juego: busca el juego por ID, actualiza los datos en la base de datos.
Eliminar juego: busca el juego por ID, elimina el registro de la base de datos (si no está asociado a ninguna compra).
Gestión de Carrito y Compras:

Agregar al carrito: verifica si el juego ya está en el carrito del usuario, si no, agrega un nuevo registro en la tabla "Carrito" con el ID del usuario y el ID del juego.
Eliminar del carrito: busca el registro correspondiente en la tabla "Carrito" y lo elimina.
Realizar compra:
Calcula el total de la compra, aplicando descuentos según el tipo de membresía del usuario.
Crea un nuevo registro en la tabla "Compra" con los detalles de la compra (ID de usuario, fecha, total).
Registra los juegos comprados en una tabla intermedia (o en la misma tabla "Compra" si se simplifica el modelo).
Vacía el carrito del usuario.

## SALIDA

El sistema genera las siguientes salidas:

### Usuarios:

Mensajes de confirmación: "Usuario registrado/modificado/eliminado correctamente".
Mensajes de error: "El correo electrónico ya está registrado", "Contraseña no cumple los requisitos", "No se puede eliminar el usuario porque tiene compras asociadas".

### Juegos:

Mensajes de confirmación: "Juego agregado/modificado/eliminado correctamente".
Mensajes de error: "El nombre del juego ya existe", "No se puede eliminar el juego porque está asociado a compras".

### Gestión de Carrito y Compras:

Mensajes de confirmación: "Juego agregado/eliminado del carrito correctamente", "Compra realizada correctamente".
Visualización del carrito de compra.
Visualización del historial de compras del usuario.