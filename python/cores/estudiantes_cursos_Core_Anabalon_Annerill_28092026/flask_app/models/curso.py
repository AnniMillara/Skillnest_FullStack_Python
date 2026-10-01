from flask_app.config.mysqlconnection import connectToMySQL

class Cursos:
    def __init__(self, data):
        self.id_curso = data["id_curso"]
        self.nombre = data["nombre"]
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
    
    @classmethod
    def todos(cls):
        query = """
            SELECT  
                id_curso,
                nombre,
                created_at,
                updated_at
            FROM cursos
            ORDER BY id_curso
        """
        resultado = connectToMySQL("esquema_estudiantes_cursos").query_db(query)
        cursos = []
        
        for curso in resultado:
            cursos.append(cls(curso))
        
        return cursos
    
    @classmethod
    def buscar_id(cls, id):
        query = """
            SELECT
                id_curso,
                nombre,
                created_at,
                updated_at
            FROM cursos
            WHERE id_curso = %(id_curso)s
        """
        
        data = {
            "id_curso" : id
        }
        
        resultado = connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
        if resultado:
            return cls(resultado[0])
        
        return None

    @classmethod
    def buscar_nombre(cls, nombre):
        query = """
            SELECT
                id_curso,
                nombre,
                created_at,
                updated_at
            FROM cursos
            WHERE nombre = %(nombre)s
        """
        
        data = {
            "nombre" : nombre
        }
        
        resultado = connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
        if resultado:
            return cls(resultado[0])
        
        return None
    
    @classmethod
    def guardar(cls, data):
        query = """
            INSERT INTO cursos(
                nombre,
                created_at,
                updated_at
            )
            VALUES(
                %(nombre)s,
                NOW(),
                NOW()
                )
        """
        
        return connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
    
    @classmethod
    def eliminar(cls, id):
        query = """
            DELETE FROM cursos
            WHERE id_curso = %(id_curso)s
        """
    
        data = {
            "id_curso": id
        }
    
        return connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)