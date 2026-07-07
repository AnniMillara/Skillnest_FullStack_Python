import os
from usuario import Usuarios

def limpiar_consola():
    os.system('cls')

## WHILE ------------------------------------------------------------------------------------------------------------------------------

continuar = True
resultado = False

while continuar:
    print('\n==============================')
    print('SISTEMA DE USUARIOS')
    print('==============================')
    
    print('\n⁰-. Cerrar')
    print('¹-. Iniciar Sesión')
    
    opcion = int(input('Por favor ingresar acción:_'))
    if opcion == 1:
        limpiar_consola()
        name = input("Por favor ingresar usuario:_").strip()
        word = input("Por favor ingresar contraseña:_").strip()
        
        if name != "" and word != "":
            resultado = Usuarios.revisar(name, word) #Cosa rara para ver si es admin (que horrible)
            
        #Si es ADMIN
        if resultado:
            seguir = True
            
            while seguir:
                print('\n==============================')
                print('ACTIVIDADES ADMIN')
                print('==============================')
    
                print('\n⁰-. Cerrar Sesión')
                print('¹-. Registrar usuario')
                print('²-. Listar usuarios')
                print('³-. Buscar usuario')
                print('⁴-. Modificar usuario')
                print('⁵-. Eliminar usuario')
                
                seleccion = int(input('Por favor ingresar acción:_'))
                
                if seleccion == 1:
                    limpiar_consola()
                    Usuarios.ingresar()
                elif seleccion == 2:
                    limpiar_consola()
                    Usuarios.listar()
                elif seleccion == 3:
                    limpiar_consola()
                    Usuarios.buscar()
                elif seleccion == 4:
                    limpiar_consola()
                    Usuarios.modificar()
                elif seleccion == 5:
                    limpiar_consola()
                elif seleccion == 0:
                    limpiar_consola()
                    print('^._.^ฅ')
                    seguir = False
                else:
                    limpiar_consola()
                    print('Por favor ingresar un elemnto válido')
        
    elif opcion == 0:
        limpiar_consola()
        print('Hasta la proxima¡!')
        continuar = False
    else:
        print('Por favor ingresar elemento válido...')