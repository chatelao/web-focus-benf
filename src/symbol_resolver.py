from asg import *
from symbol_table import SymbolTable

class SymbolResolver:
    """
    Traverses the Abstract Semantic Graph (ASG) to resolve symbols and populate the SymbolTable.
    Currently focuses on Dialogue Manager (DM) variable resolution.
    """
    def __init__(self, symbol_table=None):
        self.symbol_table = symbol_table or SymbolTable()

    def resolve(self, nodes):
        """Main entry point for resolving symbols in a list of ASG nodes or a single node."""
        if isinstance(nodes, list):
            for node in nodes:
                self.visit(node)
        else:
            self.visit(nodes)
        return self.symbol_table

    def visit(self, node):
        """Dispatches to specific visit methods based on node type."""
        if node is None or not isinstance(node, ASGNode):
            return

        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Default visitor that recurses into all ASGNode attributes and lists of ASGNodes."""
        for attr_name, attr_value in vars(node).items():
            if isinstance(attr_value, ASGNode):
                self.visit(attr_value)
            elif isinstance(attr_value, list):
                for item in attr_value:
                    if isinstance(item, ASGNode):
                        self.visit(item)

    def visit_SetDM(self, node):
        """Registers a Dialogue Manager variable definition from -SET."""
        # Define the variable in the symbol table if it doesn't exist
        # Metadata could eventually store the expression or evaluated value
        self.symbol_table.define(node.variable, symbol_type='DM_VAR')
        self.visit(node.expression)

    def visit_Repeat(self, node):
        """Registers a Dialogue Manager loop variable definition from -REPEAT."""
        if hasattr(node, 'loop_var') and node.loop_var:
            self.symbol_table.define(node.loop_var, symbol_type='DM_VAR')

        # Visit all relevant components
        for attr in ['condition', 'times', 'start_val', 'end_val', 'step_val']:
            if hasattr(node, attr):
                self.visit(getattr(node, attr))

    def visit_AmperVar(self, node):
        """Resolves a Dialogue Manager variable usage."""
        symbol = self.symbol_table.lookup(node.name)
        # We attach the symbol to the node for later stages (IR generation, etc.)
        node.symbol = symbol
        if not symbol:
            # For WebFOCUS, variables might be external parameters.
            # We can still track them as potential external dependencies.
            pass
