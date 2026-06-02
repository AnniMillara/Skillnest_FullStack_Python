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
torneo1 = Torneo("Torneo Apertura 2025", "League of Legends", "$5,000", "2025-03-10", "2025-04-20","Bastián", "santiago")

torneo1.inscribir_equipo()
torneo1.inscribir_equipo()