from flask_app.config.mysqlconnection import connectToMySQL

class Usuarios:
    def __init__(self, data):
        self.id_estudiante = data["id_estudiante"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.edad = data["edad"]
        self.curso_id = data["curso_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def todos(cls):
        query = """
            SELECT
                id_estudiante,
                nombre,
                apellido,
                edad,
                curso
            FROM usuarios
            ORDER BY curso
        """
        resultados = connectToMySQL("esquema_estudiantes_cursos").query_db(query)
        estudiantes = []
        
        for estudiante in resultados:
            estudiantes.append(cls(estudiante))
        
        return estudiantes
    
    @classmethod
    def buscar_id(cls, id):
        query = """
            SELECT
                id_estudiante,
                nombre,
                apellido,
                edad,
                curso
            FROM usuarios
            WHERE id_estudiante = %(id)s
        """
        
        data = {
            "id_estudiante" : id
        }
        
        resultado = connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
        if resultado:
            return cls(resultado[0])
        
        return None
    
    @classmethod
    def inscripcion(cls, id_curso):
        query = """
            
        """
        