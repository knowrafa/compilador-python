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

        self.__token_ids = {}

    def insercao(self, token):
        self.__token_ids['identificador'] = token

    def token_exists(self, identificador):
        if self.__token_ids.get(identificador):
            return self.__token_ids['identificador']
        return False

    def atualizacao(self):
        pass

    def get_palavras_reservadas(self):
        return self.__palavras_reservadas

    def get_token_ids(self):
        return self.__token_ids
