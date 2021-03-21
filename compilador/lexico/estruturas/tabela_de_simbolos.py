from .token import TOKEN


class TabelaDeSimbolos:

    # Palavras reservadas da linguagem
    # __palavras_reservadas = []

    # Lista de TOKEN, se for da classe ID
    # __token_ids = []

    def __init__(self):
        self.__palavras_reservadas = [
            'inicio',
            'varinicio',
            'varfim',
            'escreva',
            'leia',
            'se',
            'entao',
            'fimse',
            'faca-ate',
            'fimfaca',
            'fim',
            'inteiro',
            'lit',
            'real'
        ]

        self.__token_ids = [
            TOKEN(classe='Num', lexema='Num'),
            TOKEN(classe='Literal', lexema='Literal'),
            TOKEN(classe='id', lexema='id'),
            TOKEN(classe='Comentário', lexema='Comentário'),
            TOKEN(classe='EOF', lexema='EOF'),
            TOKEN(classe='OPR', lexema='OPR'),
            TOKEN(classe='RCB', lexema='RCB'),
            TOKEN(classe='OPM', lexema='AB_P'),
            TOKEN(classe='FC_P', lexema='PT_V'),
            TOKEN(classe='PT_V', lexema='PT_V'),
            TOKEN(classe='ERRO', lexema='ERRO')
        ]

    def insercao(self):
        pass

    def atualizacao(self):
        pass

    def get_palavras_reservadas(self):
        return self.__palavras_reservadas

    def get_token_ids(self):
        return self.__token_ids
