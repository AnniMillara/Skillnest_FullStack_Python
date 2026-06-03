class tipoUsuario:
    # Define los roles que pueden tener los usuarios en el sistema
    tipos_disponibles = []  # Atributo de clase
    
    def __init__(self, nombre_tipo, descripcion_tipo):
        self.nombre_tipo = nombre_tipo
        self.descripcion_tipo = descripcion_tipo
        tipoUsuario.tipos_disponibles.append(self)
    
    def mostrar_info(self):  # Método de instancia
        return f"Rol: {self.nombre_tipo}\nDescripción: {self.descripcion_tipo}"
    
    @classmethod
    def buscar_tipo_por_nombre(cls, nombre):  # Método de clase
        # Busca un tipo de usuario por su nombre
        for tipo in cls.tipos_disponibles:
            if tipo.nombre_tipo.lower() == nombre.lower():
                return tipo
        return None
    
    @staticmethod
    def validar_nombre_tipo(nombre):  # Método estático
        # Valida si el nombre del tipo es correcto
        nombres_validos = ["jugador", "admin", "jugador lider", "equipo tecnico", "comentarista"]
        return nombre.lower() in nombres_validos

tipo1 = tipoUsuario("Jugador", "Participa activamente en torneos")
tipo2 = tipoUsuario("Admin", "Organiza y supervisa torneos")

