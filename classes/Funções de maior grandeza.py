"""
high order functions - hof

funçoes que retornam outras funçoes como resultado ou mesmo que podemos passar
funçoes como argumnetos para outras funçoes e até mesmo criar variaveis do tipo de funçoes nos
nossos programas.

em python as funçoes sao first class citizens

"""

# definindo funçoes
def somar(a,b):
    return a+b

def calcular(num1, num2, funcao):
    return funcao(num1 + num2)

# nested functions

