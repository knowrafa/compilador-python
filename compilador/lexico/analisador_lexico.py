from estruturas import TabelaDeSimbolos
import logging


class AnalisadorLexico:

    def __init__(self):
        self.tabela_de_simbolos = TabelaDeSimbolos()

    def executar_analisador(self):
        print(self.tabela_de_simbolos.get_palavras_reservadas())
        print(self.tabela_de_simbolos.get_token_ids())

    def scanner(self):
        return


analisador = AnalisadorLexico()
analisador.executar_analisador()
