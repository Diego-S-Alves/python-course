import random
from collections import Counter

matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
lista = []

for linha in range(0, 5):
    for coluna in range(0, 5):
        num = random.randint(0, 99)
        matriz[linha][coluna] = num
        lista.append(num)
        for chave, vezes in Counter(lista).items():
            if vezes > 1:
                matriz[linha].pop()
                matriz[linha].append(random.randint(0, 99))
                lista.append(num)

for linha in range(0, 5):
    for coluna in range(0, 5):
        print(f'[{matriz[linha][coluna]:^7}]', end=' ')
    print()