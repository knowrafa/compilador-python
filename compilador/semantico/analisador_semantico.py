from compilador.lexico.estruturas import TOKEN
import copy


class AnalisadorSemantico:
    nome_arquivo = 'programa.c'
    pilha_semantica = []
    tabulacao_atual = 1
    temporaria_atual = 0

    variaveis = []
    linhas = []

    def analisador(self, numero_regra, regra, tokens_para_verificar, tabela_de_simbolos):
        temp_token = TOKEN(classe=regra, lexema=regra)
        if numero_regra == 5:
            tabs = ''
            for i in range(0, self.tabulacao_atual):
                tabs += '\t'
            for i in range(0, 3):
                self.linhas.append(tabs + '\n')

        elif numero_regra == 6:
            tipo = tokens_para_verificar.pop()
            token_id = tokens_para_verificar.pop()

            token_id.tipo = tipo.tipo
            self.preencher_linhas(token_id.tipo + " " + token_id.lexema.strip() + ";")
            temp_token = token_id
        elif numero_regra == 7:
            id1 = tokens_para_verificar.pop()

            temp_token = id1
        elif numero_regra == 8:
            id2 = tokens_para_verificar.pop()

            temp_token = id2
        elif numero_regra == 9:
            inteiro = tokens_para_verificar.pop()
            inteiro.tipo = 'int'
            temp_token = inteiro
        elif numero_regra == 10:
            real = tokens_para_verificar.pop()
            real.tipo = 'double'
            temp_token = real
        elif numero_regra == 11:
            literal = tokens_para_verificar.pop()
            literal.tipo = 'literal'
            temp_token = literal
        elif numero_regra == 13:
            tokens_para_verificar.pop()
            token_id = tokens_para_verificar.pop()

            if token_id.tipo == 'literal':
                self.preencher_linhas("scanf(\"%s\", " + token_id.lexema.strip() + ");")
            elif token_id.tipo == 'int':
                self.preencher_linhas("scanf(\"%d\", &" + token_id.lexema.strip() + ");")
            elif token_id.tipo == 'double':
                self.preencher_linhas("scanf(\"%lf\", &" + token_id.lexema.strip() + ");")
            else:
                temp_token = TOKEN(classe="ERRO", lexema="Erro: Variável não declarada!", tipo='erro')
        elif numero_regra == 14:
            tokens_para_verificar.pop()
            arg = tokens_para_verificar.pop()

            if arg.classe == 'Literal':
                self.preencher_linhas("printf(\"%s\", " + arg.lexema.strip() + ");")
            elif arg.classe == 'id':
                if arg.tipo == 'literal':
                    self.preencher_linhas("printf(\"%s\", " + arg.lexema.strip() + ");")
                elif arg.tipo == 'int':
                    self.preencher_linhas("printf(\"%d\", " + arg.lexema.strip() + ");")
                elif arg.tipo == 'double':
                    self.preencher_linhas("printf(\"%lf\", " + arg.lexema.strip() + ");")
                else:
                    temp_token = TOKEN(classe="ERRO", lexema="Erro: Variável não declarada!", tipo='erro')
        elif numero_regra in [15, 16, 17]:
            token_id = tokens_para_verificar.pop()
            if token_id.classe != 'id' or (token_id.classe == 'id' and token_id.tipo is not None):
                temp_token = copy.copy(token_id)
            else:
                temp_token = TOKEN(classe="ERRO", lexema="Erro: Variável não declarada!", tipo='erro')
        elif numero_regra == 19:
            token_id = tokens_para_verificar.pop()
            rcb = tokens_para_verificar.pop()
            ld = tokens_para_verificar.pop()

            if token_id.tipo is not None:
                if token_id.tipo == ld.tipo:
                    self.preencher_linhas(token_id.lexema.strip() + " = " + ld.lexema.strip() + ";")
                elif ld.classe == 'Num':
                    self.preencher_linhas(token_id.lexema.strip() + " = " + ld.lexema.strip() + ";")
                else:
                    temp_token = TOKEN(classe="ERRO", lexema="Erro: Tipos diferentes para atribuição!", tipo='erro')
            else:
                temp_token = TOKEN(classe="ERRO", lexema="Erro: Variável não declarada!", tipo='erro')
        elif numero_regra == 20:
            oprd1 = tokens_para_verificar.pop()
            opm = tokens_para_verificar.pop()
            oprd2 = tokens_para_verificar.pop()

            self.preencher_variaveis("int T" + str(self.temporaria_atual) + ";")

            tipo1 = oprd1.tipo
            tipo2 = oprd2.tipo

            if 'literal' not in [tipo1, tipo2] or 'Num' in [oprd1.classe, oprd2.classe]:
                temp_token.lexema = "T" + str(self.temporaria_atual)

                if tipo1 == tipo2:
                    temp_token.tipo = tipo1
                elif 'Num' in [oprd1.classe, oprd2.classe]:
                    temp_token.tipo = 'int'
                else:
                    temp_token.tipo = 'double'

                self.preencher_linhas(
                    "T" + str(
                        self.temporaria_atual) + " = " + oprd1.lexema.strip() + " " + opm.lexema.strip() + " " + oprd2.lexema.strip() + ";")

            elif None in [tipo1, tipo2]:
                temp_token = TOKEN(classe="ERRO", lexema="Erro: Variável não declarada!", tipo='erro')
            elif 'literal' not in [tipo1, tipo2]:
                temp_token = TOKEN(classe="ERRO", lexema="Erro: Operandos com tipos incompatíveis!", tipo='erro')

            self.temporaria_atual += 1

        elif numero_regra == 21:
            oprd = tokens_para_verificar.pop()
            temp_token = copy.copy(oprd)
        elif numero_regra == 22:
            token_id = tokens_para_verificar.pop()
            if token_id.classe != 'id' or (token_id.classe == 'id' and token_id.tipo is not None):
                temp_token = copy.copy(token_id)
            else:
                temp_token = TOKEN(classe="ERRO", lexema="Erro: Variável não declarada!", tipo='erro')
        elif numero_regra == 23:
            num = tokens_para_verificar.pop()
            temp_token = copy.copy(num)
        elif numero_regra == 25:
            self.tabulacao_atual -= 1
            self.preencher_linhas("}")
        elif numero_regra == 26:
            tokens_para_verificar.pop()
            tokens_para_verificar.pop()
            exp_r = tokens_para_verificar.pop()
            self.preencher_linhas("if (" + exp_r.lexema + "){")
            self.tabulacao_atual += 1

        elif numero_regra == 27:
            oprd1 = tokens_para_verificar.pop()
            opr = tokens_para_verificar.pop()
            oprd2 = tokens_para_verificar.pop()

            self.preencher_variaveis("int T" + str(self.temporaria_atual) + ";")

            tipo1 = oprd1.tipo
            tipo2 = oprd2.tipo

            if tipo1 == tipo2 or (tipo1 == 'double' and tipo2 == 'int') or (
                    tipo2 == 'int' and tipo2 == 'double') or 'Num' in [oprd1.classe, oprd2.classe]:

                temp_token.lexema = "T" + str(self.temporaria_atual)

                if tipo1 == tipo2:
                    temp_token.tipo = tipo1
                else:
                    temp_token.tipo = 'double'

                self.preencher_linhas(
                    "T" + str(
                        self.temporaria_atual) + " = " + oprd1.lexema.strip() + " " + opr.lexema.strip() + " " + oprd2.lexema.strip() + ";")

            else:
                temp_token = TOKEN(classe="ERRO", lexema="Erro: Operandos com tipos incompatíveis!", tipo='erro')

            self.temporaria_atual += 1
        elif numero_regra == 32:
            pass
        elif numero_regra == 33:
            tokens_para_verificar.pop()
            tokens_para_verificar.pop()
            expr_r = tokens_para_verificar.pop()
            self.preencher_linhas("while(" + expr_r.lexema + ") {")
            self.tabulacao_atual += 1
        elif numero_regra in [34, 35, 36]:
            es = tokens_para_verificar.pop()
            cp_r = tokens_para_verificar.pop()
            temp_token = copy.copy(cp_r)
        elif numero_regra == 37:
            cp_r = tokens_para_verificar.pop()
            temp_token.lexema = cp_r.lexema

            self.preencher_linhas("}")
            self.tabulacao_atual -= 1
        elif 38:
            tokens_para_verificar.pop()
            temp_token.lexema = 'fim'

        return temp_token

    def preencher_cabecalho(self):
        with open(self.nome_arquivo, 'w') as arquivo:
            arquivo.write('#include<stdio.h>\n\n')
            arquivo.write('typedef char literal[256];\n\n')
            arquivo.write("int main(void){\n\n")

    def preencher_variaveis(self, variavel):
        tabs = ''
        for i in range(0, self.tabulacao_atual):
            tabs += '\t'

        self.variaveis.append(tabs + variavel + '\n')

    def preencher_linhas(self, linha):
        tabs = ''
        for i in range(0, self.tabulacao_atual):
            tabs += '\t'

        self.linhas.append(tabs + linha + " \n")

    def terminar_arquivo(self):
        with open(self.nome_arquivo, 'a') as arquivo:
            for i in range(0, len(self.variaveis)):
                arquivo.write(self.variaveis[i])
            for i in range(0, len(self.linhas)):
                arquivo.write(self.linhas[i])
            arquivo.write('\n\treturn 0;\n')
            arquivo.write('}')
