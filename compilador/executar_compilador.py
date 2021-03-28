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

for linha in arquivo:
    nr_linha += 1
    index = 0

    while index < len(linha):
        comeco = index
        token, index = analisador.scanner(palavra=linha, index=index)
        final = index
        nome_linha = "%s: %s-%s ( %s)" % (nr_linha, comeco, final, linha.strip())

        if token.classe != 'ERRO':
            print(tabulate([[str(nome_linha), *token.tabular_objeto()]],
                           ['Linha', 'Classe', 'Lexema', 'Tipo'],
                           tablefmt="grid"))

        else:
            print(tabulate([[str(nome_linha), *token.tabular_objeto()]],
                           ['Linha', 'Classe', 'Lexema', 'Tipo'],
                           tablefmt="grid"))
            print("ERRO: Caractere inválido na linguagem, linha %s, coluna %s" % (nr_linha, final))

            # Pular para a pŕoxima linha caso ache erro
            # Se não tiver o break, ele procura erros na linha toda
            break


token, index = analisador.scanner(eof=True)
print(tabulate([['eof', *token.tabular_objeto()]], ['Linha', 'Classe', 'Lexema', 'Tipo'], tablefmt="grid"))
arquivo.close()
# print(tokens)
