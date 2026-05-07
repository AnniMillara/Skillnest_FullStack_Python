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
    def __init__(self, usuario, saldo_pendiente, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.saldo_pendiente = saldo_pendiente
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion] # <-- Importante

    def realizar_pago(self, monto):
        self.saldo_pendiente -= monto
        if self.saldo_pendiente < 0:
            print("No queda mas saldo...")
            self.saldo_pendiente = 0

    def cambiar_suscripcion(self, nuevo_tipo):
        self.tipo_suscripcion = nuevo_tipo
        self.costo_mensual = self.costos_suscripcion[nuevo_tipo]

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion != "Gratis":
            print("Por favor disfruta de nuestro contenido exclusivo como tu quieras!!")
        elif self.tipo_suscripcion == "Gratis":
            print(f"Lo sentimos tu suscripcion es de tipo {self.tipo_suscripcion}")

    def mostrar_info_suscripcion(self):
        print(f"\nuser ⧽ {self.usuario}")
        print(f"tipo de suscripcion ⧽ {self.tipo_suscripcion}")
        print(f"costo mensual ⧽ ${self.costo_mensual}")
        print(f"saldo pendiente ⧽ ${self.saldo_pendiente}")

# usuarios --------------------------------------------------------------------------------------------------------------------------------------------------------
user1 = SuscripcionStreaming("milkyway", 27000, "Estándar")
user2 = SuscripcionStreaming("cookiescheeserunning", 0,)
user3 = SuscripcionStreaming("thethirdman", 3000, "Premium")

usuarios = [user1, user2, user3]
# Lo necesitoooooo ------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Hello again, what you wanna do today?!")
sueño = True


usuario = int(input("Podrias ingresar tu llave de usuario por favor?(1-3):_"))
while sueño:
    print("1-. Pagar")
    print("2-. Cambiar suscripción")
    print("3-. Contenido exclusivo")
    print("4-. Info")
    seleccion = int(input("Por favor ingresar actividad:_"))