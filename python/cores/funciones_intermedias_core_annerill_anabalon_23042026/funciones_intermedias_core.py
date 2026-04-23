import os
# extra -------------------------------------------------------------------------------------------------------------------------------------------
def limpiar_consola():
    os.system('cls')

"""
Evaluacion core
"""
# 1) 
# En puntajes, cambia el valor 300 por 600 (ajuste en los puntajes de la primera ronda).
# En streamers, cambia el nombre de ”GameNinjaPro” a ”EliteGamerX”.
# En eventos, cambia la ciudad “Las Vegas” por “San Francisco”.
# En ubicacion, cambia el valo de ”latitud” a 40.712776 (cambiando la sede del torneo a Nueva York).

# Ranking de puntajes de un torneo de eSports -----------------------------------------------------------------------------------------------------------------------------------
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
puntajes[1][0] = 600

# Lista de creadores de contenido en una plataforma de streaming ----------------------------------------------------------------------------------------------------------------------
streamers = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]
streamers[0]["nombre"] = "EliteGamerX"

# Eventos en distintas ciudades del mundo --------------------------------------------------------------------------------------------------------------------------------------------
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}
eventos["Estados Unidos"][2] = "San Francisco"

# Coordenadas de la sede de un torneo internacional ---------------------------------------------------------------------------------------------------------------------------------------------
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]
ubicacion[0]["latitud"] = 40.712776

# 2) Creacion de funciones ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

""" Funcion uno """
def iterar_diccionario(lista):
    inte = input("Ingresa un numero (0/1):_")
    
    if inte == "0":
        print(f"nombre - {lista[0]["nombre"]}, seguidores - {lista[0]["seguidores"]}")
    elif inte == "1":
        print(f"nombre - {lista[1]["nombre"]}, seguidores - {lista[1]["seguidores"]}")
    else:
        print("Por favor ingresar valor valido")

""" Funcion dos """
def obtener_valores(clave, lista):
    for i in range(len(lista)):
        actual = lista[i]
        if actual in lista:
            print(lista[i][clave])
        else:
            pass

""" Funcion tres """
# diccionario especial
categorias = {
    "juegos_populares": [
        "Fortnite", 
        "Minecraft", 
        "Valorant", 
        "GTA V",
    ],
    "ciudades_eventos": [
        "Nueva York",
        "Madrid",
        "Tokio",
    ]
}

def mostrar_informacion(diccionario):
    for categoria, lista in diccionario.items():
        print(f"{len(lista)} {categoria.upper()}")
        for item in lista:
            print(item)

# ⫶☰ MENU
print("Bienvenido a python!")
print("Este es un menu, por favor seleccionar del uno al tres para revisar las funciones, ")
print("cuatro para ver los diccionarios y 0 para salir")

seguir = True
while seguir:
    seleccion = input("Seleccionar nivel >> ")
    if seleccion == "1":
        limpiar_consola()
        print("Navegando al nivel uno...⏅")
        print(iterar_diccionario(streamers))
    elif seleccion == "2":
        limpiar_consola()
        print("Navegando al nivel dos...⛴")
        obtener_valores("nombre", streamers)
        obtener_valores("seguidores", streamers)
    elif seleccion == "3":
        limpiar_consola()
        print("Navegando al nivel tres...☸")
        mostrar_informacion(categorias)
    elif seleccion == "4":
        limpiar_consola()
        print("Mostrando diccionarios...𓂃 ོ☼𓂃")
        print("Diccionario de puntajes")
        print(puntajes)
        print("Diccionario de streamers")
        print(streamers)
        print("Diccionario de eventos")
        print(eventos)
        print("Diccionario de ubicaciones")
        print(ubicacion)
        print("Diccionario de categorias")
        print(categorias)
        print("Diccionario de datos")
    elif seleccion == "0":
        limpiar_consola()
        print("Saliendo...")
        seguir = False
    else:
        print("No válido...")