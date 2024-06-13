-- Una sola tabla (mostrando todos los datos)
SELECT * FROM usuario;
-- Una sola tabla (mostrando algunas columnas)
SELECT idUsuario, nombre, apellido FROM usuario;
-- Una sola tabla con where
SELECT * FROM categoria
	WHERE tipo = "accion" OR tipo = "shooter";
-- Una sola tabla con where utilizando between
SELECT * FROM usuario
	WHERE idUsuario BETWEEN 9 AND 12;
-- Una sola tabla con where utilizando limit
SELECT * FROM usuario
	WHERE Membresia_idMembresia = 2 LIMIT 3;
-- Más de 1 tabla con inner join
SELECT usuario.nombre, usuario.apellido, membresia.tipo FROM usuario
	INNER JOIN membresia
    ON usuario.Membresia_idMembresia = membresia.idMembresia;
-- Más de 1 tabla con inner join y con filtros
SELECT usuario.nombre, usuario.apellido, membresia.tipo FROM usuario
	INNER JOIN membresia
    ON usuario.Membresia_idMembresia = membresia.idMembresia
    WHERE membresia.tipo = "plus";


