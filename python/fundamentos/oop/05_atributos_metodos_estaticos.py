# Atributos, Métodos de clase, Métodos estáticos

# DEFINICIÓN DE LA CLASE
class estudiante:
    # new: atributo de clase, nombre colegio y lista de estudiantes
    colegio = "Liceo Vate Vicnte Huidobro"
    estudiantes = []
    
    # Método constructor
    def __init__(self, nombre, nota):
        # Atributos de INSTANCIAS
        self.nombre = nombre
        self.nota = nota
        # Agregar elementos a la lista de estudiantes (insertar objeto dentro de...)
        estudiante.estudiantes.append(self)
    
    # Metodo de instancia (Como las funciones)
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
    
    # Método de CLASE
    ## Usa 'cls' porque trabaja con la información de la clase
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre
    @classmethod
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)
    
    # Método estático
    ## No usa 'cls' ni 'self' solo parámetros
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0 and nota <= 7.0:
            return True
        else:
            return False

## Creacion de objetos (instancias)
e1 = estudiante("Donovan", 4.0)
e2 = estudiante("Randy", 6.7)

# Usos de metodos de instancias
print("\n⏔⏔ Métodos de instancias ⏔⏔")
e1.mostrar_info() ## <= mostrar info de un estudiante
e2.mostrar_info()

# Usos de metodos de clase
print("\n⏔⏔ Atributo de clase ⏔⏔")
print(e1.colegio) ## <= mostrar colegio de un estudiante
print(e2.colegio)

# Uso de metodo de clase
print("\n⏔⏔ Método de clase ⏔⏔")
estudiante.cambiar_colegio("Nuestro mundo")
print(e1.colegio) ## <= mostrar colegio de un estudiante
print(e2.colegio)

# Contar estudiantes
print("\n⏔⏔ contar estudiantes ⏔⏔")
print(f"Total estudiantes : {estudiante.cantidad_estudiantes()}")

# Uso de metodo estatico
print("\n⏔⏔ Método estatico ⏔⏔")
print(e1.colegio) ## <= mostrar colegio de un estudiante
print(e2.colegio)

## Función repaso
## Crear función que valide usuario y contraseña
def validar(user, passw):
    if user == "donovancallate" and passw == "MeDueleLaCabeza":
        print(f"Bievenvenido de nuevo {user}")
        return "( ദ്ദി ˙ᗜ˙ )"
    else:
        
        print(f"Lo sentimos, el usuario {user} no existe")
        return "(≖_≖ )NO"

def enviar():
    print()
    inp = input("Por favor ingresar usuario:_")
    inpDos = input("Por favor ingresar contraseña:_")
    
    validador = validar(inp, inpDos)
    print(validador)

enviar()