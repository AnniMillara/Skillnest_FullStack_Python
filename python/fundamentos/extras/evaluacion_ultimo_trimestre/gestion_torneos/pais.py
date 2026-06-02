class pais:
    def __init__(self, nombre_pais):
        self.nombre_pais = nombre_pais
    
    def mostrar_pais(self):
        return f"País: {self.nombre_pais}"

chile = pais("Chile")
venezuela = pais("Venezuela")