"""
teste de tempo de processamento

ex:
"""
import time

gen_inicio = time.time()

ge2 = (num for num in range(100000000))
print(ge2)
#generator tem maior ganho em tempo de execuçao comparado com o list comprehension, fora a diferença em memoria

