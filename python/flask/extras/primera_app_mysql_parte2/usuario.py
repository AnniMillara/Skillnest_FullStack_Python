# MODELO USUARIO
from mysqlconnection import connectToMySQL

class Usuario:
    """
    Representa un registro de la tabla usuarios.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """
        Consulta todos los usuarios.
        Retorna una lista de objetos Usuario.
        """
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL("primera_flask").query_db(query)

        if not resultados:
            return []

        usuarios = []
        for registro in resultados:
            usuarios.append(cls(registro))
        return usuarios