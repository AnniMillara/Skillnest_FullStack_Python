USE usuarios_db;

INSERT INTO tipo_usuarios (nombre_tipo, descripcion_tipo, created_by, updated_by)
VALUES 
    ('Normal', 'Participa activamente en el sitio', 'system', 'system'),
    ('Admin', 'Crea, coordina y supervisa actividades en el sitio', 'system', 'system');

INSERT INTO usuarios (username, contraseña, tipo_usuario_id, created_by, updated_by)
VALUES 
    ('UserFree','okeokeoke', 1,'system', 'system'),
    ('PanConQueso','CreamCheese', 1,'system', 'system'),
    ('RatonPerez','AllM0n3y', 1,'system', 'system'),
    ('IfiUser','3ls3bit', 1,'system', 'system'),
    ('Conexion','Adm1n1str4d0r', 2,'system', 'system');