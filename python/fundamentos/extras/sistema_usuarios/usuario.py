from conexion import Conexion

class Usuarios:
    def __init__(self, username, contraseña, tipo_usuario = 1):
        self.username = username
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario
        self.created_by = "system"
        self.updated_by = "system"
        
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
            
            if usuario[3] == "Admin":
                print(f'Bienvenido Administrador {usuario[1]}!!\nQué vas a ver hoy??')
                return True
            else:
                print(f'Bienvenido Usuario {usuario[1]}!!\nQué vas a ver hoy??')
                return False
        else:
            print('usuario u Contraseña no válidos')
    
    def listar():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        sql = """
        SELECT u.id_usuario, u.username, u.tipo_usuario_id
        FROM usuarios u
        JOIN tipo_usuarios t ON u.tipo_usuario_id = t.id_tipo_usuario
        WHERE u.deleted = 0
        """
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        
        print("\n===== USUARIOS =====")
        for u in usuarios:
            print(f"ID: {u[0]} | Nombre: {u[1]} | Tipo: {u[2]}")
            
        cursor.close()
        conexion.close()
        
    def guardar(self):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        # Estructura de control: validacion existencia tipo de usuario
        sql = """
        SELECT t.id_tipo_usuario
        FROM tipo_usuarios t
        WHERE id_tipo_usuario = %s AND deleted = 0
        """
        cursor.execute(sql, (self.tipo_usuario,))
        if not cursor.fetchone():
            print("\nEl tipo de usuario no existe, primero debes de crearlo...")
            cursor.close()
            conexion.close()
            return
        
        # Estructura de control: validacion nombre unico
        sql = """
        SELECT id_usuario
        FROM usuarios
        WHERE username = %s AND deleted = 0
        """
        cursor.execute(sql, (self.username,))
        if cursor.fetchone():
            print("\nEl nombre de usuario ya esta registrado.")
            cursor.close()
            conexion.close()
            return
        
        # ahora lo weno
        sql = """
        INSERT INTO usuarios (nombre_tipo, descripcion_tipo, created_by, updated_by)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (self.username, self.contraseña, self.tipo_usuario, self.created_by, self.updated_by))
        conexion.commit()
        print("\nUsuario agregado correctamente.")
        
        cursor.close()
        conexion.close()
    
    @staticmethod
    def ingresar():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        nombreU = input("Ingresar nombre de usuario:_").strip()
        contraU = input("Ingresar nombre de usuario:_").strip()
        
        sql = """
        SELECT t.id_tipo_usuario t.nombre_tipo, t.descripcion_tipo
        FROM t tipo_usuarios
        WHERE deleted = 0
        """
        
        cursor.execute(sql)
        
        tipoU = int(input("Ingresar tipo de usuario:_")).strip()
        
        if nombreU != "" and contraU != "" and tipoU != "":
            usuario_obj = Usuarios(nombreU, contraU, tipoU)
            usuario_obj.guardar()
        
        cursor.close()
        conexion.close()