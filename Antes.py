class Cliente:
    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = cuenta

    def calcular_descuento(self):
        if self.cuenta.saldo > 5000:
            return self.cuenta.saldo * 0.07
        else:
            return 0

class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo
