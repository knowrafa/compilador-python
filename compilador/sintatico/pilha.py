class Pilha:
    pilha = [0]

    def empilha(self, estado):
        self.pilha.append(estado)

    def desempilha(self):
        self.pilha.pop()

    def topo(self):
        return self.pilha[-1]