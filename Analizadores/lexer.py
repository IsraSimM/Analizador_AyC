import ply.lex as lex

# Definir todos los tokens que el lexer debe reconocer
tokens = [
    'NUMERO', 'SUMA', 'RESTA', 'MULTI', 'DIVIDE', 'LPAREN', 'RPAREN', 'IDENTIFICADOR', 
    'COMPARADOR', 'PUNTOYCOMA', 'IGUAL', 'LLLAVE', 'RLLAVE', 'FOR', 'IF', 'ELSE', 'TIPODATO', 
    'INCLUDE', 'PRINTF', 'SCANF', 'CADENA', 'CHAR', 'FLOAT', 'COMA', 'CORCHETEIZQ', 'CORCHETEDER', 'PUNTO',
    'CARACTER', 'AMPERSAND'
]

# Expresiones regulares para operadores y delimitadores
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r'\]'
t_PUNTOYCOMA = r';'
t_COMPARADOR = r'==|!=|<=|>=|<|>'
t_IGUAL = r'='
t_AMPERSAND = r'&'
t_COMA = r','
t_PUNTO = r'\.'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_ignore = ' \t\n'  # Ignorar espacios, tabulaciones y nuevas líneas

# Palabra reservada 'for'
def t_FOR(t):
    r'for'
    return t

# Palabra reservada 'if'
def t_IF(t):
    r'if'
    return t

# Palabra reservada 'else'
def t_ELSE(t):
    r'else'
    return t

# Funciones printf y scanf
def t_PRINTF(t):
    r'printf'
    return t

def t_SCANF(t):
    r'scanf'
    return t

# Cadenas de caracteres
def t_CADENA(t):
    r'\".*?\"'
    return t

# Caracteres
def t_CARACTER(t):
    r'\'.\''
    return t

# Tipos de datos
def t_TIPODATO(t):
    r'int|float|char|double|void|bool'
    return t

# Directivas de preprocesador
def t_INCLUDE(t):
    r'\#include[ ]*<.*?>'
    return t

# Comentarios de línea
def t_COMMENT(t):
    r'//.*'
    pass  # Ignorar comentarios de línea

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
    try:
        with open(r"Common Files\TesterFile.c", "r") as file:
            data = file.read()
    except FileNotFoundError:
        print("El archivo no se encuentra.")
        exit()

    lexer.input(data)
    print(f"\nAnalizando: {data}")

    with open("output.txt", "w") as file:
        for token in lexer:
            file.write(f"{token.type} {token.value}\n")

""" 
for token in lexer:
    print(f"{token.type} {token.value} ") """
