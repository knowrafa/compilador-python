class Gramatica:
    gramatica = {
        1: {
            "key": "P\'",
            "regra": "P",
            "cardinalidade": 1,
        },
        2: {
            "key": "P",
            "regra": "inicio V A",
            "cardinalidade": 3,
        },
        3: {
            "key": "V",
            "regra": "varinicio LV",
            "cardinalidade": 2,
        },
        4: {
            "key": "LV",
            "regra": "D LV",
            "cardinalidade": 2,
        },
        5: {
            "key": "LV",
            "regra": "varfim;",
            "cardinalidade": 2,
        },
        6: {
            "key": "D",
            "regra": "TIPO L;",
            "cardinalidade": 3,
        },
        7: {
            "key": "L",
            "regra": "id, L",
            "cardinalidade": 3,
        },
        8: {
            "key": "L",
            "regra": "id",
            "cardinalidade": 1,
        },
        9: {
            "key": "TIPO",
            "regra": "int",
            "cardinalidade": 1,
        },
        10: {
            "key": "TIPO",
            "regra": "real",
            "cardinalidade": 1,
        },
        11: {
            "key": "TIPO",
            "regra": "lit",
            "cardinalidade": 1,
        },
        12: {
            "key": "A",
            "regra": "ES A",
            "cardinalidade": 2,
        },
        13: {
            "key": "ES",
            "regra": "leia id;",
            "cardinalidade": 3,
        },
        14: {
            "key": "ES",
            "regra": "escreva ARG;",
            "cardinalidade": 3,
        },
        15: {
            "key": "ARG",
            "regra": "literal",
            "cardinalidade": 1,
        },
        16: {
            "ARG": "num",
            "key": "ARG",
            "regra": "num",
            "cardinalidade": 1,
        },
        17: {
            "ARG": "id",
            "key": "ARG",
            "regra": "id",
            "cardinalidade": 1,
        },
        18: {
            "key": "A",
            "regra": "CMD A",
            "cardinalidade": 2,
        },
        19: {
            "key": "CMD",
            "regra": "id rcb LD;",
            "cardinalidade": 4,
        },
        20: {
            "key": "LD",
            "regra": "OPRD opm OPRD",
            "cardinalidade": 3,
        },
        21: {
            "key": "LD",
            "regra": "OPRD",
            "cardinalidade": 1,
        },
        22: {
            "key": "OPRD",
            "regra": "id",
            "cardinalidade": 1,
        },
        23: {
            "key": "OPRD",
            "regra": "num",
            "cardinalidade": 1,
        },
        24: {
            "key": "A",
            "regra": "COND A",
            "cardinalidade": 2,
        },
        25: {
            "key": "COND",
            "regra": "CAB CP",
            "cardinalidade": 2,
        },
        26: {
            "key": "CAB",
            "regra": "se (EXP_R) entao",
            "cardinalidade": 5,
        },
        27: {
            "key": "EXP_R",
            "regra": "OPRD opr OPRD",
            "cardinalidade": 3,
        },
        28: {
            "key": "CP",
            "regra": "ES CP",
            "cardinalidade": 2,
        },
        29: {
            "key": "CP",
            "regra": "CMD CP",
            "cardinalidade": 2,
        },
        30: {
            "key": "CP",
            "regra": "COND CP",
            "cardinalidade": 2,
        },
        31: {
            "key": "CP",
            "regra": "fimse",
            "cardinalidade": 1,
        },
        32: {
            "key": "A",
            "regra": "R A",
            "cardinalidade": 2,
        },
        33: {
            "key": "R",
            "regra": "facaAte (EXP_R) CP_R",
            "cardinalidade": 5,
        },
        34: {
            "key": "CP_R",
            "regra": "ES CP_R",
            "cardinalidade": 2,
        },
        35: {
            "key": "CP_R",
            "regra": "CMD CP_R",
            "cardinalidade": 2,
        },
        36: {
            "key": "CP_R",
            "regra": "COND CP_R",
            "cardinalidade": 2,
        },
        37: {
            "key": "CP_R",
            "regra": "fimFaca",
            "cardinalidade": 1,
        },
        38: {
            "key": "A",
            "regra": "fim",
            "cardinalidade": 1,
        },
    }
