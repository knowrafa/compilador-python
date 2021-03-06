import logging
from termcolor import colored
import coloredlogs
from tabulate import tabulate

from compilador.sintatico.pilha import Pilha
from lexico import AnalisadorLexico
from sintatico import AnalisadorSintatico
from semantico import AnalisadorSemantico

analisador_lexico = AnalisadorLexico()
analisador_sintatico = AnalisadorSintatico()
analisador_semantico = AnalisadorSemantico()

# arquivo = open('entrada.txt', 'rb')
i = 0
tokens = []
'''
for linha in arquivo:
    i += 1
    try:
        index = 0
        while index < len(linha):
            token, index = analisador_lexico.scanner(linha, index)
            tokens.append(token)
    except NameError():
        # print("ERRO na linha " + i)
        pass
'''
linha = ""
arquivo = open('fonte.mygol', 'r')
tokens = []
nr_linha = 0
erro = []
logger = logging.getLogger(__name__)
# coloredlogs.install(level='DEBUG', logger=logger)

analisador_semantico.preencher_cabecalho()

for linha in arquivo:
    nr_linha += 1
    index = 0
    leitura = False
    escrita = False
    condicional = False
    expressao_atual = []
    while index < len(linha):
        comeco = index
        token, index, mensagem = analisador_lexico.scanner(palavra=linha, index=index)

        # if celula == ('s')

        final = index

        if token.classe.find('ERRO') != -1:
            print(colored("%s: %s, linha %s, coluna %s " % (token.classe, mensagem, nr_linha, final), 'red',
                          attrs=['bold']))
            continue

        while True:
            if token.classe == '\s':
                break
            if erro:
                if token.classe in erro:
                    erro = []
                else:
                    break
            coluna = analisador_sintatico.tabela.tabela_acao[0].index(token.classe)
            topo_pilha = analisador_sintatico.pilha.pilha[-1]
            celula = analisador_sintatico.tabela.tabela_acao[topo_pilha + 1][coluna]
            if not celula:
                erro = []
                for col in range(0, len(analisador_sintatico.tabela.tabela_acao[topo_pilha + 1])):
                    if analisador_sintatico.tabela.tabela_acao[topo_pilha + 1][col]:
                        nome_linha = "%s: (%s-%s)" % (nr_linha, comeco, final)
                        print(colored("Esperava %s, linha %s, coluna %s " % (
                            analisador_sintatico.tabela.tabela_acao[0][col], nr_linha - 1, final), 'red',
                                      attrs=['bold']))
                        erro.append(analisador_sintatico.tabela.tabela_acao[0][col])
                break
            elif celula[0] == 's':
                # Se a c??lula tiver shift no come??o da palavra
                analisador_sintatico.pilha.empilha(int(celula[1:]))

                analisador_semantico.pilha_semantica.append(token)

                break

            elif celula[0] == 'r':
                # Se a c??lula tiver reduce no come??o da palavra
                numero = int(celula[1:]) + 1
                regra = analisador_sintatico.gramatica.gramatica[numero]
                # print(f"pilha: {analisador_sintatico.pilha.pilha}")
                # print(f"Desempilhando {regra.get('cardinalidade')} estado(s)")

                tokens_para_verificar = []

                for i in range(0, regra.get('cardinalidade')):
                    analisador_sintatico.pilha.desempilha()
                    token_desempilhado = analisador_semantico.pilha_semantica.pop()
                    tokens_para_verificar.append(token_desempilhado)

                topo = analisador_sintatico.pilha.topo()
                coluna = analisador_sintatico.tabela.tabela_goto[0].index(regra.get('key'))
                celula = analisador_sintatico.tabela.tabela_goto[topo + 1][coluna]

                print(str(numero) + ' - ' + regra.get('key') + ' -> ' + regra.get('regra'))

                nao_terminal = analisador_semantico.analisador(numero, regra.get('key'), tokens_para_verificar,
                                                               analisador_lexico.tabela_de_simbolos)

                analisador_sintatico.pilha.empilha(int(celula))
                if nao_terminal.classe != 'ERRO':
                    analisador_semantico.pilha_semantica.append(nao_terminal)
                else:
                    print(colored("Erro sem??ntico: %s, linha %s, coluna %s " % (token.lexema, nr_linha, final), 'red',
                                  attrs=['bold']))

        nome_linha = "%s: (%s-%s)" % (nr_linha, comeco, final)
        print('-----------------------------------------------------------------------')

        print(
            colored("Linha: %s => Classe: %s, Lexema: \"%s\", Tipo: %s" % (
                nome_linha, token.classe, '\\n' if token.lexema == '\n' else token.lexema.strip(), token.tipo),
                    'green'))

while True:
    coluna = analisador_sintatico.tabela.tabela_acao[0].index('$')
    topo_pilha = analisador_sintatico.pilha.pilha[-1]
    celula = analisador_sintatico.tabela.tabela_acao[topo_pilha + 1][coluna]
    if celula == 'acc':
        regra = analisador_sintatico.gramatica.gramatica[topo_pilha]
        print(str(topo_pilha) + ' - ' + regra.get('key') + ' -> ' + regra.get('regra'))
        break
    elif not celula:
        break
    elif celula[0] == 'e':
        mensagem = analisador_sintatico.tabela.obter_erro(int(celula[1:]))
        final = index
        nome_linha = "%s: (%s-%s)" % (nr_linha, comeco, final)
        print(colored("%s, linha %s, coluna %s " % (mensagem, nr_linha, final), 'red',
                      attrs=['bold']))

        break
    elif celula[0] == 'r':
        # Se a c??lula tiver reduce no come??o da palavra
        numero = int(celula[1:]) + 1
        regra = analisador_sintatico.gramatica.gramatica[numero]
        # print(f"pilha: {analisador_sintatico.pilha.pilha}")
        # print(f"Desempilhando {regra.get('cardinalidade')} estado(s)")

        for i in range(0, regra.get('cardinalidade')):
            analisador_sintatico.pilha.desempilha()

        topo = analisador_sintatico.pilha.topo()
        coluna = analisador_sintatico.tabela.tabela_goto[0].index(regra.get('key'))
        celula = analisador_sintatico.tabela.tabela_goto[topo + 1][coluna]
        # print(f"pilha: {analisador_sintatico.pilha.pilha}")
        analisador_sintatico.pilha.empilha(int(celula))
        # print(f"pilha: {analisador_sintatico.pilha.pilha}")

        print(str(numero) + ' - ' + regra.get('key') + ' -> ' + regra.get('regra'))

token, index, _ = analisador_lexico.scanner(eof=True)
print('-----------------------------------------------------------------------')
print(
    colored("Linha: %s => Classe: %s, Lexema: %s, Tipo: %s" % (
        nr_linha + 1, token.classe, token.lexema.strip(), token.tipo
    ), 'yellow', 'on_grey',
            )
)
arquivo.close()

analisador_semantico.terminar_arquivo()
