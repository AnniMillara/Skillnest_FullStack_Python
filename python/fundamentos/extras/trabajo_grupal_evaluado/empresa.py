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

import os

def limpiar_consola():
    os.system('cls')

# ==================== CLASES ====================

class TipoUsuario:
    """Define los roles que pueden tener los usuarios en el sistema"""
    tipos_disponibles = []  # Atributo de clase
    
    def __init__(self, nombre_tipo, descripcion_tipo):
        self.nombre_tipo = nombre_tipo
        self.descripcion_tipo = descripcion_tipo
        TipoUsuario.tipos_disponibles.append(self)
    
    def mostrar_info(self):  # Método de instancia
        return f"Rol: {self.nombre_tipo}\nDescripción: {self.descripcion_tipo}"
    
    @classmethod
    def buscar_tipo_por_nombre(cls, nombre):  # Método de clase
        """Busca un tipo de usuario por su nombre"""
        for tipo in cls.tipos_disponibles:
            if tipo.nombre_tipo.lower() == nombre.lower():
                return tipo
        return None
    
    @staticmethod
    def validar_nombre_tipo(nombre):  # Método estático
        """Valida si el nombre del tipo es correcto"""
        nombres_validos = ["jugador", "admin", "jugador lider", "equipo tecnico", "comentarista"]
        return nombre.lower() in nombres_validos

class Pais:
    def __init__(self, nombre_pais):
        self.nombre_pais = nombre_pais
    
    def mostrar_pais(self):
        return f"País: {self.nombre_pais}"

class Ciudad:
    def __init__(self, nombre_ciudad, pais):
        self.nombre_ciudad = nombre_ciudad
        self.pais = pais
    
    def mostrar_ciudad_completa(self):
        return f"Ciudad: {self.nombre_ciudad}, {self.pais.mostrar_pais()}"

class Usuario:
    def __init__(self, nombre_completo, email, username, ciudad, edad, tipo_usuario):
        self.nombre_completo = nombre_completo
        self.email = email
        self.username = username
        self.ciudad = ciudad
        self.edad = edad
        self.tipo_usuario = tipo_usuario
    
    def mostrar_datos(self):  # Método de instancia
        return (f"Nombre: {self.nombre_completo}\n"
                f"Username: {self.username}\n"
                f"Email: {self.email}\n"
                f"Edad: {self.edad}\n"
                f"{self.ciudad.mostrar_ciudad_completa()}\n"
                f"{self.tipo_usuario.mostrar_info()}")
    
    def cambiar_email(self, nuevo_email):  # Método de instancia
        if "@" in nuevo_email and "." in nuevo_email:
            self.email = nuevo_email
            return f"Email actualizado a: {self.email}"
        return "Email no válido"
    
    @classmethod
    def crear_usuario_anonimo(cls, ciudad, tipo_usuario):  # Método de clase
        """Crea un usuario con datos por defecto"""
        return cls("Usuario Anónimo", "anonimo@email.com", "anonimo", ciudad, 18, tipo_usuario)
    
    @staticmethod
    def validar_edad(edad):  # Método estático
        """Verifica si la edad es apta para participar"""
        return edad >= 16

class Equipo:
    equipos_registrados = []
    
    def __init__(self, nombre_equipo, fecha_creacion, capitan):
        self.nombre_equipo = nombre_equipo
        self.fecha_creacion = fecha_creacion
        self.capitan = capitan
        self.miembros = [capitan]
        Equipo.equipos_registrados.append(self)
    
    def agregar_miembro(self, usuario):  # Método de instancia
        if usuario not in self.miembros:
            self.miembros.append(usuario)
            return f"{usuario.nombre_completo} se unió a {self.nombre_equipo}"
        return f"{usuario.nombre_completo} ya está en el equipo"
    
    def mostrar_equipo(self):
        miembros_str = "\n".join([f"  - {m.nombre_completo}" for m in self.miembros])
        return (f"Equipo: {self.nombre_equipo}\n"
                f"Capitán: {self.capitan.nombre_completo}\n"
                f"Miembros:\n{miembros_str}")
    
    @classmethod
    def buscar_equipo_por_nombre(cls, nombre):  # Método de clase
        for equipo in cls.equipos_registrados:
            if equipo.nombre_equipo.lower() == nombre.lower():
                return equipo
        return None
    
    @staticmethod
    def validar_nombre_equipo(nombre):  # Método estático
        return len(nombre) >= 3 and len(nombre) <= 50

class Torneo:
    torneos_disponibles = []
    
    def __init__(self, nombre_torneo, juego, premio, fecha_inicio, fecha_fin, organizador, ciudad):
        self.nombre_torneo = nombre_torneo
        self.juego = juego
        self.premio = premio
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.organizador = organizador
        self.ciudad = ciudad
        self.equipos_inscritos = []
        Torneo.torneos_disponibles.append(self)
    
    def inscribir_equipo(self, equipo):  # Método de instancia
        if equipo not in self.equipos_inscritos:
            self.equipos_inscritos.append(equipo)
            return f"Equipo {equipo.nombre_equipo} inscrito en {self.nombre_torneo}"
        return "Equipo ya inscrito"
    
    def mostrar_info(self):
        equipos_str = "\n".join([f"  - {e.nombre_equipo}" for e in self.equipos_inscritos]) if self.equipos_inscritos else "  - Sin equipos"
        return (f"Torneo: {self.nombre_torneo}\n"
                f"Juego: {self.juego}\n"
                f"Premio: {self.premio}\n"
                f"Fechas: {self.fecha_inicio} al {self.fecha_fin}\n"
                f"Organizador: {self.organizador.nombre_completo}\n"
                f"{self.ciudad.mostrar_ciudad_completa()}\n"
                f"Equipos:\n{equipos_str}")
    
    @classmethod
    def buscar_torneo_por_juego(cls, juego_buscar):  # Método de clase
        resultados = []
        for torneo in cls.torneos_disponibles:
            if juego_buscar.lower() in torneo.juego.lower():
                resultados.append(torneo)
        return resultados

# ==================== CREAR INSTANCIAS ====================

# Crear tipos de usuarios
tipo1 = TipoUsuario("Jugador", "Participa activamente en torneos")
tipo2 = TipoUsuario("Admin", "Organiza y supervisa torneos")

# Crear países
chile = Pais("Chile")
venezuela = Pais("Venezuela")

# Crear ciudades
santiago = Ciudad("Santiago", chile)
caracas = Ciudad("Caracas", venezuela)

# Crear usuarios
user1 = Usuario("Lautaro Martínez", "lautaro@email.com", "lautarito13", santiago, 22, tipo1)
user2 = Usuario("Camila Rojas", "camila@email.com", "camirojas", caracas, 19, tipo1)
user3 = Usuario("Mateo Fernández", "mateo@email.com", "mateo_nfc", santiago, 24, tipo2)

# Crear equipos
equipo1 = Equipo("Bandamax", "2024-01-01", user1)
equipo2 = Equipo("LosLucianos", "2024-01-01", user2)

# Agregar miembros
equipo1.agregar_miembro(user3)

# Crear torneos
torneo1 = Torneo("Torneo Apertura 2025", "League of Legends", "$5,000", "2025-03-10", "2025-04-20", user3, santiago)

# Inscribir equipos
torneo1.inscribir_equipo(equipo1)
torneo1.inscribir_equipo(equipo2)

# ==================== MENÚ INTERACTIVO ====================

print("=== SISTEMA DE GESTIÓN DE TORNEOS ===")
print("Bienvenido usuario!! ✮⋆˙")
seguir = True

# Listas para el menú
usuarios = [user1, user2, user3]
equipos = [equipo1, equipo2]
torneos = [torneo1]

# Seleccionar usuario
print("\nUsuarios disponibles:")
for i, user in enumerate(usuarios, 1):
    print(f"{i}. {user.nombre_completo} ({user.username})")

user = int(input("\nElige tu usuario (1-3): ")) - 1
usuario_actual = usuarios[user]
limpiar_consola()

while seguir:
    print(f"\n=== BIENVENIDO {usuario_actual.username.upper()} ===")
    print("1. Mostrar mis datos")
    print("2. Cambiar mi email")
    print("3. Mostrar información del torneo")
    print("4. Ver equipos registrados")
    print("5. Buscar torneo por juego (Método de clase)")
    print("6. Validar edad (Método estático)")
    print("7. Buscar tipo de usuario (Método de clase)")
    print("0. Salir")
    
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        limpiar_consola()
        print(usuario_actual.mostrar_datos())
    
    elif opcion == 2:
        limpiar_consola()
        email_nuevo = input("Ingresar nuevo email: ")
        print(usuario_actual.cambiar_email(email_nuevo))
    
    elif opcion == 3:
        limpiar_consola()
        print(torneo1.mostrar_info())
    
    elif opcion == 4:
        limpiar_consola()
        for equipo in equipos:
            print(equipo.mostrar_equipo())
            print()
    
    elif opcion == 5:
        limpiar_consola()
        juego = input("Ingresa el nombre del juego (ej: League, Valorant, CS): ")
        resultados = Torneo.buscar_torneo_por_juego(juego)  # Método de clase
        if resultados:
            for torneo in resultados:
                print(f"→ {torneo.nombre_torneo} - {torneo.juego}")
        else:
            print("No se encontraron torneos para ese juego")
    
    elif opcion == 6:
        limpiar_consola()
        print("=== VALIDAR EDAD ===")
        print("(Método estático - no necesita instancia)")
        edad_prueba = int(input("Ingresa una edad para validar: "))
        if Usuario.validar_edad(edad_prueba):  # Método estático
            print(f"Edad {edad_prueba} es válida para participar")
        else:
            print(f"Edad {edad_prueba} es muy joven (mínimo 16 años)")
    
    elif opcion == 7:
        limpiar_consola()
        print("=== BUSCAR TIPO DE USUARIO ===")
        print("(Método de clase - trabaja con la clase)")
        nombre_tipo = input("Ingresa nombre del rol (Jugador/Admin): ")
        tipo_encontrado = TipoUsuario.buscar_tipo_por_nombre(nombre_tipo)  # Método de clase
        if tipo_encontrado:
            print(tipo_encontrado.mostrar_info())
        else:
            print("Tipo de usuario no encontrado")
    
    elif opcion == 0:
        limpiar_consola()
        print("^._.^ฅ ¡Hasta luego!")
        seguir = False
    
    else:
        print("Opción inválida")