import os # --> ejecuta comandos en consola
def limpiar_consola(): # limpian consola del terminal
    os.system('cls')

# BUCLE WHILE -----------------------------------------------------------------------------------------------------------------------
go = True
while go:
    print("\n\n === BIENENVENIDO ADMIN ===\nQué vas a hacer hoy?\n")
    print("1 -. mostrar ciudad")
    print("2 -. agregar miembro a un equipo")
    print("3 -. Mostrar equipo")
    print("4 -. Buscar equipo por nombre")
    print("5 -. Validar nombre de equipo")
    print("6 -. Validar tipo usuario")
    print("7 -. Mostrar info usuario")
    print("8 -. buscar tipo de usuario pon nombre")
    print("9 -. Inscribir equipo al torneo")
    print("10 -. Mostar info torneo")
    print("11 -. mostar datos usuario")
    print("12 -. cambiar email usuario")
    print("13 -. validar edad usuario")
    
    
    elect = int(input("\nPor favor elegir una del las opciones: "))
    if elect == 1:
        limpiar_consola()
        print("Dirigiendo al ejercicio uno")
        pass
    
    elif elect == 2:
        limpiar_consola()
        print("Dirigiendo al ejercicio dos")
        pass
    
    elif elect == 3:
        limpiar_consola()
        print("Dirigiendo al ejercicio tres")
        pass
    
    elif elect == 4:
        limpiar_consola()
        print("Dirigiendo al ejercicio cuatro")
        pass
    
    elif elect == 5:
        limpiar_consola()
        print("Dirigiendo al ejercicio cinco")
        pass
    
    elif elect == 6:
        limpiar_consola()
        print("Dirigiendo al ejercicio seis")
        pass
    
    elif elect == 7:
        limpiar_consola()
        print("Dirigiendo al ejercicio siete")
        pass
    
    elif elect == 8:
        limpiar_consola()
        print("Dirigiendo al ejercicio ocho")
        pass
    
    elif elect == 9:
        limpiar_consola()
        print("Dirigiendo al ejercicio nueve")
        pass
    
    elif elect == 10:
        limpiar_consola()
        print("Dirigiendo al ejercicio diez")
        pass
    
    elif elect == 11:
        limpiar_consola()
        print("Dirigiendo al ejercicio once")
        pass
    
    elif elect == 12:
        limpiar_consola()
        print("Dirigiendo al ejercicio doce")
        pass
    
    elif elect == 13:
        limpiar_consola()
        print("Dirigiendo al ejercicio trece")
        pass
    
    elif elect == 0:
        limpiar_consola()
        print("ok bye...")
        go = False
    
    else:
        print("Por favor seleccionar elemento válido...")