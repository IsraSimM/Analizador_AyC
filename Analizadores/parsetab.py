
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMARESTAleftMULTIDIVIDEAMPERSAND CADENA CARACTER CHAR COMA COMPARADOR CORCHETEDER CORCHETEIZQ DIVIDE ELSE FLOAT FOR IDENTIFICADOR IF IGUAL INCLUDE LLLAVE LPAREN MULTI NUMERO PRINTF PUNTO PUNTOYCOMA RESTA RLLAVE RPAREN SCANF SUMA TIPODATOprogram : preprocessor_directive_list function_definition_listpreprocessor_directive_list : preprocessor_directive\n                                   | preprocessor_directive preprocessor_directive_listpreprocessor_directive : INCLUDEfunction_definition_list : function_definition\n                                | function_definition function_definition_listfunction_definition : TIPODATO IDENTIFICADOR LPAREN parameter_list RPAREN blockparameter_list : declaration\n                      | declaration COMA parameter_list\n                      | emptyblock : LLLAVE RLLAVE\n             | LLLAVE statement_list RLLAVEstatement_list : statement\n                      | statement statement_liststatement : declaration\n                 | assignment_statement\n                 | printf_statement\n                 | scanf_statement\n                 | for_statement\n                 | if_statement\n                 | else_statement\n                 | function_calldeclaration : TIPODATO IDENTIFICADOR PUNTOYCOMA\n                   | TIPODATO IDENTIFICADOR CORCHETEIZQ NUMERO CORCHETEDER PUNTOYCOMAassignment_statement : IDENTIFICADOR IGUAL expression PUNTOYCOMA\n                            | IDENTIFICADOR CORCHETEIZQ expression CORCHETEDER IGUAL expression PUNTOYCOMAexpression : expression SUMA expression\n                  | expression RESTA expression\n                  | expression MULTI expression\n                  | expression DIVIDE expression\n                  | NUMERO\n                  | IDENTIFICADOR\n                  | CADENA\n                  | CARACTER\n                  | LPAREN expression RPARENfunction_call : IDENTIFICADOR LPAREN RPAREN PUNTOYCOMAprintf_statement : PRINTF LPAREN CADENA RPAREN PUNTOYCOMA\n                        | PRINTF LPAREN CADENA COMA expression RPAREN PUNTOYCOMAscanf_statement : SCANF LPAREN CADENA COMA AMPERSAND IDENTIFICADOR RPAREN PUNTOYCOMAif_statement : IF LPAREN condition RPAREN blockelse_statement : ELSE blockcondition : expression COMPARADOR expressionfor_statement : FOR LPAREN assignment_statement PUNTOYCOMA condition PUNTOYCOMA assignment_statement RPAREN blockempty :'
    
_lr_action_items = {'INCLUDE':([0,3,4,],[4,4,-4,]),'$end':([1,5,6,9,21,25,43,],[0,-1,-5,-6,-7,-11,-12,]),'TIPODATO':([2,3,4,6,8,11,18,19,21,22,25,27,28,29,30,31,32,33,34,35,43,52,53,68,75,88,92,98,99,102,104,],[7,-2,-4,7,-3,12,12,-23,-7,12,-11,12,-15,-16,-17,-18,-19,-20,-21,-22,-12,-41,-24,-25,-36,-37,-40,-26,-38,-39,-43,]),'IDENTIFICADOR':([7,12,19,22,25,27,28,29,30,31,32,33,34,35,43,45,46,50,51,52,53,59,68,69,70,71,72,75,77,79,81,87,88,90,92,97,98,99,102,104,],[10,16,-23,36,-11,36,-15,-16,-17,-18,-19,-20,-21,-22,-12,54,54,65,54,-41,-24,54,-25,54,54,54,54,-36,54,54,54,54,-37,96,-40,65,-26,-38,-39,-43,]),'LPAREN':([10,36,37,38,39,40,45,46,51,59,69,70,71,72,77,79,81,87,],[11,47,48,49,50,51,59,59,59,59,59,59,59,59,59,59,59,59,]),'RPAREN':([11,13,14,15,18,19,23,47,53,54,56,57,58,62,66,68,73,82,83,84,85,86,89,93,96,98,101,],[-44,17,-8,-10,-44,-23,-9,61,-24,-32,-31,-33,-34,76,80,-25,86,-27,-28,-29,-30,-35,95,-42,100,-26,103,]),'COMA':([14,19,53,62,63,],[18,-23,-24,77,78,]),'PUNTOYCOMA':([16,42,54,55,56,57,58,61,64,68,76,82,83,84,85,86,91,93,94,95,98,100,],[19,53,-32,68,-31,-33,-34,75,79,-25,88,-27,-28,-29,-30,-35,97,-42,98,99,-26,102,]),'CORCHETEIZQ':([16,36,65,],[20,46,46,]),'LLLAVE':([17,41,80,103,],[22,22,22,22,]),'PRINTF':([19,22,25,27,28,29,30,31,32,33,34,35,43,52,53,68,75,88,92,98,99,102,104,],[-23,37,-11,37,-15,-16,-17,-18,-19,-20,-21,-22,-12,-41,-24,-25,-36,-37,-40,-26,-38,-39,-43,]),'SCANF':([19,22,25,27,28,29,30,31,32,33,34,35,43,52,53,68,75,88,92,98,99,102,104,],[-23,38,-11,38,-15,-16,-17,-18,-19,-20,-21,-22,-12,-41,-24,-25,-36,-37,-40,-26,-38,-39,-43,]),'FOR':([19,22,25,27,28,29,30,31,32,33,34,35,43,52,53,68,75,88,92,98,99,102,104,],[-23,39,-11,39,-15,-16,-17,-18,-19,-20,-21,-22,-12,-41,-24,-25,-36,-37,-40,-26,-38,-39,-43,]),'IF':([19,22,25,27,28,29,30,31,32,33,34,35,43,52,53,68,75,88,92,98,99,102,104,],[-23,40,-11,40,-15,-16,-17,-18,-19,-20,-21,-22,-12,-41,-24,-25,-36,-37,-40,-26,-38,-39,-43,]),'ELSE':([19,22,25,27,28,29,30,31,32,33,34,35,43,52,53,68,75,88,92,98,99,102,104,],[-23,41,-11,41,-15,-16,-17,-18,-19,-20,-21,-22,-12,-41,-24,-25,-36,-37,-40,-26,-38,-39,-43,]),'RLLAVE':([19,22,25,26,27,28,29,30,31,32,33,34,35,43,44,52,53,68,75,88,92,98,99,102,104,],[-23,25,-11,43,-13,-15,-16,-17,-18,-19,-20,-21,-22,-12,-14,-41,-24,-25,-36,-37,-40,-26,-38,-39,-43,]),'NUMERO':([20,45,46,51,59,69,70,71,72,77,79,81,87,],[24,56,56,56,56,56,56,56,56,56,56,56,56,]),'CORCHETEDER':([24,54,56,57,58,60,82,83,84,85,86,],[42,-32,-31,-33,-34,74,-27,-28,-29,-30,-35,]),'IGUAL':([36,65,74,],[45,45,87,]),'CADENA':([45,46,48,49,51,59,69,70,71,72,77,79,81,87,],[57,57,62,63,57,57,57,57,57,57,57,57,57,57,]),'CARACTER':([45,46,51,59,69,70,71,72,77,79,81,87,],[58,58,58,58,58,58,58,58,58,58,58,58,]),'SUMA':([54,55,56,57,58,60,67,73,82,83,84,85,86,89,93,94,],[-32,69,-31,-33,-34,69,69,69,-27,-28,-29,-30,-35,69,69,69,]),'RESTA':([54,55,56,57,58,60,67,73,82,83,84,85,86,89,93,94,],[-32,70,-31,-33,-34,70,70,70,-27,-28,-29,-30,-35,70,70,70,]),'MULTI':([54,55,56,57,58,60,67,73,82,83,84,85,86,89,93,94,],[-32,71,-31,-33,-34,71,71,71,71,71,-29,-30,-35,71,71,71,]),'DIVIDE':([54,55,56,57,58,60,67,73,82,83,84,85,86,89,93,94,],[-32,72,-31,-33,-34,72,72,72,72,72,-29,-30,-35,72,72,72,]),'COMPARADOR':([54,56,57,58,67,82,83,84,85,86,],[-32,-31,-33,-34,81,-27,-28,-29,-30,-35,]),'AMPERSAND':([78,],[90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'preprocessor_directive_list':([0,3,],[2,8,]),'preprocessor_directive':([0,3,],[3,3,]),'function_definition_list':([2,6,],[5,9,]),'function_definition':([2,6,],[6,6,]),'parameter_list':([11,18,],[13,23,]),'declaration':([11,18,22,27,],[14,14,28,28,]),'empty':([11,18,],[15,15,]),'block':([17,41,80,103,],[21,52,92,104,]),'statement_list':([22,27,],[26,44,]),'statement':([22,27,],[27,27,]),'assignment_statement':([22,27,50,97,],[29,29,64,101,]),'printf_statement':([22,27,],[30,30,]),'scanf_statement':([22,27,],[31,31,]),'for_statement':([22,27,],[32,32,]),'if_statement':([22,27,],[33,33,]),'else_statement':([22,27,],[34,34,]),'function_call':([22,27,],[35,35,]),'expression':([45,46,51,59,69,70,71,72,77,79,81,87,],[55,60,67,73,82,83,84,85,89,67,93,94,]),'condition':([51,79,],[66,91,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> preprocessor_directive_list function_definition_list','program',2,'p_program','parser.py',14),
  ('preprocessor_directive_list -> preprocessor_directive','preprocessor_directive_list',1,'p_preprocessor_directive_list','parser.py',19),
  ('preprocessor_directive_list -> preprocessor_directive preprocessor_directive_list','preprocessor_directive_list',2,'p_preprocessor_directive_list','parser.py',20),
  ('preprocessor_directive -> INCLUDE','preprocessor_directive',1,'p_preprocessor_directive','parser.py',28),
  ('function_definition_list -> function_definition','function_definition_list',1,'p_function_definition_list','parser.py',33),
  ('function_definition_list -> function_definition function_definition_list','function_definition_list',2,'p_function_definition_list','parser.py',34),
  ('function_definition -> TIPODATO IDENTIFICADOR LPAREN parameter_list RPAREN block','function_definition',6,'p_function_definition','parser.py',42),
  ('parameter_list -> declaration','parameter_list',1,'p_parameter_list','parser.py',47),
  ('parameter_list -> declaration COMA parameter_list','parameter_list',3,'p_parameter_list','parser.py',48),
  ('parameter_list -> empty','parameter_list',1,'p_parameter_list','parser.py',49),
  ('block -> LLLAVE RLLAVE','block',2,'p_block','parser.py',59),
  ('block -> LLLAVE statement_list RLLAVE','block',3,'p_block','parser.py',60),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',68),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_list','parser.py',69),
  ('statement -> declaration','statement',1,'p_statement','parser.py',77),
  ('statement -> assignment_statement','statement',1,'p_statement','parser.py',78),
  ('statement -> printf_statement','statement',1,'p_statement','parser.py',79),
  ('statement -> scanf_statement','statement',1,'p_statement','parser.py',80),
  ('statement -> for_statement','statement',1,'p_statement','parser.py',81),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',82),
  ('statement -> else_statement','statement',1,'p_statement','parser.py',83),
  ('statement -> function_call','statement',1,'p_statement','parser.py',84),
  ('declaration -> TIPODATO IDENTIFICADOR PUNTOYCOMA','declaration',3,'p_declaration','parser.py',89),
  ('declaration -> TIPODATO IDENTIFICADOR CORCHETEIZQ NUMERO CORCHETEDER PUNTOYCOMA','declaration',6,'p_declaration','parser.py',90),
  ('assignment_statement -> IDENTIFICADOR IGUAL expression PUNTOYCOMA','assignment_statement',4,'p_assignment_statement','parser.py',98),
  ('assignment_statement -> IDENTIFICADOR CORCHETEIZQ expression CORCHETEDER IGUAL expression PUNTOYCOMA','assignment_statement',7,'p_assignment_statement','parser.py',99),
  ('expression -> expression SUMA expression','expression',3,'p_expression','parser.py',107),
  ('expression -> expression RESTA expression','expression',3,'p_expression','parser.py',108),
  ('expression -> expression MULTI expression','expression',3,'p_expression','parser.py',109),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','parser.py',110),
  ('expression -> NUMERO','expression',1,'p_expression','parser.py',111),
  ('expression -> IDENTIFICADOR','expression',1,'p_expression','parser.py',112),
  ('expression -> CADENA','expression',1,'p_expression','parser.py',113),
  ('expression -> CARACTER','expression',1,'p_expression','parser.py',114),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','parser.py',115),
  ('function_call -> IDENTIFICADOR LPAREN RPAREN PUNTOYCOMA','function_call',4,'p_function_call','parser.py',125),
  ('printf_statement -> PRINTF LPAREN CADENA RPAREN PUNTOYCOMA','printf_statement',5,'p_printf_statement','parser.py',129),
  ('printf_statement -> PRINTF LPAREN CADENA COMA expression RPAREN PUNTOYCOMA','printf_statement',7,'p_printf_statement','parser.py',130),
  ('scanf_statement -> SCANF LPAREN CADENA COMA AMPERSAND IDENTIFICADOR RPAREN PUNTOYCOMA','scanf_statement',8,'p_scanf_statement','parser.py',137),
  ('if_statement -> IF LPAREN condition RPAREN block','if_statement',5,'p_if_statement','parser.py',142),
  ('else_statement -> ELSE block','else_statement',2,'p_else_statement','parser.py',146),
  ('condition -> expression COMPARADOR expression','condition',3,'p_condition','parser.py',151),
  ('for_statement -> FOR LPAREN assignment_statement PUNTOYCOMA condition PUNTOYCOMA assignment_statement RPAREN block','for_statement',9,'p_for_statement','parser.py',156),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',161),
]
