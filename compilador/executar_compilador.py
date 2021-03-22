from lexico import AnalisadorLexico

analisador = AnalisadorLexico()
analisador.executar_analisador()

# arquivo = open('entrada.txt', 'rb')
arquivo = ""
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
while linha != 'quit':
    linha = input("-> ")
    try:
        index = 0
        while index < len(linha):
            token, index = analisador.scanner(palavra=linha, index=index)
            print(token)
    except Exception as e:
        repr(e)
        pass

print(tokens)
