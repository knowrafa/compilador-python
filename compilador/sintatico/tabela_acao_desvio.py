import csv


class TabelaAcaoDesvio:
    acao = ['l0']

    tabela_acao = []
    tabela_desvio = []

    def __init__(self):
        self.preencher_tabela_acao()

    def preencher_tabela_acao(self):
        with open('../tabela_acao.csv', 'r') as csvfile:
            read = csv.reader(csvfile)
            print('aq')
            tabela = []
            for row in read:
                tabela.append(row.copy())
        self.tabela_acao = tabela
