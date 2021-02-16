"""
ao abrir modo leitura se pode apenas ler e vice versa.

"""

with open('zen_of_python', 'w') as arquivo: #modo de abertura do arquivo 'w'
    arquivo.write('teste de dados novos no arquivo. \n')
    arquivo.write('quantas linhas quisermos. \n')
