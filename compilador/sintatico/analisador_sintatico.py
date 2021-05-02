from .Gramatica import Gramatica
from .pilha import Pilha
from .tabela_acao_desvio import TabelaAcaoDesvio


class AnalisadorSintatico:
    pilha = None
    tabela = None
    gramatica = None

    def __init__(self):
        self.pilha = Pilha()
        self.tabela = TabelaAcaoDesvio()
        self.gramatica = Gramatica()
