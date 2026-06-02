class Equipo:
    equipos_registrados = []
    
    def __init__(self, nombre_equipo, fecha_creacion, capitan):
        self.nombre_equipo = nombre_equipo
        self.fecha_creacion = fecha_creacion
        self.capitan = capitan
        self.miembros = [capitan] # <-- lo establece como 1ER elemento
        Equipo.equipos_registrados.append(self) # <-- todos los equipos registrados
    
    def agregar_miembro(self, usuario):  # Método de instancia
        if usuario not in self.miembros: # <-- Sí no esta en el arreglo miembros
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

equipo1 = Equipo("Bandamax", "2024-01-01", "Lautaro")
equipo2 = Equipo("Supercalifrastilisticoespialidoso", "2024-01-01", "Martinez")