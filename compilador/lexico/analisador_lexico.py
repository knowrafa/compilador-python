from estruturas import TabelaDeSimbolos
from estruturas import TOKEN


class AnalisadorLexico:

    def __init__(self):
        self.tabela_de_simbolos = TabelaDeSimbolos()

    def executar_analisador(self):
        print(self.tabela_de_simbolos.get_palavras_reservadas())
        print(self.tabela_de_simbolos.get_token_ids())

    def scanner(self, palavra):
        # Procedimento para identificar qual o TOKEN
        token = None

        if token == 'id':
            return self.tabela_de_simbolos.insercao(identificador=palavra)

        return TOKEN(classe=token, lexema=palavra)


analisador = AnalisadorLexico()
analisador.executar_analisador()


arquivo = open('entrada.txt', 'rb')
for linha in arquivo:
    for simbolo in linha:
        print(simbolo)
