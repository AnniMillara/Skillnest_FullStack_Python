import os
from usuario import Usuarios

def limpiar_consola():
    os.system('cls')

continuar = True
while continuar:
    print('\n==============================')
    print('SISTEMA DE USUARIOS')
    print('==============================')
    
    print('\n⁰-. Cerrar')
    print('¹-. Iniciar Sesión')
    
    opcion = int(input('Por favor ingresar acción:_'))
    if opcion == 1:
        name = input("Por favor ingresar usuario:_").strip()
        word = input("Por favor ingresar contraseña:_").strip()
        
        if name != "" and word != "":
            Usuarios.revisar(name, word)
    elif opcion == 0:
        print('Hasta la proxima¡!')
        continuar = False
    else:
        print('Por favor ingresar elemento válido...')