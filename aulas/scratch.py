matriz_1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz_2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

matriz_3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for linha in range(4):
    for coluna in range(4):
        matriz_1[linha][coluna] = int(input("informe os numeros da matriz  1 :"))

for linha in range(4):
    for coluna in range(4):
        matriz_2[linha][coluna] = int(input("informe os numeros da matriz 2 : "))

for impressao_matriz in matriz_1, matriz_2:
    print(impressao_matriz)

print('\n')

for linha in range(4):
    for coluna in range(4):
        if matriz_1[linha][coluna] > matriz_2[linha][coluna]:
            matriz_3[linha][coluna] = matriz_1[linha][coluna]
        else:
            matriz_3[linha][coluna] = matriz_2[linha][coluna]

print(matriz_3)
