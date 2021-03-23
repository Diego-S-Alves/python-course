"""
high order functions - hof

funçoes que retornam outras funçoes como resultado ou mesmo que podemos passar
funçoes como argumnetos para outras funçoes e até mesmo criar variaveis do tipo de funçoes nos
nossos programas.

em python as funçoes sao first class citizens
nested functions = inner functions
"""

# definindo funçoes
def somar(a,b):
    return a+b

def calcular(num1, num2, funcao):
    return funcao(num1 + num2)

# nested functions
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai', 'Suma!', 'gosto de voce'))
    return humor() + pessoa

print(cumprimento('Diego'))
