class Agenda:

    def __init__(self):

        self.base = {}

    def inserir(self, posicao, nome, idade, altura):

        self.posicao = posicao

        self.nome = nome

        self.idade = idade

        self.altura = altura

        if 'nomes' not in self.base:

            self.base['nomes'] = {'posicao': posicao, 'nome': nome, 'idade': idade, 'altura': altura}

        else:

            self.base['nomes'].update({'posicao': posicao, 'nome': nome, 'idade': idade, 'altura': altura})

    def listar(self):

        for posicao, nome, idade, altura in self.base['nomes'].items():
            print(posicao, nome, idade, altura)

    def apagar(self, nome):

        del self.base['nomes'][nome]


nome01 = Agenda()

nome01.inserir('01', 'Jamesson', 40, 1.78)

nome01.inserir('02', 'João', 40, 1.80)

nome01.listar()
