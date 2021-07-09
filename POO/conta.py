class Conta:
    # função construtora
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo {self.saldo} do titular {self.titular}")


conta = Conta(123, "Diego", 55.5, 1000.0)

print(conta.extrato())


