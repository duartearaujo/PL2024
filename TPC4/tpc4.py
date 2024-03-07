import sys
import re
import ply.lex as ply

instrucoes = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE'
}

tokens = [
    'INSTRUCAO',
    'ATRIBUTO',
    'VIRGULA',
    'OPERADOR',
    'NUMERO'
] + list(instrucoes.values())

def t_INSTRUCAO(t):
    r'\b[A-Za-z]+\b' 
    t.value = t.value.lower()
    t.type = instrucoes.get(t.value, 'ATRIBUTO')
    return t

def t_VIRGULA(t):
    r','
    return t

def t_OPERADOR(t):
    r'[=<>]+'
    return t

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Caracter ilegal: ", t.value[0])
    t.lexer.skip(1)

def main():
    lexer = ply.lex()
    for linha in sys.stdin:
        lexer.input(linha)
        for tok in lexer:
            print(tok)

if __name__ == "__main__":
    main()