class Symbol:
    """Represents a named entity (variable, field, etc.) in the symbol table."""
    def __init__(self, name, symbol_type=None, **metadata):
        self.name = name
        self.symbol_type = symbol_type
        self.metadata = metadata

    def __repr__(self):
        return f"Symbol(name='{self.name}', type='{self.symbol_type}', metadata={self.metadata})"

class Scope:
    """Represents a lexical scope in the symbol table."""
    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = {}

    def define(self, symbol):
        """Defines a symbol in the current scope."""
        self.symbols[symbol.name.upper()] = symbol

    def lookup(self, name, local_only=False):
        """Looks up a symbol by name, optionally searching parent scopes."""
        name_upper = name.upper()
        symbol = self.symbols.get(name_upper)
        if symbol:
            return symbol
        if not local_only and self.parent:
            return self.parent.lookup(name_upper)
        return None

class SymbolTable:
    """Manages nested scopes and symbol resolution."""
    def __init__(self):
        self.global_scope = Scope()
        self.current_scope = self.global_scope

    def enter_scope(self):
        """Enters a new nested scope."""
        self.current_scope = Scope(parent=self.current_scope)

    def exit_scope(self):
        """Exits the current scope and returns to the parent scope."""
        if self.current_scope.parent:
            self.current_scope = self.current_scope.parent
        else:
            raise Exception("Cannot exit the global scope.")

    def define(self, name, symbol_type=None, **metadata):
        """Defines a new symbol in the current scope."""
        symbol = Symbol(name, symbol_type, **metadata)
        self.current_scope.define(symbol)
        return symbol

    def define_global(self, name, symbol_type=None, **metadata):
        """Defines a new symbol in the global scope."""
        symbol = Symbol(name, symbol_type, **metadata)
        self.global_scope.define(symbol)
        return symbol

    def lookup(self, name, local_only=False):
        """Resolves a symbol name to its definition."""
        return self.current_scope.lookup(name, local_only)
