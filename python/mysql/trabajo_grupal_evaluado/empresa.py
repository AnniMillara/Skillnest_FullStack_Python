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

class libro:
    libros = []
    def __init__(self, titulo, isbn, autor, disponibilidad = True):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor()
        self.disponibilidad = disponibilidad
        libro.libros.append(self.titulo)
    
    # recibir nombre y decir si eta disponible o no
    @classmethod
    def buscar_libro(cls, self, nombre):
        if nombre in cls.libros:
            return self.disponibilidad
        else:
            return f"No se encuentra disponible"


class genero_libro:
    def __init__(self, nombre_genero, descripcion):
        self.nombre = nombre_genero
        self.descripcion = descripcion 

class prestamo:
    def __init__(self, fecha_prestamo, fecha_devolucion, fecha_limite):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_limite = fecha_limite