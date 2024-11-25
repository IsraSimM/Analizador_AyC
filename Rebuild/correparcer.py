from sintaxy import *

try:
    with open(r"Common Files\TesterFile.c", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("El archivo no se encuentra.")
    exit()

# Código fuente
code = data

print("Código fuente:", code)

print("\nAnálisis léxico:")
# Analizar el código
parser.parse(code)

test_parser(code)
