import os # --> ejecuta comandos en consola
def limpiar_consola(): # limpian consola del terminal
    os.system('cls')

# clase pais
class pais:
    def __init__(self, nombre_pais):
        self.nombre_pais = nombre_pais

# clase ciudad
class ciudad:
    def __init__(self, nombre_ciudad):
        self.nombre_ciudad = nombre_ciudad

# clase usuario
class usuario:
    def __init__(self, nombre, email, telefono, username, fecha_registro, edad):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.username = username
        self.fecha_registro = fecha_registro
        self.edad = edad
        self.localidad = pais(), ciudad()

# clase equipos
class equipos:
    def __init__(self, nombre_equipo, fecha_creacion, capitan):
        self.nombre_equipo = nombre_equipo
        self.fecha_creacion = fecha_creacion
        self.capitan = usuario

# clase torneos
class torneo:
    def __init__(self, nombre_torneo, juego, premio, fecha_inicio, fecha_fin, organizador):
        self.nombre_torneo = nombre_torneo
        self.juego = juego
        self.premio = premio
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.organizador = organizador
