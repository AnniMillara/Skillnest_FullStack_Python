# MODELO MASCOTA
from mysqlconnection import connectToMySQL

class Mascota:
    """
    Representa un registro de la tabla mascotas.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """
        Consulta todas las mascotas.
        Retorna una lista de objetos Mascota.
        """
        query = "SELECT * FROM mascotas;"
        resultados = connectToMySQL("primera_flask").query_db(query)

        # Si ocurrió un error, resultados será False
        if not resultados:
            return []  # o podrías lanzar una excepción, pero devolvemos lista vacía

        mascotas = []
        for registro in resultados:
            mascotas.append(cls(registro))
        return mascotas

    @classmethod
    def get_by_id(cls, id):
        """
        Busca una mascota por su ID.
        Retorna un objeto Mascota o None si no existe.
        """
        query = "SELECT * FROM mascotas WHERE id = %(id)s;"
        data = {"id": id}
        resultados = connectToMySQL("primera_flask").query_db(query, data)

        if resultados:
            return cls(resultados[0])
        else:
            return None