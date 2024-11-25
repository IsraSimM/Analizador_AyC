from sintaxy import *

class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # Pila de ámbitos

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def add_symbol(self, name, symbol_type, value=None):
        if name in self.scopes[-1]:
            raise Exception(f"Error: El símbolo '{name}' ya está declarado en este ámbito.")
        self.scopes[-1][name] = {'type': symbol_type, 'value': value}

    def get_symbol(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Error: El símbolo '{name}' no está declarado.")

    def update_symbol(self, name, value):
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name]['value'] = value
                return
        raise Exception(f"Error: El símbolo '{name}' no está declarado.")
