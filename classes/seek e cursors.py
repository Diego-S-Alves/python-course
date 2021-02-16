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
"""
streaming é o nome da conexão que fica entre o arquivo e pc usando o open(), deve-se encerrar usando o close() quando se terminar de usar
1 - usar arquivo
2 - trabalhar arquivo
3 - fechar arquivo
"""
arquivo.close()

print(arquivo.closed) #true se o arquivo estiver fechado