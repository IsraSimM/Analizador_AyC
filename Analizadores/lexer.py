import ply.lex as lex

# Definir todos los tokens que el lexer debe reconocer
tokens = [
    'NUMERO', 'SUMA', 'RESTA', 'MULTI', 'DIVIDE', 'LPAREN', 'RPAREN', 'IDENTIFICADOR', 
    'COMPARADOR', 'PUNTOYCOMA', 'IGUAL', 'LLLAVE', 'RLLAVE', 'FOR', 'TIPODATO', 'INCLUDE', 'COMA'
]

# Expresiones regulares para operadores y delimitadores
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PUNTOYCOMA = r';'
t_IGUAL = r'='
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_COMA = r','
t_COMPARADOR = r'==|!=|<=|>=|<|>'
t_ignore = ' \t\n'  # Ignorar espacios, tabulaciones y nuevas líneas

# Palabra reservada 'for'
def t_FOR(t):
    r'for'
    return t

# Tipos de datos
def t_TIPODATO(t):
    r'int|float|char|double'
    return t

# Directivas de preprocesador
def t_INCLUDE(t):
    r'\#include[ ]*<.*?>'
    return t

# Números enteros
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identificadores (variables)
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Manejo de errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()

if __name__ == "__main__": 
    data = input("Ingrese la expresión a analizar: ") 
    lexer.input(data) 
    print(f"Analizando: {data}") 
    for token in lexer: 
        print(token.type, token.value)
