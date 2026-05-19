USE `sistema_mensajes`;

-- Insertar roles
INSERT INTO `roles_usuarios` (`nombre_rol`, `descripcion_rol`)
VALUES 
    ('Administrador', 'Persona responsable que gestiona, organiza y mantiene el sistema'),
    ('Usuario', 'Persona que interactúa o utiliza el sitio web');

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

INSERT INTO `usuarios` (`nombre_usuario`, `email_usuario`, `password_hash`, `rol_usuario_id`)
VALUES
    (`Paula`, `paulita45@gmail.com`, `P4ulita1inda`, `1`)
    (`Catalina`, `catalina50@gmail.com`, `LunaSol2024`, `2`)
    (`Dany`, `ElMaestro999@gmail.com`, `RosaMariposa`, `2`)
    (`Constanza`, `PerroFeliz@gmail.com`, `MarAzul99`, `2`)
    (`Benjamin`, `benja6547@gmail.com`, `PanConQueso`, `1`)

INSERT INTO `mensajes` (`texto_mensaje`, `estado_mensaje_id`,  `remitente_mensaje_id`, `destinatario_mensaje_id`)
VALUES

INSERT INTO `` (``)
VALUES