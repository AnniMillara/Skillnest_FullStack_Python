from flask_app.config.mysqlconnection import connectToMySQL

class Estudiantes:
    def __init__(self, data):
        self.id_estudiante = data["id_estudiante"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.edad = data["edad"]
        self.curso_id = data["curso_id"]
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
    
    @classmethod
    def todos(cls):
        query = """
            SELECT
                id_estudiante,
                nombre,
                apellido,
                edad,
                curso_id,
                created_at,
                updated_at
            FROM estudiantes
            ORDER BY id_estudiante
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
                curso_id,
                created_at,
                updated_at
            FROM estudiantes
            WHERE id_estudiante = %(id_estudiante)s
        """
        
        data = {
            "id_estudiante" : id
        }
        
        resultado = connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
        if resultado:
            return cls(resultado[0])
        
        return None
    
    @classmethod
    def estudiantes_por_curso(cls, curso_id):
        query = """
            SELECT
                id_estudiante,
                nombre,
                apellido,
                edad,
                curso_id,
                created_at,
                updated_at
            FROM estudiantes
            WHERE curso_id = %(curso_id)s
            ORDER BY apellido, nombre
        """
        
        data = {
            "curso_id" : curso_id
        }
        
        resultados = connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
        
        return [cls(fila) for fila in resultados]
    
    @classmethod
    def guardar(cls, data):
        query = """
            INSERT INTO estudiantes(
                nombre,
                apellido,
                edad,
                curso_id,
                created_at,
                updated_at
            )
            VALUES(
                %(nombre)s,
                %(apellido)s,
                %(edad)s,
                %(curso_id)s,
                NOW(),
                NOW()
                )
        """
        
        return connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
    
    @classmethod
    def editar(cls, data):
        query = """
            UPDATE estudiantes
            SET
                nombre = %(nombre)s,
                apellido = %(apellido)s,
                edad = %(edad)s,
                curso_id = %(curso_id)s,
                updated_at = NOW()
            WHERE id_estudiante = %(id_estudiante)s
        """
        
        return connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
    
    @classmethod
    def eliminar(cls, id):
        query = """
            DELETE FROM estudiantes
            WHERE id_estudiante = %(id_estudiante)s
        """
    
        data = {
            "id_estudiante": id
        }
    
        return connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)

    @classmethod
    def hay_estudiantes_cursos(cls, id_curso):
        query = """
            SELECT
                COUNT(*) AS total
            FROM estudiantes
            WHERE curso_id = %(id_curso)s
        """
        
        data = {
            "id_curso" : id_curso
        }
        
        resultado = connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
        
        if resultado[0]["total"] > 0:
            return True
        
        return False