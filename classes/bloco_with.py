"""
contexto de trabalho onde os recursos utilizados são fechado após o bloco

"""

with open('zen_of_python') as arquivo:
    print(arquivo.readlines())

#forma pythonica de manipular arquivos
#não precisa mais fechar o arquivo
