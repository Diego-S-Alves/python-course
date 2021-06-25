class Conta:
    # função construtora
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


conta1 = Conta(123, "Diego S", 300.0, 1000.0)

print(conta1.numero)
