# Importamos el conector MySQL
import mysql.connector


class Conexion:

    @staticmethod
    def conectar():
        """
        Este método crea y retorna una conexión
        a la base de datos.
        """
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="1234",
            database="colegio"
        )

        return conexion