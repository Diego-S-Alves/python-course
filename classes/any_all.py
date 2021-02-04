vetor_1 = []
vetor_2 = []

vetor_intersccao = []

for numero in range(10):
    vetor_1.append(int(input(f"Informe os numeros para o vetor 1 :  {numero} /10  : ")))
    vetor_2.append(int(input(f"Informe os numeros para o vetor 2 :  {numero} /10   : ")))

print(vetor_1)
print(vetor_2)

vetor_intersccao = list(set(vetor_1).intersection(vetor_2))
print(f"numeros intersecção dos vetores 1 e 2 {vetor_intersccao}")