# MODELO MASCOTA
from mysqlconnection import connectToMySQL

class Mascota:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM mascotas;"
        resultados = connectToMySQL("primera_flask").query_db(query)
        if not resultados:
            return []
        mascotas = []
        for registro in resultados:
            mascotas.append(cls(registro))
        return mascotas

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM mascotas WHERE id = %(id)s;"
        data = {"id": id}
        resultados = connectToMySQL("primera_flask").query_db(query, data)
        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def get_by_name(cls, nombre):
        query = "SELECT * FROM mascotas WHERE nombre = %(nombre)s;"
        data = {"nombre": nombre}
        resultados = connectToMySQL("primera_flask").query_db(query, data)
        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def get_by_tipo(cls, tipo):
        query = "SELECT * FROM mascotas WHERE tipo = %(tipo)s;"
        data = {"tipo": tipo}
        resultados = connectToMySQL("primera_flask").query_db(query, data)
        if not resultados:
            return []
        mascotas = []
        for registro in resultados:
            mascotas.append(cls(registro))
        return mascotas