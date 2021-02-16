"""
ao abrir modo leitura se pode apenas ler e vice versa.
ao abrir um arquivo para escrita o arquivo é criado
"""

with open('teste', 'w') as arquivo: #modo de abertura do arquivo 'w'
    arquivo.write('teste de dados novos no arquivo. \n')
    arquivo.write('quantas linhas quisermos. \n')


