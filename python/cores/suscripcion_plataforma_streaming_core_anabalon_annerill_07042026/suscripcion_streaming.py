import os
def limpiar_consola():
    os.system('cls')
    
## Define la clase SuscripcionStreaming, que debe incluir:

# Atributos:
# usuario (nombre del usuario asociado a la suscripción)
# tipo_suscripcion (Gratis, Estándar, Premium)
# costo_mensual (según el tipo de suscripción)
# saldo_pendiente (monto acumulado que debe pagar el usuario)
# Métodos:
# realizar_pago(self, monto) reduce el saldo pendiente según el monto pagado.
# cambiar_suscripcion(self, nuevo_tipo) cambia el tipo de suscripción y ajusta el costo mensual.
# ver_contenido_exclusivo(self) permite el acceso a contenido según el tipo de suscripción. La suscripción “Gratis” no tiene acceso a contenido exclusivo.
# mostrar_info_suscripcion(self) muestra el estado actual de la suscripción del usuario.
#  Realizar las siguientes pruebas con instancias:

# Crea 3 usuarios con diferentes tipos de suscripción.
# Haz que el primer usuario intente ver contenido exclusivo, mejore su suscripción y pague su saldo.
# Haz que el segundo usuario vea contenido exclusivo, cambie su suscripción a Premium y pague dos veces.
# Haz que el tercer usuario intente pagar una cantidad menor a su saldo pendiente y vea contenido exclusivo.

class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5000, "Premium": 10000}
    
    # metodo constructor
    def __init__(self, usuario, saldo_pendiente, tipo_suscripcion="Gratis", puede_ver = True):
        self.usuario = usuario
        self.saldo_pendiente = saldo_pendiente
        self.tipo_suscripcion = tipo_suscripcion
        self.puede_ver = puede_ver
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion] # <-- Importante

    def realizar_pago(self, monto):
        if self.tipo_suscripcion == "Gratis":
                print(f"Que quieres pagar si tu suscripcion es gratis?!")
                print(f"Tu sueldo: ${monto} fue recuperado...")
        
        if self.saldo_pendiente == 0 or monto >= self.costo_mensual:
            print(f"Muchas gracias por mantenerte en nuestra plataforma!!")
            self.puede_ver = True
        elif monto < self.costo_mensual:
            print(f"Pagaste: ${monto} pero debes de pagar: ${self.costo_mensual} minimo...")
            self.puede_ver = False
            self.saldo_pendiente -= monto
    
    def cambiar_suscripcion(self, nuevo_tipo):
        self.tipo_suscripcion = nuevo_tipo
        self.costo_mensual = self.costos_suscripcion[nuevo_tipo]

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion != "Gratis" and self.puede_ver:
            print("Por favor disfruta de nuestro contenido exclusivo como tu quieras!!")
        elif not self.puede_ver:
            print(f"Lo sentimos pero debes de pagar tu suscripcion...")
        elif self.tipo_suscripcion == "Gratis":
            print(f"Lo sentimos tu suscripcion es de tipo {self.tipo_suscripcion}")

    def mostrar_info_suscripcion(self):
        print(f"\nuser ⧽ {self.usuario}")
        print(f"tipo de suscripcion ⧽ {self.tipo_suscripcion}")
        print(f"costo mensual ⧽ ${self.costo_mensual}")
        print(f"saldo pendiente ⧽ ${self.saldo_pendiente}")

# ejercicios -----------------------------------------------------------------------------------------------------------------
def ejercicio_uno():
    inp = int(input("Por favor ingresar monto a pagar:\n"))
    if inp != "":
        usuarios[user - 1].realizar_pago(inp)

def ejercicio_dos():
    sus = input("Por favor ingresar nueva suscripción:\n")
    if sus != "":
        usuarios[user - 1].cambiar_suscripcion(sus)

# usuarios --------------------------------------------------------------------------------------------------------------------------------------------------------
user1 = SuscripcionStreaming("milkyway", 27000, "Estándar")
user2 = SuscripcionStreaming("cookiescheeserunning", 0,)
user3 = SuscripcionStreaming("thethirdman", 300000, "Premium")

usuarios = [user1, user2, user3]
# Lo necesitoooooo ------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Hello again, what you wanna do today?!")
sueño = True


user = int(input("Podrias ingresar tu llave de usuario por favor?(1-3):_"))
while sueño:
    print("1-. Pagar")
    print("2-. Cambiar suscripción")
    print("3-. Contenido exclusivo")
    print("4-. Info")
    print("0-. Salir")
    
    hacer = int(input("Por favor ingresar actividad:_"))
    if hacer == 1:
        limpiar_consola()
        ejercicio_uno()
    elif hacer == 2:
        limpiar_consola()
        ejercicio_dos()
    elif hacer == 3:
        limpiar_consola()
        usuarios[user - 1].ver_contenido_exclusivo()
    elif hacer == 4:
        limpiar_consola()
        usuarios[user - 1].mostrar_info_suscripcion()
    elif hacer == 0:
        limpiar_consola()
        print("^._.^ฅ")
        sueño = False
    else:
        print("Opción no válida")