USE bibliosSad;

-- 1. Insert into usuarios
INSERT INTO usuarios (nombre_usuario, correo_usuario, telefono_usuario, password_hash, created_by)
VALUES
    ('isiadora', 'isi@gmail.com', '947982493', 'hash_isipisi', NULL),
    ('yulieth', 'yulieth@gmail.com', '962788882', 'hash_tulitapafeliz', NULL),
    ('Sergei', 'sergei@gmail.com', '932057428', 'hash_geisito', NULL),
    ('Krishna', 'krishna@gmail.com', '912345678', 'hash_ñemalodon', NULL),
    ('Annerill', 'anne@gmail.com', '995613301', 'hash_panconmantequilla3000', NULL);

-- 2. Insert into nacionalidades
INSERT INTO nacionalidades (nombre_nacionalidad, created_by)
VALUES
    ('Chilena', NULL),
    ('Argentina', NULL),
    ('Peruana', NULL),
    ('Mexicana', NULL),
    ('Española', NULL);

-- 3. Insert into estados_libros
INSERT INTO estados_libros (nombre_estado_libro, descripcion_estado_libro, created_by)
VALUES
    ('Nuevo', 'Libro sin uso, en perfectas condiciones', NULL),
    ('Bueno', 'Leve desgaste por uso normal', NULL),
    ('Regular', 'Algunas marcas o páginas subrayadas', NULL),
    ('Malo', 'Daños visibles, pero legible', NULL),
    ('Restaurado', 'Reparado para su circulación', NULL);

-- 4. Insert into generos_libros
INSERT INTO generos_libros (nombre_genero_libro, descripcion_genero_libro, created_by)
VALUES
    ('Ficción', 'Obras literarias imaginarias', NULL),
    ('No Ficción', 'Basadas en hechos reales', NULL),
    ('Ciencia Ficción', 'Tecnología y futuros especulativos', NULL),
    ('Misterio', 'Suspenso e investigación', NULL),
    ('Biografía', 'Vida de personas reales', NULL);

-- 5. Insert into estados_prestamos
INSERT INTO estados_prestamos (nombre_estado_prestamo, descripcion_estado_prestamo, created_by)
VALUES
    ('Activo', 'Préstamo vigente dentro del plazo', NULL),
    ('Vencido', 'Préstamo con fecha límite pasada', NULL),
    ('Devuelto', 'Libro regresado a la biblioteca', NULL),
    ('Perdido', 'Libro no devuelto y declarado perdido', NULL),
    ('En Reparación', 'Libro dañado en préstamo', NULL);

-- 6. Insert into autores 
INSERT INTO autores (nombre_autor, apellido_autor, fecha_nacimiento, fecha_fallecimiento, nacionalidad_id, created_by)
VALUES
    ('Gabriela', 'Mistral', '1889-04-07 00:00:00', '1957-01-10 00:00:00', 1, NULL),
    ('Jorge Luis', 'Borges', '1899-08-24 00:00:00', '1986-06-14 00:00:00', 2, NULL),
    ('Mario', 'Vargas Llosa', '1936-03-28 00:00:00', '3000-01-01 00:00:00', 3, NULL),  -- sigue vivo
    ('Octavio', 'Paz', '1914-03-31 00:00:00', '1998-04-19 00:00:00', 4, NULL),
    ('Miguel de', 'Cervantes', '1547-09-29 00:00:00', '1616-04-22 00:00:00', 5, NULL);

-- 7. Insert into libros
INSERT INTO libros (titulo, resumen_libro, autor_id, genero_id, estado_libro_id, created_by)
VALUES
    ('Desolación', 'Colección de poemas que reflejan dolor y esperanza', 1, 1, 2, NULL),
    ('Ficciones', 'Cuentos laberínticos sobre realidades paralelas', 2, 3, 1, NULL),
    ('La ciudad y los perros', 'Historia de cadetes en un colegio militar', 3, 1, 3, NULL),
    ('El laberinto de la soledad', 'Ensayo sobre la identidad mexicana', 4, 2, 2, NULL),
    ('Don Quijote de la Mancha', 'Aventuras del ingenioso hidalgo', 5, 1, 4, NULL);

-- 8. Insert into prestamos 
INSERT INTO prestamos (fecha_prestamo, fecha_devolucion, fecha_limite, estado_prestamo_id, usuario_id, libro_id, created_by)
VALUES
    ('2025-01-10 10:00:00', '2025-01-20 14:30:00', '2025-01-24 23:59:59', 3, 1, 1, NULL),
    ('2025-02-05 09:15:00', '2025-02-18 11:00:00', '2025-02-19 23:59:59', 1, 2, 2, NULL),
    ('2025-02-28 13:45:00', '2025-03-15 10:20:00', '2025-03-14 23:59:59', 2, 3, 3, NULL),
    ('2025-03-01 12:00:00', '2025-03-05 16:45:00', '2025-03-15 23:59:59', 3, 4, 4, NULL),
    ('2025-03-10 08:30:00', '2025-03-20 09:00:00', '2025-03-24 23:59:59', 1, 5, 5, NULL);


-- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- LOS SELECT Y CAMBIOS DE COSAS -------------------------------------------------------------------------------------------------------------------------------
-- ------------------------------------------------------------------------------------------------------------------------------------------------------------
SELECT * FROM usuarios;
SELECT * FROM autores;
SELECT * FROM estados_libros;
SELECT * FROM estados_prestamos;
SELECT * FROM generos_libros;
SELECT * FROM libros;
SELECT * FROM nacionalidades;
SELECT * FROM prestamos;

-- SELECTs
SELECT autor_id, genero_id
FROM libros;

SELECT nombre_genero_libro, descripcion_genero_libro
FROM generos_libros
WHERE id_genero_libro IN (1,3);

-- SELECT LOGICO
SELECT nombre_usuario -- > selecciona ______  (que queremos ver??)
FROM usuarios         -- > de ___________ (En que tabla se encuentra?)
WHERE deleted = 0;    -- > donde ___________ (cual es la condicion(que el deleted sea 0)?)

SELECT nombre_autor
FROM autores
WHERE deleted = 0;

SELECT nombre_estado_libro
FROM estados_libros
WHERE deleted = 0;

SELECT nombre_estado_prestamo
FROM estados_prestamos
WHERE deleted = 0;

SELECT nombre_genero_libro
FROM generos_libros
WHERE deleted = 0;

SELECT titulo
FROM libros
WHERE deleted = 0;

SELECT nombre_nacionalidad
FROM nacionalidades
WHERE deleted = 0;

SELECT nombre_prestamo
FROM prestamos
WHERE deleted = 0;

-- BORRADO LOGICO
UPDATE usuarios
SET deleted = 1 -- Se recupera colocando 0 de nuevo ˙ᵕ˙
WHERE id_usuario = 2;