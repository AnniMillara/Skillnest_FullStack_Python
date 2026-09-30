from flask_app.config.mysqlconnection import connectToMySQL

class Cursos:
    def __init__(self, data):
        self.id_curso = data["id_curso"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def todos(cls):
        query = """
            SELECT  
                id_curso,
                nombre
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
                nombre
            FROM cursos
            WHERE id_curso = %(id)s
        """
        
        data = {
            "id_curso" : id
        }
        
        resultado = connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
        if resultado:
            return cls(resultado[0])
        
        return None