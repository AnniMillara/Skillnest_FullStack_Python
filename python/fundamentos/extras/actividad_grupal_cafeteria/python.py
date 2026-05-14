class CafeteriaCliente:
    # clase
    total_clientes = []
    
    # instancias
    def __init__(self, nombre, puntos_acumulados = 0, saldo_pendiente = 0, tipo_membresía = "Bronce"):
        self.nombre = nombre
        self.puntos_acumulados = puntos_acumulados
        self.saldo_pendiente = saldo_pendiente
        self.tipo_membresía = tipo_membresía
        CafeteriaCliente.total_clientes.append(self.nombre)
        
    def realizar_compra(self, monto):
        # Aumentar saldo pendiente
        # Pra bucle while
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
        return f"{self.nombre} realizó una compra, de: ${self.saldo_pendiente} y \nacumuló un total de: {self.puntos_acumulados}pts \n"
    
    def pagar_saldo(self, monto):
        # Validar el pago
        print(f"Debes un total de: ${self.saldo_pendiente}")
        if monto == self.saldo_pendiente:
            print(f"Total pagado correctamente!!\n")
            self.saldo_pendiente -= monto
        elif monto > self.saldo_pendiente:
            print(f"Te queda un total de: ${monto - self.saldo_pendiente} vuelto\n")
            self.saldo_pendiente = 0
        else:
            print("Paga el total.")
            self.saldo_pendiente -= monto
            return f"Aun debes un total de: ${self.saldo_pendiente}\n"
    
    @classmethod
    def mostrar_total_clientes(cls):
        return len(cls.total_clientes)
    
    @staticmethod
    def validar_membresia(tipo):
        membresias_validas = ["Bronce", "Plata", "Oro"] # <-- arreglo
        for i in range(len(membresias_validas)):
            if membresias_validas[i].lower() == tipo.lower():
                return True
        return False

user1 = CafeteriaCliente("Patty Warren")
user2 = CafeteriaCliente("Sergius Huang")
user3 = CafeteriaCliente("Ian  ")

print(user1.realizar_compra(29000))
print(user1.pagar_saldo(2900))

print(f"Hay un total de: {CafeteriaCliente.mostrar_total_clientes()} clientes\n")

print(f"El usuario es: {user2.validar_membresia("PLATA")}")
print(f"El usuario es: {user3.validar_membresia("ComóPerdón")}")
