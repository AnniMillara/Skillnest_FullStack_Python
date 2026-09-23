import pymysql.cursors

# CLASE MYSQL CONNECTION
class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    # EJECUTAR CONSULTA
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query_debug = cursor.mogrify(query, data)
                print(
                    "Running Query:",
                    query_debug
                )

                # Ejecutar consulta.
                cursor.execute(
                    query,
                    data
                )

                # INSERT
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid

                # SELECT
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result

                # UPDATE / DELETE
                else:
                    self.connection.commit()

            except Exception as e:
                print(
                    "Ups, algo ha salido mal :(", e)
                return False

            finally:
                # Cerrar conexión.
                self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)