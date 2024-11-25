import ply.yacc as yacc
from lexer import tokens  # Importar los tokens definidos en lexer.py

# Precedencia de operadores
precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTI', 'DIVIDE'),
)

# Programa principal
def p_program(p):
    '''program : preprocessor_directive_list function_definition_list'''
    p[0] = ('program', p[1], p[2])

def p_preprocessor_directive_list(p):
    '''preprocessor_directive_list : preprocessor_directive
                                   | preprocessor_directive preprocessor_directive_list'''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[2]

def p_preprocessor_directive(p):
    '''preprocessor_directive : INCLUDE'''
    p[0] = ('include', p[1])

def p_function_definition_list(p):
    '''function_definition_list : function_definition
                                | function_definition function_definition_list'''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[2]

def p_function_definition(p):
    '''function_definition : TIPODATO IDENTIFICADOR LPAREN parameter_list RPAREN block'''
    p[0] = ('function', p[1], p[2], p[4], p[6])

def p_parameter_list(p):
    '''parameter_list : declaration
                      | declaration COMA parameter_list
                      | empty'''
    p[0] = [p[1]] if len(p) == 2 and p[1] != 'empty' else [] if p[1] == 'empty' else [p[1]] + p[3]

def p_block(p):
    '''block : LLLAVE RLLAVE
             | LLLAVE statement_list RLLAVE'''
    p[0] = ('block', []) if len(p) == 3 else ('block', p[2])

def p_statement_list(p):
    '''statement_list : statement
                      | statement statement_list'''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[2]

def p_statement(p):
    '''statement : for_statement
                 | assignment_statement
                 | printf_statement
                 | scanf_statement
                 | declaration
                 | if_statement
                 | else_statement
                 | function_call'''
    p[0] = p[1]

# Reglas para declaraciones
def p_declaration(p):
    '''declaration : TIPODATO identificador_list PUNTOYCOMA
                   | TIPODATO IDENTIFICADOR IGUAL expression PUNTOYCOMA
                   | TIPODATO IDENTIFICADOR CORCHETEIZQ NUMERO CORCHETEDER PUNTOYCOMA'''
    if len(p) == 4:  # Lista de variables sin inicializar
        p[0] = ('declaration', p[1], p[2])
    elif len(p) == 6:  # Variable inicializada
        p[0] = ('declaration', p[1], [(p[2], p[4])])
    elif len(p) == 7:  # Array
        p[0] = ('array_declaration', p[1], p[2], p[4])

def p_identificador_list(p):
    '''identificador_list : IDENTIFICADOR
                          | IDENTIFICADOR COMA identificador_list'''
    if len(p) == 2:
        p[0] = [(p[1], None)]  # Identificador sin inicialización
    else:
        p[0] = [(p[1], None)] + p[3]  # Lista de identificadores

def p_assignment_statement(p):
    '''assignment_statement : IDENTIFICADOR IGUAL expression PUNTOYCOMA
                            | IDENTIFICADOR CORCHETEIZQ expression CORCHETEDER IGUAL expression PUNTOYCOMA'''
    p[0] = ('assign', p[1], p[3]) if len(p) == 5 else ('array_assign', p[1], p[3], p[6])

def p_expression(p):
    '''expression : expression SUMA expression
                  | expression RESTA expression
                  | expression MULTI expression
                  | expression DIVIDE expression
                  | NUMERO
                  | IDENTIFICADOR
                  | CADENA
                  | CARACTER
                  | condition
                  | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4 and p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = (p[2], p[1], p[3])

def p_function_call(p):
    '''function_call : IDENTIFICADOR LPAREN RPAREN PUNTOYCOMA'''
    p[0] = ('function_call', p[1])

def p_printf_statement(p):
    '''printf_statement : PRINTF LPAREN CADENA RPAREN PUNTOYCOMA
                        | PRINTF LPAREN CADENA COMA expression RPAREN PUNTOYCOMA'''
    p[0] = ('printf', p[3]) if len(p) == 6 else ('printf', p[3], p[5])

def p_scanf_statement(p):
    '''scanf_statement : SCANF LPAREN CADENA COMA AMPERSAND IDENTIFICADOR RPAREN PUNTOYCOMA'''
    p[0] = ('scanf', p[3], p[6])

def p_if_statement(p):
    '''if_statement : IF LPAREN condition RPAREN block'''
    p[0] = ('if', p[3], p[5])

def p_else_statement(p):
    '''else_statement : ELSE block'''
    p[0] = ('else', p[2])

""" def p_for_statement(p):
    '''for_statement : FOR LPAREN assignment_statement condition PUNTOYCOMA assignment_statement RPAREN block'''
    p[0] = ('for', p[3], p[5], p[7], p[9]) """

def p_for_statement(p):
    '''for_statement : FOR LPAREN assignment_statement RPAREN block'''
    p[0] = ('for', p[2], p[3], p[4])

def p_condition(p):
    '''condition : expression COMPARADOR expression'''
    p[0] = ('condition', p[1], p[2], p[3])

def p_empty(p):
    'empty :'
    p[0] = None

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' en la línea {p.lineno}")
    else:
        print("Error de sintaxis al final del archivo")

parser = yacc.yacc()

def pretty_print_tree(node, indent=0):
    """
    Función para imprimir el árbol de sintaxis de manera estructurada.
    :param node: El nodo actual del árbol (puede ser una tupla, lista o valor simple).
    :param indent: Nivel de indentación actual.
    """
    spacer = ' ' * (indent * 2)  # Espaciado para la indentación
    if isinstance(node, tuple):  # Nodo compuesto
        print(f"{spacer}{node[0]}:")
        for child in node[1:]:
            pretty_print_tree(child, indent + 1)
    elif isinstance(node, list):  # Lista de nodos (como declaraciones o sentencias)
        print(f"{spacer}[")
        for item in node:
            pretty_print_tree(item, indent + 1)
        print(f"{spacer}]")
    else:  # Nodo hoja (valor simple)
        print(f"{spacer}{node}")


if __name__ == "__main__":
    with open("Common Files/TesterFile.c", "r") as file:
        data = file.read()
    result = parser.parse(data)
    print("Árbol de sintaxis:")
    pretty_print_tree(result)
