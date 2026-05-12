class CafeteriaCliente:
    total_clientes = []
    
    def __init__(self, nombre, puntos_acumulados = 0, saldo_pendiente = 0, tipo_membresía = "Bronce"):
        self.nombre = nombre
        self.puntos_acumulados = puntos_acumulados
        self.saldo_pendiente = saldo_pendiente
        self.tipo_membresía = tipo_membresía
        CafeteriaCliente.total_clientes.append(self.nombre)
        
    def realizar_compra(self, monto):
        # Aumentar saldo pendiente
        seguir = True
        aumentar = 1000
        if monto > 0 and monto != "":
            self.saldo_pendiente += monto
        # Aumentar puntos
        while seguir:
            if aumentar <= self.saldo_pendiente:
                aumentar += 1000
                self.puntos_acumulados += 10
            else:
                seguir = False
        print(f"{self.nombre} realizó una compra, de: ${self.saldo_pendiente} y \nacumuló un total de: {self.puntos_acumulados}pts")
    
    def pagar_saldo(self, monto):
        # Validar el pago
        print(f"Debes un total de: ${self.saldo_pendiente}")
        if monto == self.saldo_pendiente:
            print(f"Total pagado correctamente!!")
            self.saldo_pendiente -= monto
        elif monto > self.saldo_pendiente:
            print(f"Te queda un total de: ${monto - self.saldo_pendiente}")
            self.saldo_pendiente -= monto
        else:
            print("Paga el total.")
    
    @classmethod
    def mostrar_total_clientes(cls):
        return len(cls.total_clientes + 1)
    
    @staticmethod
    def validar_membresia(tipo):
        membresias_validas = ["Bronce", "Plata", "Oro"]
        for i in membresias_validas:
            if membresias_validas[i].lower() == tipo.lower():
                return True
            else:
                return False

user1 = CafeteriaCliente("Patty Warren")
user2 = CafeteriaCliente("Sergius Huang")
user3 = CafeteriaCliente("Ian Lefipan")

print(user1.realizar_compra(29000))
print(user1.pagar_saldo(2900))