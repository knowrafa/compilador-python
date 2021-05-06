import csv


class TabelaAcaoDesvio:
    acao = ['l0']

    tabela_acao = []
    tabela_goto = []

    def __init__(self):
        self.preencher_tabela_acao()
        self.preencher_tabela_goto()

    def preencher_tabela_acao(self):
        with open('../tabela_acao.csv', 'r') as csvfile:
            read = csv.reader(csvfile)
            tabela = []
            for row in read:
                tabela.append(row.copy())
        self.tabela_acao = tabela

    def preencher_tabela_goto(self):
        with open('../tabela_goto.csv', 'r') as csvfile:
            read = csv.reader(csvfile)
            tabela = []
            for row in read:
                tabela.append(row.copy())
        self.tabela_goto = tabela

    def obter_erro(self, num):
        if num in [0, 1]:
            return "Esperava palavra-reservada inicio!"
        elif num == 2:
            return "Esperava palavra reservada varinicio!"
        elif num == 3:
            return "Não inicializou corretamente ou esperava um fechamento com fim," \
                   " uma leitura/impressao de variavel, um id, uma condicional ou uma estrutura de repeticao!"
        elif num == 4:
            return "Esperava encerrar uma declaracao de variavel ou um id"
        elif num == [5, 6, 7, 8]:
            return "Esperava um fechamento com fim, uma leitura/impressao de variavel," \
                   " um id, uma condicional ou uma estrutura de repeticao!"
        elif num == 9:
            return "Esperava id"
        elif num == 10:
            return "Esperava definicao de argumento: literal, num ou id"
        elif num == 11:
            return "Esperava operador de atribuicao"
        elif num == 12:
            return "Esperava finalizar condicional, leitura/escrita de variavel, id ou incializar condicional"
        elif num in [13, 14]:
            return "Esperava abre parenteses ("
        elif num == 15:
            return "Esperava fechamento de declaracao de variavel ou id"
        elif num == 16:
            return "Esperava ;"
        elif num == 17:
            return "Esperava definicao de tipo de variavel: int, real ou lit"
        elif num in [18, 19]:
            return "Esperava ;"
        elif num == 20:
            return "Esperava id ou num"
        elif num in [21, 22, 23]:
            return "Esperava finalizar condicional, leitura/escrita de variavel, id ou inicializar condicional"
        elif num in [24, 25]:
            return "Esperava corpo de condicional, id ou num"
        elif num == 26:
            return "Esperava ;"
        elif num == 27:
            return "Esperava id"
        elif num == 28:
            return "Esperava ;"
        elif num == 29:
            return "Esperava fecha parenteses )"
        elif num == 30:
            return "Esperava operador relacional (<, >, <>, <=, 'a= =, >=)"
        elif num == 31:
            return "Esperava fecha parenteses )"
        elif num == 32:
            return "Esperava id ou num"
        elif num == 33:
            return "Esperava fechamento de repeticao, leitura/escrita de variavel, ide ou inicializacao de condicional"
        elif num == 34:
            return "Esperava id ou num"
        elif num == 35:
            return "Esperava palavra-reservada entao"
        elif num in [36, 37, 38]:
            return "Esperava fechamento de repeticao, leitura/escrita de variavel, id ou inicializacao de condicional"
