"""
São tuplas diferenciadas onde especificamos um nome e também parametros
"""

from collections import namedtuple

#precisamos definir o nome e parametros

#forma 1

cachorro = namedtuple('cachorro', 'idade raca nome')

#forma 2

cachorro = namedtuple('cachorro', 'idade, raca, nome')

#forma 3(preferível)

cachorro = namedtuple('cachorro', ['idade', 'raca','nome'])

#usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)
