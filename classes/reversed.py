"""
diferente do reverse de listas

reverse = funçao apenas de listas, reverte os valores
reversed

, como a sorted inverte qualquer iterável

class 'list_reverseiterator'
também podemos converter o objeto retornado  em lista tupla ou conjunto

set nao inverte, poisnao guarda a ordem
podemos iterar sobre o reversed, ex:


"""

for letra in reversed('Geek University'):
    print(letra, end='')

print(''.join(list(reversed('Geek University'))))

#slice de strings:
print('el diegon'[::-1])