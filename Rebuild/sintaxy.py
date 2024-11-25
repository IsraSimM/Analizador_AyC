import ply.yacc as yacc
from lexy import tokens

# Definir la clase para el árbol sintáctico (AST)
class ASTNode:
    def __init__(self, type_, value=None, children=None):
        self.type = type_
        self.value = value if value is not None else ""  # Aseguramos que value no sea None
        self.children = children if children else []
    
    def add_child(self, child):
        self.children.append(child)
    
    def __repr__(self):
        repr_str = f"{self.type}: {self.value}\n"
        for child in self.children:
            repr_str += child.__repr__()  # Llamamos a __repr__ sin parámetros adicionales
        return repr_str

# Función para imprimir el árbol de sintaxis (AST)
def pretty_print_tree(node, indent=0):
    spacer = ' ' * (indent * 2)
    if isinstance(node, ASTNode):
        print(f"{spacer}{node.type}: {node.value}")
        for child in node.children:
            pretty_print_tree(child, indent + 1)

# Reglas gramaticales
def p_program(p):
    '''program : INCLUDE HEADER program
               | function'''
    if len(p) == 4:
        p[0] = ASTNode("program", children=[p[1], p[2], p[3]])
    else:
        p[0] = p[1]

def p_function(p):
    '''function : INT MAIN LPAREN RPAREN LBRACE statement_list RBRACE'''
    p[0] = ASTNode("function", children=[p[1], p[2], p[3], p[4], p[5], p[6]])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = ASTNode("statement_list", children=[p[1], p[2]])
    else:
        p[0] = ASTNode("statement_list", children=[p[1]])

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
        p[0] = ASTNode("identifier_list", children=[p[1]])
    else:
        p[0] = ASTNode("identifier_list", children=[p[1], p[3]])

def p_declaration(p):
    '''declaration : type_specifier IDENTIFIER EQUAL expression SEMICOLON
                   | type_specifier identifier_list SEMICOLON
                   | type_specifier identifier_list LBRAKET NUMBER RBRAKET SEMICOLON'''
    if len(p) == 6:
        p[0] = ASTNode("declaration", children=[p[1], p[2], p[3], p[4], p[5]])
    elif len(p) == 4:
        p[0] = ASTNode("declaration", children=[p[1], p[2], p[3]])
    else:
        p[0] = ASTNode("declaration", children=[p[1], p[2], p[3], p[4], p[5], p[6]])

def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | CHAR'''
    p[0] = ASTNode("type_specifier", value=p[1])

def p_compound_assignment(p):
    '''compound_assignment : PLUS EQUAL
                           | MINUS EQUAL
                           | TIMES EQUAL
                           | DIVIDE EQUAL'''
    p[0] = ASTNode("compound_assignment", value=p[1])

def p_assignment(p):
    '''assignment : IDENTIFIER EQUAL expression SEMICOLON
                  | IDENTIFIER compound_assignment expression SEMICOLON
                  | IDENTIFIER LBRAKET expression RBRAKET compound_assignment expression SEMICOLON
                  | IDENTIFIER LBRAKET expression RBRAKET EQUAL expression SEMICOLON'''
    if len(p) == 5:
        p[0] = ASTNode("assignment", children=[p[1], p[2], p[3], p[4]])
    elif len(p) == 4:
        p[0] = ASTNode("assignment", children=[p[1], p[2], p[3]])

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
        p[0] = ASTNode("expression", value=p[2], children=[p[1], p[3]])
    elif len(p) == 3 and p[1] == '(':
        p[0] = ASTNode("expression", value="parenthesis", children=[p[2]])
    elif len(p) == 2:
        p[0] = ASTNode("expression", value=p[1])

def p_expression_list(p):
    '''expression_list : expression
                       | expression COMMA expression_list'''
    if len(p) == 2:
        p[0] = ASTNode("expression_list", children=[p[1]])
    else:
        p[0] = ASTNode("expression_list", children=[p[1], p[3]])

def p_unitarymodifiers(p):
    '''unitarymodifiers : IDENTIFIER PLUS PLUS
                        | IDENTIFIER MINUS MINUS'''
    p[0] = ASTNode("unitarymodifiers", children=[p[1]])

def p_for_loop(p):
    '''for_loop : FOR LPAREN assignment condition SEMICOLON unitarymodifiers RPAREN LBRACE statement_list RBRACE'''
    p[0] = ASTNode("for_loop", children=[p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]])

def p_condition(p):
    '''condition : expression COMPARER expression'''
    p[0] = ASTNode("condition", children=[p[1], p[2], p[3]])

def p_if_statement(p):
    '''if_statement : IF LPAREN condition RPAREN LBRACE statement_list RBRACE
                    | IF LPAREN condition RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'''
    if len(p) == 8:
        p[0] = ASTNode("if_statement", children=[p[1], p[2], p[3], p[4], p[5], p[6], p[7]])
    else:
        p[0] = ASTNode("if_statement", children=[p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]])

def p_function_call(p):
    '''function_call : PRINTF LPAREN STRING COMMA IDENTIFIER RPAREN SEMICOLON
                     | PRINTF LPAREN STRING RPAREN SEMICOLON
                     | PRINTF LPAREN STRING COMMA expression_list RPAREN SEMICOLON
                     | SCANF LPAREN STRING COMMA AMPERSAND IDENTIFIER RPAREN SEMICOLON'''
    p[0] = ASTNode("function_call", children=[p[1], p[2], p[3]])

def p_return_statement(p):
    '''return_statement : RETURN SEMICOLON
                        | RETURN expression SEMICOLON'''
    if len(p) == 3:
        p[0] = ASTNode("return_statement", children=[p[1]])
    else:
        p[0] = ASTNode("return_statement", children=[p[1], p[2]])

def p_error(p):
    if p:
        print(f"Error de sintaxis en la línea {p.lineno}: {p.value}")
    else:
        print("Error de sintaxis al final del archivo")

# Construir el parser
parser = yacc.yacc()

# Función de prueba con entrada de ejemplo
def test_parser(input_data):
    result = parser.parse(input_data)
    print("Árbol de derivación:")
    pretty_print_tree(result)  # Usamos pretty_print_tree para visualizar el AST
