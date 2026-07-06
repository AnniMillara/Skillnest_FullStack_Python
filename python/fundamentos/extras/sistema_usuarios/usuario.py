from conexion import Conexion

class Usuarios:
    @staticmethod
    def revisar(username, contraseña):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        sql = """
            SELECT u.id_usuario, u.username, u.contraseña, t.nombre_tipo
            FROM usuarios u
            JOIN tipo_usuarios t ON u.tipo_usuario_id = t.id_tipo_usuario
            WHERE u.deleted = 0 AND u.username = %s AND u.contraseña = %s
        """
        
        cursor.execute(sql, (username, contraseña))
        usuario = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        if usuario:
            print('Verificación exitosa')
            return True
        else:
            print('usuario u Contraseña no válidos')
            return False