from conexion import Conexion

class Usuarios:
    def __init__(self, username, contraseña):
        self.username = username
        self.contraseña = contraseña
        self.tipo_usuario = "usuario"
        
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
            
            if usuario[2] == "Admin":
                print(f'Bienvenido Administrador {usuario[1]}!!\nQué vas a ver hoy??')
                return True
            else:
                print(f'Bienvenido Usuario {usuario[1]}!!\nQué vas a ver hoy??')
                return False
        else:
            print('usuario u Contraseña no válidos')
    
    @staticmethod
    def ingresar(username, contraseña):
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
            
            if usuario[2] == "Admin":
                print(f'Bienvenido Administrador {usuario[1]}!!\nQué vas a ver hoy??')
                return True
            else:
                print(f'Bienvenido Usuario {usuario[1]}!!\nQué vas a ver hoy??')
                return False
        else:
            print('usuario u Contraseña no válidos')