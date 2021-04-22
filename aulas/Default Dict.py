"""
Módulo Collection - Default Dict

Ao criar um dicionario nós informamos um valor default, podendo utilizar um lambda.
Será utilizado sempre que não houver um valor definido.
Caso tentar acessar uma chave que não existe, será criada e o valor default atribuído.
"""

from _collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programando em Python'

print(dicionario)

print(dicionario['outro'])

print(dicionario)
