from conexion import Conexion

class Usuarios:
    @staticmethod  # ← Agregué esto
    def revisar(username, contraseña):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        sql = """
            SELECT u.id_usuario, u.username, u.contraseña, t.nombre_tipo
            FROM usuarios u
            JOIN tipo_usuarios t ON u.tipo_usuario_id = t.id_tipo_usuario
            WHERE u.deleted = 0
        """
        
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        
        for u in usuarios:
            if u[1] == username and u[2] == contraseña:
                print('Verificación exitosa')
                
                cursor.close()
                conexion.close()
                return True
        
        print('usuario u Contraseña no válidos')
        cursor.close()
        conexion.close()
        return False
    