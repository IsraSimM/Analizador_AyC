# Analizador_AyC
 Analizador sintactico y semantico usando PLY_YACC
 1)instalar librería Python PLY desde la terminal 
$pip install ply

2) instalar librería de Python regex desde la terminal 
$pip install regex

3) ejecutar sintaxy.py, en caso de error solo modificar la linea 307 de acuerdo a la dirección del archivo (../Common Files/CorrectedProgram.c)(Common Files/CorrectedProgram.c)

El analizador esta realizado de acuerdo a el archivo CorrectedProgram.c y toma como consideración los siguientes bloques: 
análisis léxico: 
	análisis de caracteres 
	asignación de tokens 

análisis sintáctico:	
	declaración de variables:
		declaración simple: token_type identifier semicolon
		declaración con inicialización: token_type identifier equals expression semicolon
		declaración múltiple: token_type identifier_list semicolon
		declaración múltiple con inicializacion: token_type identifier_list equals expression semicolon
	asignación de valores 
	directivas de procesamiento
	funtion main()
	bucles for simples
	condicional if
	impresiones 
	escaneos 
	árbol sintáctico 

	
análisis semántico: 
	tabla de símbolos 
	identificación de tipo en una expresión 
	identificación de variables no declaradas 
	verificación de tipos de dato en la asignación 
	
		



