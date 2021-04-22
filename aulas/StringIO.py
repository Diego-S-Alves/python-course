"""
StringIO - ler e criar arquivos em memória

para ler ou escrever dados em arquivos do sistema operacional o software precisa de permissao

"""

from io import StringIO

mensagem = "string normal"

#podemos criar file já com uma string inserida, ou vazio para usar dps

arquivo = StringIO(mensagem)

#com o arquivo criado podemos utilizar funções de leitura/escrita de arquivos
