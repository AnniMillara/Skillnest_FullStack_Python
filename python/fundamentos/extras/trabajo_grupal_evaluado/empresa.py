import os # --> ejecuta comandos en consola
def limpiar_consola(): # limpian consola del terminal
    os.system('cls')

class usuario:
    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
    
    def mostrar_datos(self):
        return f"Nombre: {self.nombre}\nCorreo: {self.correo}\nTeléfono: {self.telefono}\n"
    
    def cambiar_correo(self, email):
        if "@" in email:
            self.correo = email
            return f"Correo de: {self.correo} actualizado correctamente!!\n"
        else:
            return f"Correo no válido...\n"

class autor:
    def __init__(self, nombre, apellido, nacionalidad, fecha_nacimiento, biografia, fecha_fallecimiento = None):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.biografia = biografia
        self.fecha_fallecimiento = fecha_fallecimiento
    
    def informacion(self):
        return f"Nombre completo: {self.nombre} {self.apellido}\nFecha_nacimiento: {self.fecha_nacimiento}\nfecha_fallecimiento: {self.fecha_fallecimiento}\nNacionalidad: {self.nacionalidad}\n"

class Libro:
    libros = []
    
    def __init__(self, titulo, isbn, disponibilidad=True):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.disponibilidad = disponibilidad
        Libro.libros.append(self)
    
    @classmethod
    def buscar_libro_por_titulo(cls, titulo_buscar):
        titulo_buscar = titulo_buscar.lower()
        for libro in cls.libros:
            if titulo_buscar in libro.titulo.lower():
                return f"Título: {libro.titulo}\nDisponible: {libro.disponibilidad}"
        return "Libro no encontrado"

class prestamo:
    def __init__(self, fecha_prestamo, fecha_devolucion, fecha_limite): # parametros obligatorios
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_limite = fecha_limite
        self.usuario = None
        self.libro = None
    
    def registrar_prestamo(self, selecc, usuario_actual, libros_disponibles):
        selecc = selecc.lower()
        
        for eleccion in libros_disponibles:
            if selecc == eleccion.titulo.lower():
                if eleccion.disponibilidad:
                    self.usuario = usuario_actual
                    self.libro = eleccion
                    self.fecha_prestamo = "2026/05/27" # <-- Sobrescribe lo que llegó
                    self.fecha_limite = "2027/05/27" # <-- Sobrescribe lo que llegó
                    dev = input("Ingresar dia de devolucion: ")
                    self.fecha_devolucion = f"2026/06/{dev}" # <-- Sobrescribe lo que llegó
                    eleccion.disponibilidad = False
                    return f"El usuario: {self.usuario.nombre} tomo el libro {eleccion.titulo} el dia {self.fecha_prestamo}"
                else:
                    return f"El libro '{selecc}' no está disponible..."
        return f"Libro no encontrado..."

userUno = usuario("pepito", "pepitolegustanlaspapas@gmail.com", "+56999991099")
userDos = usuario("ian", "ianlefipan@gmail.com", "+56971659347")
userTres = usuario("Martin", "martinignacio@gmail.com", "+56962788882")

autor1 = autor("Edgar Allan", "Poe", "Estadounidense", "19-01-1809", "Escritor y poeta estadounidense", "07-10-1849")
autor2 = autor("Franz", "Kafka", "Checo", "03-07-1883", "Escritor checo", "03-06-1924")
autor3 = autor("Jorge", "Baradit", "Chileno", "11-06-1969", "Escritor Chileno")

libro1 = Libro("El cuervo y otros poemas", "978-84-376-0494-7")
libro2 = Libro("La metamorfosis", "978-84-206-3365-9")
libro3 = Libro("Historia secreta de Chile", "978-956-8992-62-8")

libro1.autor = autor1
libro2.autor = autor2
libro3.autor = autor3

print("Bienvenido usuario!! ✮⋆˙")
seguir = True

usuarios = [userUno, userDos, userTres]
autores = [autor1, autor2, autor3]
libros = [libro1, libro2, libro3]

user = int(input("Podrías ingresar tu llave de usuario por favor? (1-3): ")) - 1
usuario_actual = usuarios[user]

while seguir:
    print("\n1. Mostrar mis datos")
    print("2. Cambiar mi correo")
    print("3. Ver autor de un libro")
    print("4. Ver disponibilidad de un libro por título")
    print("5. Prestamo")
    print("0. Salir")
    
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        limpiar_consola()
        print(usuario_actual.mostrar_datos())
    elif opcion == 2:
        limpiar_consola()
        email_nuevo = input("Por favor ingresar nuevo email: ")
        print(usuario_actual.cambiar_correo(email_nuevo))
    elif opcion == 3:
        limpiar_consola()
        buscar = int(input("Por favor ingresar codigo autor(1-3): ")) - 1
        if 0 <= buscar < len(autores):
            print(autores[buscar].informacion())
        else:
            print("Código de autor inválido")
    elif opcion == 4:
        limpiar_consola()
        nombre = input("Ingresa el nombre del libro: ")
        print(Libro.buscar_libro_por_titulo(nombre))
    elif opcion == 5:
        limpiar_consola()
        nombre = input("Ingresa el nombre del libro: ")
        nuevo_prestamo = prestamo(None, None, None) # Valores temporales que serán reemplazados
        print(nuevo_prestamo.registrar_prestamo(nombre, usuario_actual, libros))
    elif opcion == 0:
        limpiar_consola()
        print("^._.^ฅ ¡Hasta luego!")
        seguir = False
    else:
        print("Opción inválida")