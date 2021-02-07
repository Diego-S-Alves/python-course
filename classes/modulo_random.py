"""
modulo random possui várias funções para gerar números pseudo-aleatório. (pseudo pois pode haver repetição)

- em python módulo são apenas outros arquivos python.
- reutilização de código

Existem duas formas de se utilizar um módulo ou função deste:
"""
#forma 1 - Importando todo o módulo

import random

#ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem dentro do módulo
#ficarão disponíveis, logo, consumindo memória, não é recomendável.

#dir(random) no terminal

print(random.random())

#lembrar da diferença de função e pacote!!! função abre e fecha parenteses, random() é apenas uma das funções

#ao clicar segurando o ctrl é possível ver o código fonte
from random import uniform

for i in range(10):
    print(uniform(3, 7))
#randint faz a mesma coisa, porém com inteiros.

#Choice() valor aleatório entre um iterável

jogadas = ['pedra', 'papel', 'tesoura']

from random import choice

print(choice(jogadas))

#shuffle embaralha os dados

cartas = ['K', 'Q', 'J' , 'A',2,3,4,5,6,7,8,9]

print(cartas)
from random import shuffle

shuffle(cartas)
print(cartas)