"""
cria um iteravel, zip objetc que agrega elementos de cada um dos iteraveis passados como entrada em pares
"""

lista1 = [1,2,3]
lista2 = [4,5,6]

zip1 = zip(lista1,lista2)

print(zip1)
print(type(zip1))

print(list(zip1))

#para tuplas, dicionarios ou set fica vazio, tem de reexecutar, quando o menor iteravel acaba o zip para

# *desempacotamento

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1],dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))