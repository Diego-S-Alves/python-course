"""
generators


generator object
ocupa menos recurso em memoria que o list,dict e set comprehension
utiliza o list quando PRECISAR da lista
"""
nomes = ['Carlos', 'Camila', 'Carla', 'Vanessa']
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

#import sys  getsizeof (mostra bytes de quando ocupa em memoria)

from sys import getsizeof

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dic_comp = getsizeof({x: x * 10 for x in range(1000)})
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

#iterando

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)