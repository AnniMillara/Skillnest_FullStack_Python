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

        # ======================================================
    # READ
    # OBTENER TODAS LAS MASCOTAS
    # ======================================================

    @classmethod
    def get_all(cls):
        """
        Recupera todas las mascotas de la base de datos.
        """
        query = """
            SELECT
                id,
                nombre,
                tipo,
                color,
                created_at,
                updated_at
            FROM mascotas
            ORDER BY id;
        """
        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query)
        
        mascotas = []
        for mascota in resultados:
            mascotas.append(
                cls(mascota)
            )
        return mascotas

    # ======================================================
    # CREATE
    # CREAR NUEVA MASCOTA
    # ======================================================
    @classmethod
    def save(cls, datos):
        """
        Crea una nueva mascota en la base de datos.
        Recibe un diccionario llamado "datos" con:
        nombre
        tipo
        color
        """
        # --------------------------------------------------
        # CONSULTA INSERT
        # --------------------------------------------------
        #
        # Los valores variables no se concatenan
        # directamente dentro del SQL.
        #
        # Utilizamos placeholders.
        # --------------------------------------------------
        query = """
            INSERT INTO mascotas
            (
                nombre,
                tipo,
                color,
                created_at,
                updated_at
            )
            VALUES
            (
                %(nombre)s,
                %(tipo)s,
                %(color)s,
                NOW(),
                NOW()
            );
        """
        
        # --------------------------------------------------
        # EJECUTAR CONSULTA
        # --------------------------------------------------
        return connectToMySQL(
            "primera_flask"
        ).query_db(
            query,
            datos
        )

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
        return None

    # ACTIVIDAD DE CONSOLIDACIÓN: buscar por nombre
    @classmethod
    def get_by_name(cls, nombre):
        """
        Busca una mascota por su nombre exacto.
        Retorna un objeto Mascota o None si no existe.
        """
        query = "SELECT * FROM mascotas WHERE nombre = %(nombre)s;"
        data = {"nombre": nombre}
        resultados = connectToMySQL("primera_flask").query_db(query, data)

        if resultados:
            return cls(resultados[0])
        return None

    # DESAFÍO: buscar por tipo (devuelve lista)
    @classmethod
    def get_by_tipo(cls, tipo):
        """
        Busca todas las mascotas de un tipo determinado.
        Retorna una lista de objetos Mascota.
        """
        query = "SELECT * FROM mascotas WHERE tipo = %(tipo)s;"
        data = {"tipo": tipo}
        resultados = connectToMySQL("primera_flask").query_db(query, data)

        if not resultados:
            return []

        mascotas = []
        for registro in resultados:
            mascotas.append(cls(registro))
        return mascotas