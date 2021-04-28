from .token import TOKEN


class TabelaDeSimbolos:

    # Palavras reservadas da linguagem
    # __palavras_reservadas = []

    # Lista de TOKEN, se for da classe ID
    # __token_ids = []

    def __init__(self):
        # São as palavras reservadas do sistema
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

        # É o conjunto de tokens do tipo ID lidas no programa fonte
        self.__token_ids = {
            'inicio': TOKEN(classe='inicio', lexema='inicio'),
            'varinicio': TOKEN(classe='varinicio', lexema='varinicio'),
            'varfim': TOKEN(classe='varfim', lexema='varfim'),
            'escreva': TOKEN(classe='escreva', lexema='escreva'),
            'leia': TOKEN(classe='leia', lexema='leia'),
            'se': TOKEN(classe='se', lexema='se'),
            'entao': TOKEN(classe='entao', lexema='entao'),
            'fimse': TOKEN(classe='fimse', lexema='fimse'),
            'facaate': TOKEN(classe='facaAte', lexema='facaAte'),
            'fimfaca': TOKEN(classe='fimfaca', lexema='fimfaca'),
            'fim': TOKEN(classe='fim', lexema='fim'),
            'inteiro': TOKEN(classe='inteiro', lexema='inteiro'),
            'lit': TOKEN(classe='lit', lexema='lit'),
            'real': TOKEN(classe='real', lexema='real')
        }

    def insercao(self, token):
        # Insere o token ID no dicionário de IDS, usando como chave seu lexema
        self.__token_ids[token.lexema] = token

    def token_id_exists(self, identificador):
        return self.__token_ids.get(identificador, False)

    def get_palavras_reservadas(self):
        return self.__palavras_reservadas

    def get_token_ids(self):
        return self.__token_ids
