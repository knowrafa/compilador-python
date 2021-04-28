from .pilha import Pilha
from .tabela_acao_desvio import TabelaAcaoDesvio


class AnalisadorSintatico:
    pilha = None
    tabela = None
    gramatica = {
        1: 3,
    }
    def __init__(self):
        self.pilha = Pilha()
        self.tabela = TabelaAcaoDesvio()
