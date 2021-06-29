print(' '*30)
print ("Sequência de Fibonacci ")
print(' '*30)
num =int(input("Quantos termos da Sequência de Fibonacci você deseja saber? "))
print(' '*30)
anterior = 0
proxima = 1
iteracao = 0
print('{},{}'.format(anterior, proxima), end='')
cont = 3
while cont<= num:
  iteracao = anterior + proxima
  print (',{}'.format(iteracao), end ='')
  anterior = proxima
  proxima = iteracao
  cont +=1
print(' '*30)
