"""
https://docs.python.org/3/py-modindex.html
"""

from random import *
# importa todas as funções

from random import randint as rdi

# nomeando a função e não o módulo

"""
quando varios imports, costuma-se usar tupla
"""
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))

