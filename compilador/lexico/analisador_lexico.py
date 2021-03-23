from .estruturas import Scanner, TabelaDeSimbolos


class AnalisadorLexico:

    def __init__(self):
        self.tabela_de_simbolos = TabelaDeSimbolos()

    def executar_analisador(self):
        pass

    @staticmethod
    def get_chave(caractere, eof=False):

        chave = None
        if eof is True:
            chave = 'EOF'
        elif caractere.isalpha():
            chave = 'letra'
            if caractere == 'E' or caractere == 'e':
                chave = 'letra_e'
        elif caractere.isdigit():
            chave = 'digito'
        elif caractere == '(':
            chave = 'abre_parentese'
        elif caractere == ')':
            chave = 'fecha_parentese'
        elif caractere == ';':
            chave = 'ponto_virgula'
        elif caractere == ',':
            chave = 'virgula'
        elif caractere == '\"':
            chave = 'aspa'
        elif caractere in ['+', '-', '/', '*']:
            if caractere == '+':
                chave = 'mais'
            elif caractere == '-':
                chave = 'menos'
            elif caractere == '/':
                chave = 'divisao'
            elif caractere == '*':
                chave = 'multiplicacao'
        elif caractere in ['<', '>', '=']:
            if caractere == '<':
                chave = 'menor'
            elif caractere == '>':
                chave = 'maior'
            elif caractere == '=':
                chave = 'igual'
        elif caractere in ['.', '_', '{', '}']:
            if caractere == '.':
                chave = 'ponto'
            elif caractere == '_':
                chave = 'underline'
            elif caractere == '{':
                chave = 'abre_chave'
            elif caractere == '}':
                chave = 'fecha_chave'
        elif caractere.isspace() or caractere=='\s' or not caractere.isprintable():
            chave = 'espaco'
        else:
            chave = 'erro'

        return chave

    def scanner(self, palavra, index=0, eof=False):
        estado_inicial = 'q0'
        estado_atual = estado_inicial
        scanner = Scanner()
        # Procedimento para identificar qual o TOKEN
        token = None
        primeiro_caractere = index
        ultimo_caractere = index

        # palavra = "AWEIUQ=WBEIQWOWE123123OIH12ZHQIEGU212"

        tamanho = len(palavra)
        for posicao in range(index, tamanho):
            caractere = palavra[posicao]
            chave = self.get_chave(caractere, eof=eof)
            if chave == 'erro':
                lexema = palavra[primeiro_caractere:ultimo_caractere+1]
                token = scanner.tokens.get('ERRO')
                token.lexema = lexema
                return token, ultimo_caractere

            # Se retornar algo diferente de False, então existe a transição
            proximo_estado = scanner.tabela_de_transicoes[estado_atual].get(chave, False)

            def verificando_token():
                if scanner.tabela_de_transicoes[estado_atual].get('final'):
                    tipo_token = scanner.classificacao_estados_finais.get(estado_atual)
                    lexema = palavra[primeiro_caractere:ultimo_caractere]
                    if tipo_token == 'id':
                        token = self.tabela_de_simbolos.token_exists(identificador=lexema)
                        if not token:
                            token = scanner.tokens.get(tipo_token)
                            token.lexema = lexema
                            self.tabela_de_simbolos.insercao(token)
                    else:
                        token = scanner.tokens.get(tipo_token)
                        token.lexema = lexema
                    return token, ultimo_caractere

            if proximo_estado:
                estado_atual = proximo_estado
                ultimo_caractere += 1
                if ultimo_caractere == len(palavra):
                    return verificando_token()

            else:
                return verificando_token()
