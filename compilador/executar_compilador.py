import logging
from termcolor import colored
import coloredlogs
from tabulate import tabulate

from lexico import AnalisadorLexico

analisador = AnalisadorLexico()
analisador.executar_analisador()

# arquivo = open('entrada.txt', 'rb')
i = 0
tokens = []
'''
for linha in arquivo:
    i += 1
    try:
        index = 0
        while index < len(linha):
            token, index = analisador.scanner(linha, index)
            tokens.append(token)
    except NameError():
        # print("ERRO na linha " + i)
        pass
'''
linha = ""
arquivo = open('erro.mygol', 'r')
tokens = []
nr_linha = 0

logger = logging.getLogger(__name__)
# coloredlogs.install(level='DEBUG', logger=logger)
for linha in arquivo:
    nr_linha += 1
    index = 0

    while index < len(linha):
        comeco = index
        token, index, mensagem = analisador.scanner(palavra=linha, index=index)
        final = index
        nome_linha = "%s: (%s-%s)" % (nr_linha, comeco, final)
        print('-----------------------------------------------------------------------')

        print(
            colored("Linha: %s => Classe: %s, Lexema: \"%s\", Tipo: %s" % (
                nome_linha, token.classe, '\\n' if token.lexema == '\n' else token.lexema.strip(), token.tipo), 'green'))
        if token.classe.find('ERRO') != -1:
            print(colored("%s: %s, linha %s, coluna %s " % (token.classe, mensagem, nr_linha, final), 'red',
                          attrs=['bold']))

            # Pular para a pŕoxima linha caso ache erro
            # Se não tiver o break, ele procura erros na linha toda
            break

token, index = analisador.scanner(eof=True)
print('-----------------------------------------------------------------------')
print(
    colored("Linha: %s => Classe: %s, Lexema: %s, Tipo: %s" % (
        nr_linha + 1, token.classe, token.lexema.strip(), token.tipo
    ), 'yellow', 'on_grey',
            )
)
arquivo.close()
# print(tokens)
