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
        return  f"Nombre completo: {self.nombre} {self.apellido}\nFecha_nacimiento: {self.fecha_nacimiento}\nfecha_fallecimiento: {self.fecha_fallecimiento}\nNacionalidad: {self.nacionalidad}\n"

class Libro:
    libros = []
    
    def __init__(self, titulo, isbn, disponibilidad=True):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor  # Recibe objeto Autor ya creado
        self.disponibilidad = disponibilidad
        Libro.libros.append(self)
    
    @classmethod
    def buscar_libro_por_titulo(cls, titulo):
        for libro in cls.libros:
            if libro.titulo == titulo:
                return f"Disponible: {libro.disponibilidad}"
        return "Libro no encontrado"

class genero_libro:
    def __init__(self, nombre_genero, descripcion):
        self.nombre = nombre_genero
        self.descripcion = descripcion 
    
    def mostrar_genero(self):
        return f"Género: {self.nombre}\nDescripción: {self.descripcion}\n"

class estado_prestamos:
    def __init__(self, nombre_estado, descripcion_estado):
        self.nombre_estado = nombre_estado
        self. descripcion_estado =  descripcion_estado

class prestamo:
    def __init__(self, fecha_prestamo, fecha_devolucion, fecha_limite):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_limite = fecha_limite
    
    def registrar_prestamo(self):
        if not self.libro.disponibilidad:
            return f"Error: El libro '{self.libro.titulo}' no está disponible.\n"
        
        self.libro.disponibilidad = False
        return f"Préstamo registrado: {self.usuario.nombre} tomó '{self.libro.titulo}'. Fecha límite: {self.fecha_limite}\n"

userUno = usuario("pepito", "pepitolegustanlaspapas@gmail.com", "+56999991099")
userDos = usuario("ian", "ianlefipan@gmail.com", "+56971659347")
userTres = usuario("Martin", "martinignacio@gmail.com", "+56962788882")

autor1 = autor("Edgar Allan", "Poe", "Estadounidense", "19-01-1809", "Escritor y poeta estadounidense", "07-10-1849")
autor2 = autor("Franz", " Kafka", "Checo", "03-7-1883", "Escritor checo", "03-06-1924")
autor3 = autor("Jorge", "Baradit", "Chileno", "11-06-1969", "Escritor Chileno")

libro1 = Libro("El cuervo y otros poemas", "978-84-376-0494-7")
libro2 = Libro("La metamorfosis", "978-84-206-3365-9")
libro3 = Libro("Historia secreta de Chile", "978-956-8992-62-8")

# Para asignar autores a los libros
libro1.autor = autor1
libro2.autor = autor2
libro3.autor = autor3

print(libro1.autor.informacion())