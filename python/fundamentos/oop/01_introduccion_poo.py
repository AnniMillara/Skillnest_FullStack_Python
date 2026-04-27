# ⍝ʕ´•ᴥ•`ʔ⍝
class Usuario: # Se crea la「clase」usuario
    # constructor ➠ contiene instrucciones para crear una  nueva instancia de la clase
    # self ➠ propio
    def __init__(self):
        # self ➠ propio
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0

# Instancias de una clase
miyagi = Usuario()
daniel = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Nariyoshi

daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
print(daniel.nombre) #Imprime: Daniel