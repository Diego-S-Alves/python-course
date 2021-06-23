class fibonacci():
    def __init__(self):
        self.quant_termos = int(input('Quantos termos da sequencia?:'))
        self.n1 = 0
        self.n2 = 1

    def gerar_sequencia(self):
        if self.quant_termos <= 0:
            return 0
        elif self.quant_termos == 1:
            print('Primeiro termo da sequencia é ', self.quant_termos, ':')
        else:
            count = 0
            f_sqcia = []
            print(f"Sequência de Fibonacci com {self.quant_termos}:")
            while count < self.quant_termos:
                f_sqcia.append(self.n1)
                nth = self.n1 + self.n2
                self.n1 = self.n2
                self.n2 = nth
                count += 1
            print(f_sqcia)


sequencia = fibonacci()
print(sequencia)