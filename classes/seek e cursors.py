"""
seek() movimenta o cursor pelo arquivo
tem que usar o open novamente para atualizar o arquivo

"""

arquivo =open("zen_of_python")
print(arquivo.read())

arquivo.seek(0)
#seek() recebe um parametro que indica onde queremos colocar o cursor
#readline() lê linha a linha
arquivo.seek(0)
x = arquivo.readline()
print(x.split(' '))

#readlines -> quantidade de linhas
