from .token import TOKEN


class Scanner:

    def __init__(self):
        self.tokens = {
            'Num': TOKEN(classe='Num', lexema='Num'),
            'Literal': TOKEN(classe='Literal', lexema='Literal'),
            'id': TOKEN(classe='id', lexema='id'),
            'Comentario': TOKEN(classe='Comentário', lexema='Comentário'),
            'EOF': TOKEN(classe='EOF', lexema='EOF'),
            'OPR': TOKEN(classe='OPR', lexema='OPR'),
            'RCB': TOKEN(classe='RCB', lexema='RCB'),
            'OPM': TOKEN(classe='OPM', lexema='AB_P'),
            'FC_P': TOKEN(classe='FC_P', lexema='PT_V'),
            'PT_V': TOKEN(classe='PT_V', lexema='PT_V'),
            'ERRO': TOKEN(classe='ERRO', lexema='ERRO')
        }

        self.tabela_de_transicoes = {
            'q0': {
                'final': True,
                'letra': 'q9',
                'letra_e': 'q9',
                'digito': 'q1',
                'abre_parentese': 'q19',
                'fecha_parentese': 'q20',
                'ponto_virgula': 'q21',
                'virgula': 'q22',
                'aspa': 'q7',
                'maior': 'q15',
                'igual': 'q14',
                'menor': 'q13',
                'abre_chaves': 'q10',
                'espaco': 'q0',
                'operador': 'q18',
                'EOF': 'q12',
            },
            'q1': {
                'final': False,
                'letra_e': 'q4',
                'digito': 'q1',
                'ponto': 'q2',
            },
            'q2': {
                'final': False,
                'digito': 'q3',
            },
            'q3': {
                'final': True,
                'digito': 'q3',
                'letra_e': 'q4',
            },
            'q4': {
                'final': False,
                'mais_ou_menos': 'q5',
                'digito': 'q6'
            },
            'q5': {
                'final': False,
                'digito': 'q6',
            },
            'q6': {
                'final': True,
                'digito': 'q6',
            },
            'q7': {
                'final': False,
                'ponto': 'q7',
                'aspas': 'q8',
            },
            'q8': {
                'final': True,
            },
            'q9': {
                'final': True,
                'letra': 'q9',
                'letra_e': 'q9',
                'digito': 'q9',
                'underline': 'q9'
            },
            'q10': {
                'final': False,
                'ponto': 'q10',
                'fecha_chave': 'q11',
            },
            'q11': {
                'final': True,
            },
            'q12': {
                'final': True,
            },
            'q13': {
                'final': True,
                'traco': 'q17',
                'maior': 'q16',
                'igual': 'q16'
            },
            'q14': {
                'final': True,
            },
            'q15': {
                'final': True,
                'igual': 'q16',
            },
            'q16': {
                'final': True,
            },
            'q17': {
                'final': True,
            },
            'q18': {
                'final': True,
            },
            'q19': {
                'final': True,
            },
            'q20': {
                'final': True,
            },
            'q21': {
                'final': True,
            },
            'q22': {
                'final': True,
            },
            'erro': {
                'final': True,
            },
        }

    def get_tokens(self):
        return self.tokens
