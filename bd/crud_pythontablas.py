# este módulo muestra el contenido de todas las tablas de la base de datos.
from conexion_basedatos import conectar_base
from ..aplicacion.carrito import mostrar_carrito
from ..aplicacion.categoria import mostrar_categoria
from ..aplicacion.compra import mostrar_compras
from ..aplicacion.juego import mostrar_juego
from ..aplicacion.usuario import mostrar_usuario

conexion = conectar_base()

mostrar_usuario(conexion)
mostrar_juego(conexion)
mostrar_categoria(conexion)
mostrar_compras(conexion)
mostrar_carrito(conexion)