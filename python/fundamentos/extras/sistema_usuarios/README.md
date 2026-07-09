# SISTEMA DE GESTÓN DE USUARIOS

## Descripción

Sistema de consola desarrollado en Python que permite gestionar usuarios con control de acceso por roles. Los administradores pueden realizar operaciones CRUD sobre los usuarios, mientras que los usuarios comunes solo pueden iniciar sesión y cerrar sesion.

## Tecnologias utilizadas

- Python
- Programación Orientada a Objetos
- MySQL
- mysql-connector-python

## Estructura del proyecto

> - main.py - Punto de entrada del programa
> - conexion.py - Clase para manejar la conexion a MySQL
> - usuario.py - Clase Usuarios con toda la logica de negocio
> - crear_bd.sql - Script para crear la base de datos y tablas
> - poblar_datos.sql - Script con datos iniciales
> - ERD.png - Diagrama Entidad-Relacion

## Base de datos

La base de datos se llama usuarios_db y contiene dos tablas:

- tipo_usuarios: almacena los roles disponibles (Admin, Normal)
- usuarios: almacena los datos de los usuarios con campos de auditoria

## Instalacion y ejecucion

### Requisitos previos

- Tener MySQL instalado y en funcionamiento
- Tener Python instalado

### Pasos para ejecutar

1. Clonar el repositorio

2. Instalar la dependencia necesaria

   pip install mysql-connector-python

3. Configurar la base de datos

   - Ejecutar el script crear_bd.sql en MySQL
   - Ejecutar el script poblar_datos.sql para cargar datos iniciales

4. Verificar las credenciales de conexion en conexion.py

   password="root"

5. Ejecutar el programa

   python main.py

## Credenciales de prueba

Administrador:

- Usuario: Conexion
- Contraseña: Adm1n1str4d0r

Usuario normal:

- Usuario: UserFree
- Contraseña: okeokeoke

## Funcionalidades

Menú principal:

- Iniciar sesión
- Salir

Menú de administrador:

- Registrar usuario
- Listar usuarios
- Buscar usuario por ID
- Modificar usuario
- Eliminar usuario
- Cerrar sesión

Menú de usuario común:

- Iniciar sesión
- Cerrar sesion

## Caracteristicas implementadas

- Autenticacion de usuarios
- Control de acceso por roles
- CRUD completo de usuarios
- Validacion de nombre de usuario unico
- Confirmacion antes de eliminar
- Campos de auditoria en la base de datos
- Manejo de errores basico