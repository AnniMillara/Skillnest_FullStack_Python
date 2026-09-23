from flask_app.config.mysqlconnection import connectToMySQL

# CLASE USUARIO
class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # CREATE
    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO usuarios
            (
                nombre,
                apellido,
                email
            )
            VALUES
            (
                %(nombre)s,
                %(apellido)s,
                %(email)s
            );
        """
        return connectToMySQL(
            "esquema_usuarios"
        ).query_db(
            query,
            datos
        )

    # READ (todos)
    @classmethod
    def get_all(cls):
        query = """
            SELECT
                id,
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            FROM usuarios
            ORDER BY id;
        """
        usuarios_en_bd = connectToMySQL(
            "esquema_usuarios"
        ).query_db(
            query
        )
        usuarios = []
        for usuario in usuarios_en_bd:
            usuarios.append(cls(usuario))
        return usuarios

    # READ (1)
    @classmethod
    def get_one(cls, datos):
        query = """
            SELECT
                id,
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            FROM usuarios
            WHERE id = %(id)s;
        """
        usuario_en_db = connectToMySQL(
            "esquema_usuarios"
        ).query_db(
            query,
            datos
        )

        if not usuario_en_db:
            return None

        return cls(usuario_en_db[0])

    # UPDATE
    @classmethod
    def update(cls, datos):
        query = """
            UPDATE usuarios
            SET
                nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(
            "esquema_usuarios"
        ).query_db(
            query,
            datos
        )

    # DELETE
    @classmethod
    def delete(cls, datos):
        query = """
            DELETE FROM usuarios
            WHERE id = %(id)s;
        """
        return connectToMySQL(
            "esquema_usuarios"
        ).query_db(
            query,
            datos
        )