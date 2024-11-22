import ply.yacc as yacc
from lexer import *  

# Orden de ejecucion 
precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTI', 'DIVIDE'),
)

# For
def p_statement_for(p):
    '''statement : FOR LPAREN for_init PUNTOYCOMA condition PUNTOYCOMA for_update RPAREN block'''
    p[0] = ('for', p[3], p[5], p[7], p[9])

#declaracion de la variable de inicio del bucle int i = 0;
def p_for_init(p):
    '''for_init : declaration
                | expression PUNTOYCOMA
                | empty'''
    p[0] = p[1]

# Declaración de variables
def p_declaration(p):
    '''declaration : TIPODATO IDENTIFICADOR IGUAL expression PUNTOYCOMA
                   | TIPODATO IDENTIFICADOR PUNTOYCOMA'''
    if len(p) == 6:
        p[0] = ('declaration', p[1], p[2], ('assign', p[2], p[4]))
    else:
        p[0] = ('declaration', p[1], p[2])

# Condición del for i < 10
def p_condition(p):
    '''condition : expression COMPARADOR expression'''
    p[0] = ('condition', p[1], p[2], p[3])

# actualización del for i++
def p_for_update(p):
    '''for_update : IDENTIFICADOR SUMA SUMA
                  | IDENTIFICADOR RESTA RESTA'''
    p[0] = ('update', p[1], '++' if p[2] == '+' else '--')

#includes
    '''preprocessor_directive : INCLUDE'''
    p[0] = ('include', p[1])

# funciones int main() { ... }
def p_function_definition(p):
    '''function_definition : TIPODATO IDENTIFICADOR LPAREN RPAREN block'''
    p[0] = ('function', p[1], p[2], p[5])

# Bloque de código entre llaves
def p_block(p):
    '''block : LLLAVE RLLAVE
             | LLLAVE statement_list RLLAVE'''
    if len(p) == 3:
        p[0] = ('block', [])
    else:
        p[0] = ('block', p[2])

#lista de declaraciones
def p_statement_list(p):
    '''statement_list : statement
                      | statement statement_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

# Regla general para una declaración o expresión
def p_statement(p):
    '''statement : declaration
                 | expression PUNTOYCOMA
                 | preprocessor_directive
                 | function_definition'''
    p[0] = p[1]

# Operaciones  suma, resta, multiplicación, división
def p_expression_binop(p):
    '''expression : expression SUMA expression
                  | expression RESTA expression
                  | expression MULTI expression
                  | expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

# Expresión numérica
def p_expression_number(p):
    'expression : NUMERO'
    p[0] = ('num', p[1])

# Expresión de identificador (variable)
def p_expression_identifier(p):
    'expression : IDENTIFICADOR'
    p[0] = ('id', p[1])

# Asignación de variables i = 0
def p_expression_assign(p):
    '''expression : IDENTIFICADOR IGUAL expression'''
    p[0] = ('assign', p[1], p[3])

# Regla para manejar producciones vacías
def p_empty(p):
    'empty :'
    pass

# Manejo de errores
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
        print("Árbol de derivación parcial hasta el error:")
        for symbol in parser.symstack[1:]:
            print(symbol)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

if __name__ == "__main__":
    data = input("Ingrese la expresión a analizar: ")
    result = parser.parse(data, lexer=lexer)
    print(f"Árbol de sintaxis: {result}")
