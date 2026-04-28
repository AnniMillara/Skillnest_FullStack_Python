import os
# extra -------------------------------------------------------------------------------------------------------------------------------------------
def limpiar_consola():
    os.system('cls')

print("Bienvenido python!! Que vas a hacer hoy?! \n ₍ᐢ. ̫ .ᐢ₎")

class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []

    def agregar_a_lista(self, titulo):
        self.lista_reproduccion.append(titulo)

    def ver_contenido(self, titulo):
        if titulo in self.lista_reproduccion:
            print(f"▶ Reproducendo {titulo}")
        else:
            new = input(f"Deseas ingresar {titulo} a la lista de reproducción?(si/no):_")
            if new.lower() == "si":
                self.lista_reproduccion.append(titulo)
            elif new.lower() == "no":
                print(self.lista_reproduccion)
            else:
                print("Por favor ingresar elemento valido")

    def cambiar_suscripcion(self, nueva_suscripcion):
        if nueva_suscripcion.lower() == "gratis" or nueva_suscripcion.lower() == "estándar" or nueva_suscripcion.lower() == "premium":
            self.suscripcion = nueva_suscripcion
        else:
            print("Elemento no valido")

    def mostrar_info_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Suscripción: {self.suscripcion}")
        print(f"Lista: {self.lista_reproduccion}")

# Crear usuarios - CORREGIDO: nombre y email como strings ---------------------------------------------------------------------------------------------------------------------------------
user1 = UsuarioStreaming("Ana", "ana@email.com")
user2 = UsuarioStreaming("Lucio", "lucio@email.com")
user3 = UsuarioStreaming("Victor", "victor@email.com")

# Menú principal ---------------------------------------------------------------------------------------------------------------------------------
conti = True

print("\nUsuarios disponibles:")
print("1 - Ana")
print("2 - Lucio") 
print("3 - Victor")

pin = input("Por favor ingresar número de usuario (1-3): ")

if pin <= 3 and pin > 0:
    while conti:
        print("\n----- 1) Agregar a la lista de reproducción -----")
        print("----- 2) Reproducir contenido -----")
        print("----- 3) Cambiar suscripción -----")
        print("----- 4) Mostrar info -----")
        print("----- 0) salir -----")
    
        hacer = input("Por favor ingresar número (0-4): ")
    
    # Usuario 1 - Ana
        if pin == "1":
            if hacer == "1":
                limpiar_consola()
                put = input("▸ ")
                if put != "":
                    user1.agregar_a_lista(put)
            elif hacer == "2":
                limpiar_consola()
                put = input("▸ ")
            if put != "":
                user1.ver_contenido(put)
            elif hacer == "3":
                limpiar_consola()
                put = input("▸ ")
                if put != "":
                    user1.cambiar_suscripcion(put)
            elif hacer == "4":
                limpiar_consola()
                user1.mostrar_info_usuario()
            elif hacer == "0":
                limpiar_consola()
                print("👋 ¡Hasta luego!")
                conti = False
            else:
                print("Opción no válida")
    
    # Usuario 2 - Lucio
        elif pin == "2":
            if hacer == "1":
                limpiar_consola()
                put = input("▸ ")
                if put != "":
                    user2.agregar_a_lista(put)
            elif hacer == "2":
                limpiar_consola()
                put = input("▸ ")
                if put != "":
                    user2.ver_contenido(put)
            elif hacer == "3":
                limpiar_consola()
                put = input("▸ ")
                if put != "":
                    user2.cambiar_suscripcion(put)
            elif hacer == "4":
                limpiar_consola()
                user2.mostrar_info_usuario()
            elif hacer == "0":
                limpiar_consola()
                print("👋 ¡Hasta luego!")
                conti = False
            else:
                print("Opción no válida")
    
    # Usuario 3 - Victor
        elif pin == "3":
            if hacer == "1":
                limpiar_consola()
                put = input("▸ ")
                if put != "":
                    user3.agregar_a_lista(put)
            elif hacer == "2":
                limpiar_consola()
                put = input("▸ ")
            if put != "":
                    user3.ver_contenido(put)
            elif hacer == "3":
                limpiar_consola()
                put = input("▸ ")
                if put != "":
                    user3.cambiar_suscripcion(put)
            elif hacer == "4":
                limpiar_consola()
                user3.mostrar_info_usuario()
            elif hacer == "0":
                limpiar_consola()
                print("👋 ¡Hasta luego!")
                conti = False
            else:
                print("Opción no válida")
