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
        # Caso: Lista de expresiones
        if len(expression) == 1:
            return analyze_expression(expression[0], symbol_table)
        elif expression == ['(', ')']:
            # Ignorar paréntesis explícitos
            return None
        else:
            raise ValueError(f"Lista con múltiples elementos no válida: {expression}")
    
    elif isinstance(expression, tuple) and len(expression) > 0:
        if expression[0] == 'expression':
            if len(expression) == 2:
                # Subexpresión simple
                subexpr = expression[1]
                if isinstance(subexpr, str) and subexpr in symbol_table:
                    return symbol_table[subexpr]
                elif isinstance(subexpr, int):
                    return 'int'
                elif isinstance(subexpr, float):
                    return 'float'
                elif isinstance(subexpr, tuple):
                    return analyze_expression(subexpr, symbol_table)
                else:
                    raise ValueError(f"Token desconocido: {subexpr}")
            elif len(expression) == 3:
                # Operación binaria
                operator = expression[1]
                operands = expression[2]
                if not isinstance(operands, list) or len(operands) != 2:
                    raise ValueError(f"Operadores no válidos: {operands}")
                operand_types = [
                    analyze_expression(op, symbol_table)
                    for op in operands if op != ['(', ')']
                ]
                if operator in ['+', '-', '*', '/']:
                    if 'float' in operand_types:
                        return 'float'
                    else:
                        return 'int'
                else:
                    raise ValueError(f"Operador desconocido: {operator}")
            elif len(expression) == 4 and isinstance(expression[3], list):
                # Ignorar paréntesis explícitos
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
        namesSplit = str(names).replace("('identifier_list', [", "").replace("])", "").replace("'", "")
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
        
        # Imprimir las funciones
        print("\nFunciones declaradas:")
        for func, details in self.functions.items():
            print(f"  - {func}: {details['return_type']} (params: {', '.join(details['params'])})")

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
                   | type_specifier identifier_list LBRAKET NUMBER RBRAKET SEMICOLON'''
    if len(p) == 6:
        p[0] = ('declaration', [p[1], p[2], p[3], p[4], p[5]])
        tableSy.add_variable(p[2], p[1][1])
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
        print("Undefined variable: ",p[1])
        exit()
    #validar asignacion de tipos de datos correctos, int = int, float = float
    else:
        print("Variable: ",p[3:4])
        print("Tipo: ",p[3][1])
        try:
            result = analyze_expression(p[3:4], tableSy.symbols)
            print("Tipo resultante:", result)
        except Exception as e:
            print(f"Error: {e}")
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


with open("Common Files/TesterFile.c", "r") as file:
    data = file.read()
result = parser.parse(data)
print("Árbol de sintaxis:")
#pretty_print_tree(result)

class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.functions = {}

    def add_variable(self, name, var_type):
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
        
        # Imprimir las funciones
        print("\nFunciones declaradas:")
        for func, details in self.functions.items():
            print(f"  - {func}: {details['return_type']} (params: {', '.join(details['params'])})")

tableSy.print_symbol_table()