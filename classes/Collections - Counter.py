"""
Collections -: High performance container Datetypes

Counter - Recebe um iterável como parametro e cria um objeto Collections Counter que é parecido com um dicionário.
como chave o elemento da lista e como valor a quantidade de ocorrencias deste elemento.
"""
from collections import Counter

lista = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6]
#Qualquer iterável funciona

res = Counter(lista)

print(type(res))

print(res)

#most_common()