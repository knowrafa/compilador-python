class TOKEN:
    # Classificação do lexema (Aritimético, ID, atribuição...)
    classe = None

    # Armazenará a palavra computada ( ';', '(', '=', ...)
    lexema = None

    # Definir se é inteiro, char...
    tipo = None

    def __init__(self, classe, lexema, tipo=None):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

    def __repr__(self):
        return self.classe + " | " + self.lexema


