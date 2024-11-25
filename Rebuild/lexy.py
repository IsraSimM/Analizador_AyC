import ply.lex as lex

# Lista de tokens
tokens = [
    'INCLUDE', 'HEADER', 'INT', 'FLOAT', 'CHAR', 'IDENTIFIER', 'NUMBER', 'SEMICOLON',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COMMA', 'EQUAL', 'PLUS', 'MINUS',
    'TIMES', 'DIVIDE', 'COMPARER', 'STRING', 'CHAR_LITERAL', 'AMPERSAND', 
    'RBRAKET', 'LBRAKET', 'DOT'
]

# Palabras clave
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'for': 'FOR',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'printf': 'PRINTF',
    'scanf': 'SCANF',
    'main': 'MAIN'
}

# Agregar palabras clave como tokens
tokens += list(reserved.values())

# Reglas para tokens simples
t_INCLUDE = r'\#include'
t_DOT = r'\.'
t_LBRAKET = r'\['
t_RBRAKET = r'\]'
t_HEADER = r'<[a-zA-Z_][a-zA-Z0-9_]*\.h>'
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_EQUAL = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_STRING = r'\".*?\"'
t_CHAR_LITERAL = r'\'.\''
t_AMPERSAND = r'&'
t_COMPARER = r'==|!=|<=|>=|<|>'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Regla para números
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Regla para identificadores y palabras clave
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

# Regla para nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Error de carácter ilegal '{t.value[0]}' en la línea {t.lexer.lineno}")
    t.lexer.skip(1)


# Construir el lexer
lexer = lex.lex()
