USE `sistema_mensajes`;

-- Insertar roles
INSERT INTO `roles_usuarios` (`nombre_rol`, `descripcion_rol`, `created_by`)
VALUES 
    ('Administrador', 'Persona responsable que gestiona, organiza y mantiene el sistema', null),
    ('Usuario', 'Persona que interactúa o utiliza el sitio web', null),
    ('Invitado', 'Usuario temporal con permisos limitados', null);

-- Estados de comentarios
INSERT INTO `estado_comentarios` (`nombre_estado`, `descripcion_estado`)
VALUES 
    ('Pendiente', 'Comentario esperando aprobación'),
    ('Aprobado', 'Comentario publicado y visible'),
    ('Rechazado', 'Comentario no aprobado');

-- Estados de mensajes
INSERT INTO `estado_mensajes` (`nombre_estado`, `descripcion_estado`)
VALUES 
    ('Enviado', 'Mensaje recién enviado'),
    ('Leído', 'Mensaje leído por el destinatario'),
    ('Archivado', 'Mensaje archivado');

-- Insertar usuarios
INSERT INTO `usuarios` (`nombre_usuario`, `email_usuario`, `password_hash`, `rol_usuario_id`, `created_by`)
VALUES
    ('Paula', 'paulita45@gmail.com', 'P4ulita1inda', 1, null),
    ('Catalina', 'catalina50@gmail.com', 'LunaSol2024', 2, 1),
    ('Dany', 'ElMaestro999@gmail.com', 'RosaMariposa', 2, 1),
    ('Constanza', 'PerroFeliz@gmail.com', 'MarAzul99', 2, 1),
    ('Benjamin', 'benja6547@gmail.com', 'PanConQueso', 1, 1);

-- Insertar mensajes
INSERT INTO `mensajes` (`texto_mensaje`, `estado_mensaje_id`, `remitente_mensaje_id`, `destinatario_mensaje_id`, `created_by`)
VALUES
    ('Hola, ¿cómo estás? Espero que tengas un buen día.', 1, 2, 3, 2),
    ('Estoy muy emocionado con el próximo partido de fútbol, ¿tú vas a verlo?', 2, 3, 4, 3),
    ('¿Quieres ir a cenar este fin de semana? Conozco un lugar excelente.', 1, 3, 5, 3),
    ('Acabo de ver una película increíble, te la recomiendo mucho.', 3, 2, 1, 2),
    ('Estoy pensando en hacer un viaje para las vacaciones, ¿tú tienes algún lugar en mente que me recomiendes?', 3, 4, 3, 4);

-- Insertar comentarios
INSERT INTO `comentarios` (`texto_comentario`, `estado_comentario_id`, `mensaje_id`, `usuario_id`, `created_by`)
VALUES
    ('Me encantó la película, gracias por la recomendación.', 2, 4, 2, 2),
    ('Sí, voy a ver el partido, ¿dónde te parece que nos encontremos?', 2, 2, 4, 4),
    ('Me gustaría ir a cenar, ¿a qué hora te parece bien?', 2, 3, 5, 5),
    ('No he visto la película, pero me la voy a buscar, gracias.', 2, 4, 1, 1),
    ('Me encantaría recomendarte un lugar para tus vacaciones, ¿qué tipo de lugar estás buscando?', 2, 5, 3, 3);

-- -------------
-- VER TABLAS --
-- -------------

USE `sistema_mensajes`;

SELECT * FROM roles_usuarios;
SELECT * FROM estado_comentarios;
SELECT * FROM estado_mensajes;
SELECT * FROM usuarios;
SELECT * FROM mensajes;
SELECT * FROM comentarios;

-- -----------------------
-- CONSULTAS ESPECIALES --
-- -----------------------

-- consultas simples con condición --
-- WHERE en MySQL ﹕
-- Mostrar mensajes donde el remitente sea el elegido ⮟
SELECT texto_mensaje, remitente_mensaje_id
FROM mensajes
WHERE remitente_mensaje_id = 3;

-- Mostrar usuarios que estan activos (del = 0) ⮟ 
SELECT nombre_usuario, email_usuario, rol_usuario_id
FROM usuarios
WHERE deleted = 0;

-- Borra un usuario logicamente ⮟
UPDATE usuarios
SET deleted = 1 -- Se recupera colocando 0 de nuevo ˙ᵕ˙
WHERE id_usuario = 2;

-- --------
-- TAREA --
-- --------
-- Mostrar roles de usuario (nombre, descripción)
SELECT nombre_usuario, descripcion_rol
FROM usuarios, roles_usuarios
WHERE deleted = 0;

-- Elimina dos roles de usuario
UPDATE roles_usuarios
SET deleted = 1
WHERE id_rol_usuario = 2;

UPDATE roles_usuarios
SET deleted = 1 -- Se recupera colocando 0 de nuevo ˙ᵕ˙
WHERE id_rol_usuario = 3;

-- Recupera un rol de usuario
UPDATE roles_usuarios
SET deleted = 0
WHERE id_rol_usuario = 2;

SELECT nombre_rol, descripcion_rol
FROM roles_usuarios
WHERE deleted = 0;