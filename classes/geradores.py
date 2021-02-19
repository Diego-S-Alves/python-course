"""
generators are iterators
obs, o contrario não é verdadeiro, nem todo iterator é um generator

funçoes geradores podem criar generators
palavra reservada "yield"
expressoes geradoras
diferenças entre:
"""

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


print(list(conta_ate(10)))
