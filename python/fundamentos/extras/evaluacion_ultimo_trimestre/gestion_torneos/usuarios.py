class usuario:
    def __init__(self, nombre_completo, email, username, edad, ciudad, tipoUsuario):
        self.nombre_completo = nombre_completo
        self.email = email
        self.username = username
        self.ciudad = ciudad
        self.edad = edad
        self.tipo_usuario = tipoUsuario
    
    def mostrar_datos(self):  # Método de instancia
        return (f"Nombre: {self.nombre_completo}\n"
                f"Username: {self.username}\n"
                f"Email: {self.email}\n"
                f"Edad: {self.edad}\n")
    
    def cambiar_email(self, nuevo_email):  # Método de instancia
        if "@" in nuevo_email and "." in nuevo_email:
            self.email = nuevo_email
            return f"Email actualizado a: {self.email}"
        return "Email no válido"
    
    @staticmethod
    def validar_edad(edad):  # Método estático
        # Verifica si la edad es apta para participar
        return edad >= 16

user1 = usuario("Lautaro Martínez", "lautaro@email.com", "lautarito13", 22, "Jugador")
user2 = usuario("Camila Rojas", "camila@email.com", "camirojas", 19, "Comentarista")
user3 = usuario("Mateo Fernández", "mateo@email.com", "mateo_nfc", 24, "Admin")
