-- ==========================================================
-- ESQUEMA DE BASE DE DATOS
-- ==========================================================
DROP SCHEMA IF EXISTS
    `esquema_usuarios`;
CREATE SCHEMA IF NOT EXISTS
    `esquema_usuarios`
    DEFAULT CHARACTER SET utf8;

USE `esquema_usuarios`;

-- ==========================================================
-- TABLA USUARIOS
-- ==========================================================
CREATE TABLE IF NOT EXISTS `usuarios` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `apellido` VARCHAR(45) NOT NULL,
    `email` VARCHAR(45) NOT NULL UNIQUE,
    `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- ==========================================================
-- DATOS DE PRUEBA
-- ==========================================================
INSERT INTO usuarios (nombre, apellido, email) VALUES
("Pan", "Queso", "panconqueso@gmail.com"),
("Piedra", "Papel", "piedrapapeltijera@gmail.com"),
("Chicle", "Pegado", "chiclepegadoenbanca@gmail.com"),
("Wi-Fi", "Sin Señal", "wifisinsenal@gmail.com"),
("Calcetín", "Perdido", "calcetinperdido@gmail.com");