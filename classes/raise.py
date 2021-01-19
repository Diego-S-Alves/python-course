"""
raise > lança exceções
Não é uma função e sim uma palavra reservada.
raise TipoDoErro('Mensagem de erro')

nada depois do raise é executado

"""
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}.')



colore('Diego', 'rosa')