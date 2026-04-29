import os
def limpiar_consola():
    os.system('cls')

# Reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
def menorMayor(lista):
    mayor = 0
    menor = 1000000000000000000000000
    
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
        if lista[i] < menor:
            menor = lista[i]
        else:
            pass
    return f'El numero mayor de la lista: {lista} es el {mayor} y el menor es el {menor}'

# Reciba una cadena de texto y cuente cuántas vocales contiene.
def cadena(oka):
    texto = oka.lower()
    vocal = 0
    tildes = 0
    for i in texto:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vocal += 1
        elif i == "á" or i == "é" or i == "í" or i == "ó" or i == "ú":
            tildes += 1
        else:
            pass
    return f'El  texto tiene {vocal + tildes} vocales, las cuales {tildes} llevan tildes'

# Reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.
def nombre(cadena):
    pasan = []
    for i in range(len(cadena)):
        if len(cadena[i]) > 5:
            pasan.append(cadena[i])
        else:
            pass
    
    return f'Los nombres que pasan son: {" ♥︎ ".join(pasan)}'

# Reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
def decimales(notas):
    prom = 0
    for i in range(len(notas)):
        prom += notas[i]
        if notas[i] >= 4.0 and notas[i] <= 7.0:
            print(f"➢ El estudiante {i + 1} pasa con un {notas[i]}")
        elif notas[i] < 4.0 and notas[i] >= 1.0:
            print(f"➢ El estudiante {i + 1} lamentablemente no pasa con un {notas[i]} ☹")
        else:
            print("Aqual valor no es válido...")
    print(f"El promedio de las notas es de {prom / (len(notas)+1)}")

# Reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
def desc(num):
    return num * 0.9

def productos(mercado):
    precio = []
    for i in range(len(mercado)):
        precio.append(desc(mercado[i]))
    
    for i in range(len(mercado)):
        print(f"El antigo precio es de {mercado[i]} y el nuevo es de {precio[i]}")

# Reciba un número entero y determine si es par o impar.
def im(num):
    if num == "" or type(num) != str:
        if num % 2 == 0:
            print(f"El {num} es par ദ്ദി ˉ͈̀꒳ˉ͈́ )✧")
        else:
            print(f"El {num} es impar /ᐠ • ˕ •マ ?")
    else:
        print("Por favor ingresar elemento válido")

# Reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).
def edades(personas):
    mayores = 0 
    for i in range(len(personas)):
        if personas[i] >= 18:
            mayores += 1
    return f"Hay {mayores} personas mayores"

# Reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
def palabras(oka):
    noPuedeSer = {}
    for i in range(len(oka)):
        cantVeces = 0
        for f in range(len(oka)):
            if oka[i] == oka[f]:
                cantVeces += 1
        noPuedeSer[oka[i]] = cantVeces
    return noPuedeSer

# Reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.
def exclusion(justiciaParaLosNegativos):
    discriminadores = []
    for i in range(len(justiciaParaLosNegativos)):
        if justiciaParaLosNegativos[i] >= 0:
            discriminadores.append(justiciaParaLosNegativos[i])
    return discriminadores

# Reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.
def stockcio(pelusas):
    for prod, cant in pelusas.items():
        if cant < 5:
            print(f"¡ALERTA! el producto {prod} tiene muy poco stock({cant})")

# 合 Menu ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
sueño = False
print("Bienvenido Python!! Que deseas ver hoy?")

while not sueño:
    inp = int(input("\nPor favor elegir ejercicio(1 - 10, 0 = salir):_"))
    
    if inp == 1:
        limpiar_consola()
        print("LLevando al ejercicio uno \n ❝ Mayor y menor ❞")
        print(menorMayor([100, -244, 33, 4]))
    elif inp == 2:
        limpiar_consola()
        print("LLevando al ejercicio dos \n ❝ Cantidad de vocales ❞")
        print(cadena("Uso de funciones con parámetros"))
    elif inp == 3:
        limpiar_consola()
        print("LLevando al ejercicio tres \n ❝ Nombres con mas de 5 Letras ❞")
        print(nombre(["melisa", "alice", "pan", "isi", "okokoko"]))
    elif inp == 4:
        limpiar_consola()
        print("LLevando al ejercicio cuatro \n ❝ Notas y promedios ❞")
        print(decimales([6.5, 4, 3.5, 7, 2.4]))
    elif inp == 5:
        limpiar_consola()
        print("LLevando al ejercicio cinco \n ❝ Productos con descuentos ❞")
        print(productos([10000, 44000, 330, 450]))
    elif inp == 6:
        limpiar_consola()
        print("LLevando al ejercicio seis \n ❝ Par o Impar ❞")
        print(im("okaoka"))
    elif inp == 7:
        limpiar_consola()
        print("LLevando al ejercicio siete \n ❝ Mayores de edad ❞")
        print(edades([10, 24, 33, 14]))
    elif inp == 8:
        limpiar_consola()
        print("LLevando al ejercicio ocho \n ❝ Cuantas veces aparece una palabra ❞")
        print(palabras(["manzana", "pera", "platano", "oro", "brocoli", "manzana", "pera"]))
    elif inp == 9:
        limpiar_consola()
        print("LLevando al ejercicio nueve \n ❝ Discriminadores de negativos ❞")
        print(exclusion([100, -244, 33, 4]))
    elif inp == 10:
        limpiar_consola()
        print("LLevando al ejercicio diez \n ❝ Stock ❞")
        print(stockcio({"manzana" : 9, "pera" : 1, "platano" : 87, "oro" : 3, "brocoli" : 40}))
    elif inp == 0:
        limpiar_consola()
        print("Saliendo𓍯𓂃𓏧♡")
        sueño = True
    else:
        print("ඞඞඞඞඞඞඞඞඞඞ")