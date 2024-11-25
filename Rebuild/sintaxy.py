import ply.yacc as yacc
from lexy import tokens
import re

def analyze_expression(expression, symbol_table):
    """
    Analiza una expresión estructurada para determinar los tipos de cada subexpresión.

    Args:
        expression (tuple | list): Estructura de la expresión a analizar.
        symbol_table (dict): Diccionario con las variables y sus tipos.

    Returns:
        str: Tipo resultante de la expresión ('int', 'float', 'string', etc.).
    """
    if isinstance(expression, list):
        # Si la expresión es una lista, filtramos cualquier lista vacía como ['(', ')']
        clean_expressions = [subexpr for subexpr in expression if subexpr != ['(', ')']]
        
        # Si la lista es vacía o tiene un solo elemento, procesamos la única expresión que queda
        if len(clean_expressions) == 1:
            return analyze_expression(clean_expressions[0], symbol_table)
        elif len(clean_expressions) > 1:
            # Procesar todas las expresiones en la lista
            operand_types = [analyze_expression(subexpr, symbol_table) for subexpr in clean_expressions]
            return operand_types[-1]  # Retornamos el tipo del último operando procesado
        else:
            # Si la lista está vacía o solo contiene paréntesis, retornamos None
            return None

    elif isinstance(expression, tuple) and len(expression) > 0:
        if expression[0] == 'expression':
            if len(expression) == 2:
                # Subexpresión simple: tipo de variable o número
                subexpr = expression[1]
                if isinstance(subexpr, str) and subexpr in symbol_table:
                    return symbol_table[subexpr]  # Retorna el tipo de la variable según el diccionario
                elif isinstance(subexpr, (int, float)):
                    return 'float' if isinstance(subexpr, float) else 'int'  # Retorna el tipo numérico
                else:
                    raise ValueError(f"Token desconocido: {subexpr}")
            elif len(expression) == 3:
                # Operación binaria: operator y operandos
                operator = expression[1]
                operands = expression[2]
                if not isinstance(operands, list):
                    raise ValueError(f"Operadores no válidos: {operands}")
                
                operand_types = [analyze_expression(op, symbol_table) for op in operands]
                
                # Determinar tipo según los operandos y el operador
                if operator in ['+', '-', '*', '/']:
                    return 'float' if 'float' in operand_types else 'int'
                else:
                    raise ValueError(f"Operador desconocido: {operator}")
            elif len(expression) == 4 and isinstance(expression[3], list):
                # Ignorar listas de paréntesis decorativos
                return analyze_expression(expression[2], symbol_table)
            else:
                raise ValueError(f"Estructura no válida: {expression}")
        else:
            raise ValueError(f"Estructura desconocida: {expression}")
    else:
        raise ValueError(f"Entrada no válida: {expression}")

class SymbolTable():
    def __init__(self):
        self.symbols = {}
        self.functions = {}

    def add_variable(self, name, var_type):
        if len(self.symbols)!=0 and name in self.symbols:
            raise Exception(f"Variable '{name}' ya declarada.")
        self.symbols.update({name: var_type})

    def add_variables(self, names, var_type):
        namesSplit = str(names).replace("('identifier_list', [", "").replace("])", "").replace("'", "").replace("[","").replace("]","")
        # Separar en una lista de palabras
        word_list = namesSplit.split(", ")

        # Recorrer las palabras con un bucle for
        for name in word_list:
            if name in self.symbols:
                raise Exception(f"Variable '{name}' ya declarada.")
            self.symbols[name] = var_type

    def add_function(self, name, return_type, params):
        if name in self.functions:
            raise Exception(f"Función '{name}' ya declarada.")
        self.functions[name] = {'return_type': return_type, 'params': params}

    def get_variable_type(self, name):
        return self.symbols.get(name)

    def get_function(self, name):
        return self.functions.get(name)

    def print_symbol_table(self):
        # Imprimir las variables
        print("Variables declaradas:")
        for var, var_type in self.symbols.items():
            print(f"  - {var}: {var_type}")

tableSy = SymbolTable()

# Reglas gramaticales
def p_program(p):
    '''program : preprocesor_directives_list function
               | function'''
    if len(p) == 3:
        p[0] = ('program', [p[1], p[2]])
    else:
        p[0] = p[1]

def p_preprocesor_directives_list(p):
    '''preprocesor_directives_list : preprocesor_directive preprocesor_directives_list
                                   | preprocesor_directive'''
    if len(p) == 3:
        p[0] = ('preprocesor_directives_list', [p[1], p[2]])
    else:
        p[0] = p[1]

def p_preprocesor_directive(p):
    '''preprocesor_directive : INCLUDE HEADER'''
    p[0] = p[1]

def p_function(p):
    '''function : INT MAIN LPAREN RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('function', [p[1], p[2], p[6]])

def p_statement_list(p):
    '''statement_list : statement statement_list 
                      | statement'''
    if len(p) == 3:
        p[0] = ('statement_list', [p[1], p[2]])
    else:
        p[0] = ('statement_list', [p[1]])

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | for_loop
                 | if_statement
                 | function_call
                 | return_statement'''
    p[0] = p[1]

def p_identifier_list(p):
    '''identifier_list : IDENTIFIER
                       | IDENTIFIER COMMA identifier_list'''
    if len(p) == 2:
        p[0] = ('identifier_list', [p[1]])
    else:
        p[0] = ('identifier_list', [p[1], p[3]])

def p_declaration(p):
    '''declaration : type_specifier IDENTIFIER EQUAL expression SEMICOLON
                   | type_specifier identifier_list SEMICOLON
                   | type_specifier identifier_list EQUAL expression SEMICOLON
                   | type_specifier identifier_list LBRAKET NUMBER RBRAKET SEMICOLON'''
    if len(p) == 6 and len(p[2]) == 1:
        p[0] = ('declaration', [p[1], p[2], p[3], p[4], p[5]])
        print("Hodfaaa",p[2], "Holsass", p[1][1])
        tableSy.add_variable(p[2], p[1][1])
    elif len(p) == 6:
        try:
            p[0] = ('declaration', [p[1], p[2], p[3], p[4], p[5]])
            tableSy.add_variables(str(p[2]), p[1][1])
        except Exception as e:
            print(e)
    elif len(p) == 4:
        p[0] = ('declaration', [p[1], p[2], p[3]])
        tableSy.add_variables(p[2], p[1][1])
    else:
        p[0] = ('declaration', [p[1], p[2], p[3], p[4], p[5], p[6]])
        tableSy.add_variables(p[2], p[1][1])
    
def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | CHAR'''
    p[0] = ('type_specifier', p[1])

def p_compound_assignment(p):
    '''compound_assignment : PLUS EQUAL
                           | MINUS EQUAL
                           | TIMES EQUAL
                           | DIVIDE EQUAL'''
    p[0] = ('compound_assignment', p[1])

def p_assignment(p):
    '''assignment : IDENTIFIER EQUAL expression SEMICOLON
                  | IDENTIFIER compound_assignment expression SEMICOLON
                  | IDENTIFIER LBRAKET expression RBRAKET compound_assignment expression SEMICOLON
                  | IDENTIFIER LBRAKET expression RBRAKET EQUAL expression SEMICOLON'''
    if not p[1] in tableSy.symbols:
        print("Error semantico: undefined variable: ",p[1], "en la linea", p.lineno(1))
        exit()
    else:
        if p[2] == '[':
            arrayresult = analyze_expression(p[3], tableSy.symbols)
            if arrayresult != 'int':
                print(f"Error: El índice del array '{p[1]}' debe ser de tipo entero.")
                exit()
        result = analyze_expression(p[len(p)-2], tableSy.symbols)
        if result != tableSy.symbols[p[1]]:
            print(f"Error: Asignación de tipo incorrecto para '{p[1]}': {tableSy.symbols[p[1]]} = {result}")
            exit()
        if len(p) == 5:
            p[0] = ('assignment', [p[1], p[2], p[3], p[4]])
        elif len(p) == 4:
            p[0] = ('assignment', [p[1], p[2], p[3]])

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | LPAREN expression RPAREN
                  | NUMBER
                  | CHAR_LITERAL
                  | CHAR
                  | IDENTIFIER
                  | IDENTIFIER LBRAKET expression RBRAKET'''
    if len(p) == 4:
        p[0] = ('expression', p[2], [p[1], p[3]])
    elif len(p) == 3 and p[1] == '(':
        p[0] = ('expression', 'parenthesis', [p[2]])
    elif len(p) == 2:
        p[0] = ('expression', p[1])

def p_expression_list(p):
    '''expression_list : expression
                       | expression COMMA expression_list'''
    if len(p) == 2:
        p[0] = ('expression_list', [p[1]])
    else:
        p[0] = ('expression_list', [p[1], p[3]])

def p_unitarymodifiers(p):
    '''unitarymodifiers : IDENTIFIER PLUS PLUS
                        | IDENTIFIER MINUS MINUS'''
    p[0] = ('unitarymodifiers', [p[1], p[2]])

def p_for_loop(p):
    '''for_loop : FOR LPAREN assignment condition SEMICOLON unitarymodifiers RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('for_loop', [p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]])

def p_condition(p):
    '''condition : expression COMPARER expression'''
    p[0] = ('condition', [p[1], p[2], p[3]])

def p_if_statement(p):
    '''if_statement : IF LPAREN condition RPAREN LBRACE statement_list RBRACE
                    | IF LPAREN condition RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'''
    if len(p) == 8:
        p[0] = ('if_statement', [p[1], p[2], p[3], p[4], p[5], p[6], p[7]])
    else:
        p[0] = ('if_statement', [p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]])

def p_function_call(p):
    '''function_call : PRINTF LPAREN STRING COMMA IDENTIFIER RPAREN SEMICOLON
                     | PRINTF LPAREN STRING RPAREN SEMICOLON
                     | PRINTF LPAREN STRING COMMA expression_list RPAREN SEMICOLON
                     | SCANF LPAREN STRING COMMA AMPERSAND IDENTIFIER RPAREN SEMICOLON'''
    p[0] = ('function_call', [p[1], p[2], p[3]])

def p_return_statement(p):
    '''return_statement : RETURN SEMICOLON
                        | RETURN expression SEMICOLON'''
    if len(p) == 3:
        p[0] = ('return_statement', [p[1]])
    else:
        p[0] = ('return_statement', [p[1], p[2]])

def p_error(p):
    if p:
        print(f'Error de sintaxis en la línea {p.lineno}: {p.value}')
        exit()
    else:
        print('Error de sintaxis al final del archivo')

# Construir el parser
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


with open("./Common Files/CorrectedProgram.c", "r") as file:
    data = file.read()
result = parser.parse(data)        

tableSy.print_symbol_table()

print("\nÁrbol de sintaxis:")
pretty_print_tree(result)
print("\nAnálisis de expresiones:")
print("No se encontraron errores de codigo")