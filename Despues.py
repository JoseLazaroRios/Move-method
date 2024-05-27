class Cliente:
    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = cuenta

    def obtener_descuento(self):
        return self.cuenta.calcular_descuento()

class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def calcular_descuento(self):
        if self.saldo > 5000:
            return self.saldo * 0.07
        else:
            return 0