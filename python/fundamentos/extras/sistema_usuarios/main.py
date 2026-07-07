import os
from usuario import Usuarios

def limpiar_consola():
    os.system('cls')

continuar = True
resultado = False

while continuar:
    print('\n==============================')
    print('SISTEMA DE USUARIOS')
    print('==============================')
    
    print('\n0-. Cerrar')
    print('1-. Iniciar Sesion')
    
    opcion = int(input('Por favor ingresar accion:_'))
    if opcion == 1:
        limpiar_consola()
        name = input("Por favor ingresar usuario:_").strip()
        word = input("Por favor ingresar contraseña:_").strip()
        
        if name != "" and word != "":
            resultado = Usuarios.revisar(name, word)
            
        #Si es ADMIN
        if resultado:
            seguir = True
            
            while seguir:
                print('\n==============================')
                print('ACTIVIDADES ADMIN')
                print('==============================')
    
                print('\n0-. Cerrar Sesion')
                print('1-. Registrar usuario')
                print('2-. Listar usuarios')
                print('3-. Buscar usuario')
                print('4-. Modificar usuario')
                print('5-. Eliminar usuario')
                
                seleccion = int(input('Por favor ingresar accion:_'))
                
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
                    Usuarios.eliminar()
                elif seleccion == 0:
                    limpiar_consola()
                    print('^._.^ฅ')
                    seguir = False
                else:
                    limpiar_consola()
                    print('Por favor ingresar un elemento valido')
        
    elif opcion == 0:
        limpiar_consola()
        print('Hasta la proxima!')
        continuar = False
    else:
        print('Por favor ingresar elemento valido...')