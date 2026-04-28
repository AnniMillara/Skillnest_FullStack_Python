class Usuario:
    # self ➤ contiene los atributos de la clase
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    
    # metodo dentro de la clase
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #El monto aumenta saldo_pagar
    def aumentar_credito(self, cuanto):
        self.limite_credito += cuanto
    def cambiar_correo(self, inp):
        self.email = inp

# ⏷Instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

segunda_compra = 300
print("\n------ Compras nariyoshi ------")
# Se llama al metodo y se le suma saldo a pagar
miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
miyagi.hacer_compra(segunda_compra)
print(f"Monto total de {miyagi.nombre}: ${miyagi.saldo_pagar}")
# Imprimir cuanto credito le queda a miyagi
print(f"A {miyagi.nombre} le quedan: ${miyagi.limite_credito - miyagi.saldo_pagar}")

# cuanto le queda a daniel 2 compras y muestra saldo a pagar
print("\n------ Compras daniel ------")
daniel.hacer_compra(27000)
daniel.hacer_compra(45)
print(f"Daniel debe pagar: ${daniel.saldo_pagar} por lo que le quedaria un saldo de {daniel.limite_credito - daniel.saldo_pagar}")

"""
Tarea : crear un nuevo metodo que permita aumentar el limite de credito 
"""
print("\n----- Cambiar credito -----")
cuan = input("Desea aumentar credito (si/no):_")
if cuan.lower() == "si":
    nombre = input("Ingresar nombre:_")
    if nombre.lower() == "miyagi" or nombre.lower() == "nariyoshi":
        num = int(input("Ingresar aumento: $"))
        if num != 0:
            miyagi.aumentar_credito(num)
            print(miyagi.limite_credito)
    elif nombre.lower() == "daniel" or nombre.lower() == "larusso":
        num = int(input("Ingresar aumento: $"))
        if num != 0:
            daniel.aumentar_credito(num)
            print(daniel.limite_credito)
    else:
        print("Lo sentimos, no te encontramos en nuestra base de datos ˙◠˙")
elif cuan.lower() == "no":
    print("ദ്ദി˙ ᴗ ˙ )")
    pass
else:
    print("Por favor ingresar elemento valido")
"""
Tarea : crear un nuevo metodo que permita cambiar el email
"""
print("\n----- Cambiar email -----")
em = input("Deaseas cambiar email?(si/no):_")

if em.lower() == "si":
    nombre = input("Ingresar nombre:_")

    if nombre.lower() == "miyagi" or nombre.lower() == "nariyoshi":
        correo = input("Ingresar nuevo correo:_")
        miyagi.cambiar_correo(correo)
        print(f"Correo actualizado: {miyagi.email}@gmail.com")
    elif nombre.lower() == "daniel" or nombre.lower() == "larusso":
        correo = input("Ingresar nuevo correo:_")
        daniel.cambiar_correo(correo)
        print(f"Correo actualizado: {daniel.email}@gmail.com")
    else:
        print("Lo sentimos, no te encontramos en nuestra base de datos ˙◠˙")
elif em.lower() == "no":
    print("(👍🏻ᴗ _ᴗ)👍🏻")
    pass
else:
    print("Ingresar elemento valido")