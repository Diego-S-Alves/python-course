"""
para ler o conteudo usamos a funçao integrada open()

apenas um parametro de entrada(caminho do arquivo) na forma mais simples,
retorna um _io.TextIOWraper e é com ele que trabalhamos. Há varios parametros opcionais.
open abre somente para leitura

read() - > ler o conteudo do arquivo
"""
arquivo = open('forms_script_template')

print(arquivo)

print(type(arquivo))

print(arquivo.read())