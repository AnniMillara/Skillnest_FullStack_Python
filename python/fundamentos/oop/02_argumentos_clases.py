# ⍝ʕ´•ᴥ•`ʔ⍝
class Usuario: # Se crea la「clase」usuario
    # constructor ➠ contiene instrucciones para crear una  nueva instancia de la clase
    # Argumentos ➠ Ingresos
    def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
        # self. ➠ datos
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar

# Creación de las instancias de una clase
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 300000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 100000, 300000)
ann = Usuario("Annerill", "Anabalon", "aneril.anabalon@gmail.com", 20000, 300)

#Accedemos a los atributos de la instancia
# print(instancia) ✘
# ✔ ⤵︎
print("Elementos de Nariyoshi")
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)
print("\nElementos de Daniel")
print(daniel.nombre) #Imprime: Daniel
print(daniel.limite_credito)
print(daniel.saldo_pagar)
print("\nElementos mios")
print(ann.nombre) #Imprime: Nariyoshi
print(ann.apellido)
print(ann.email)
print(ann.limite_credito)
print(ann.saldo_pagar)

# Tarea rapida ❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯
"""
Crear una clase estudiante, asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nacimiento)

Crear tres instacias con tres personas
Imprimir nombre y apellido concatenado + especialidad
"""
print("\n")
class estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

est_uno = estudiante("22.654.366k", "alex", "del monte", "cocteleria", "27042010")
est_dos = estudiante("15.765.3789", "maria", "bustos", "turismo", "06042019")
est_tres = estudiante("74.842.7370", "benjamin", "muñoz", "pedagogia", "31092009")

print(f"Bienveni@ {est_uno.nombre + " " + est_uno.apellido} a la especialidad de {est_uno.especialidad}")
print(f"Bienveni@ {est_dos.nombre + " " + est_dos.apellido} a la especialidad de {est_dos.especialidad}")
print(f"Bienveni@ {est_tres.nombre + " " + est_tres.apellido} a la especialidad de {est_tres.especialidad}")