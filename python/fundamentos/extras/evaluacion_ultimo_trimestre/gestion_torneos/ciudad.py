class ciudad:
    def __init__(self, nombre_ciudad, pais):
        self.nombre_ciudad = nombre_ciudad
        self.pais = pais
    
    def mostrar_ciudad_completa(self):
        return f"Ciudad: {self.nombre_ciudad}, {self.pais.mostrar_pais()}"

santiago = ciudad("Santiago", "chile")
caracas = ciudad("Caracas", "venezuela")