"""
iterator -> um objeto que pode ser iterado.
objeto que retorna um dado sendo um elemento por   quando uma funçao next() é chamada.



iterable ->
-um objeto que irá retornar um iterator quando a funçao iter() for chamada
listas- variaveis, dicionarios, tuplas
"""

nome = 'Geek'

it1 = iter(nome)

print(next(it1))
