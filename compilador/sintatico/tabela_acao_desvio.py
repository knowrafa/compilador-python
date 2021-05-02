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
