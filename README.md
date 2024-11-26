# Analizador AyC
**Un analizador sintáctico y semántico desarrollado con PLY y YACC.**
**Aldana Zamudio Alexis Vladimir**
**Campero Enciso Juan Francisco**
**Peña Escamilla Luis Angel**
**Simon Martinez Israel**

Este proyecto implementa un analizador basado en Python para procesar programas escritos en C, utilizando la biblioteca PLY (Python Lex-Yacc). Incluye un análisis léxico, sintáctico y semántico, y genera un árbol sintáctico a partir del código fuente proporcionado.

## Requisitos
Antes de ejecutar el analizador, asegúrate de tener instaladas las siguientes dependencias:

1. **PLY**: Biblioteca para análisis léxico y sintáctico.
   	Instalar usando:
	```bash
 	pip install ply
Regex: Biblioteca para trabajar con expresiones regulares.
	Instalar usando:
	´´´bash
	pip install regex
Ejecución
Para ejecutar el analizador, desde el ID o editor de codigo

Si encuentras errores relacionados con la ruta de acceso al archivo fuente, modifica la línea 307 de sintaxy.py para reflejar la ubicación correcta de CorrectedProgram.c. Ejemplo:

Opción 1: ../Common Files/CorrectedProgram.c
Opción 2: Common Files/CorrectedProgram.c
Características del Analizador
El analizador está diseñado específicamente para procesar el archivo CorrectedProgram.c y realiza los siguientes análisis:

1. Análisis Léxico
Análisis de caracteres.
Asignación de tokens.

2. Análisis Sintáctico
El analizador soporta las siguientes construcciones del lenguaje C:
	Declaración de variables:
		Declaración simple:
			token_type identifier semicolon
		Declaración con inicialización:
			token_type identifier equals expression semicolon
		Declaración múltiple:
			token_type identifier_list semicolon
		Declaración múltiple con inicialización:
			token_type identifier_list equals expression semicolon
	Asignación de valores.
	Directivas de preprocesador.
	Función main().
	Bucles for simples.
	Condicionales if.
	Impresiones (printf).
	Escaneos (scanf).
	Generación de árbol sintáctico.
3. Análisis Semántico
	Creación de la tabla de símbolos.
	Identificación de tipos en expresiones.
	Detección de variables no declaradas.
	Verificación de tipos de datos en asignaciones.

	
		



