from asg import *
from symbol_table import SymbolTable

class SymbolResolver:
    """
    Traverses the Abstract Semantic Graph (ASG) to resolve symbols and populate the SymbolTable.
    Handles Dialogue Manager (DM) variables and Field references.
    """
    def __init__(self, symbol_table=None, metadata_registry=None):
        self.symbol_table = symbol_table or SymbolTable()
        self.metadata_registry = metadata_registry

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
        node.symbol = symbol

    def visit_ReportRequest(self, node):
        """Resolves field references within a TABLE FILE request."""
        if self.metadata_registry:
            master_file = self.metadata_registry.get_master_file(node.filename)
            node.master_file = master_file # Schema Binding

            if master_file:
                self.symbol_table.enter_scope()
                # Register fields from the Master File
                for segment in master_file.segments:
                    for field in segment.fields:
                        # Register both short name and qualified name
                        self.symbol_table.define(field.name, symbol_type='FIELD', metadata={'field': field, 'segment': segment})
                        self.symbol_table.define(f"{segment.name}.{field.name}", symbol_type='FIELD', metadata={'field': field, 'segment': segment})

                    for vf in segment.virtual_fields:
                        self.symbol_table.define(vf.name, symbol_type='VIRTUAL_FIELD', metadata={'define': vf, 'segment': segment})
                        self.symbol_table.define(f"{segment.name}.{vf.name}", symbol_type='VIRTUAL_FIELD', metadata={'define': vf, 'segment': segment})

                for vf in master_file.virtual_fields:
                    self.symbol_table.define(vf.name, symbol_type='VIRTUAL_FIELD', metadata={'define': vf})

                # Visit components (verbs, WHERE, COMPUTE, etc.)
                for component in node.components:
                    self.visit(component)

                self.symbol_table.exit_scope()
                return

        # If no metadata registry or master file not found, still visit components but symbols might not resolve
        self.generic_visit(node)

    def visit_Identifier(self, node):
        """Resolves a field name usage."""
        symbol = self.symbol_table.lookup(node.name)
        node.symbol = symbol

    def visit_FieldSelection(self, node):
        """Resolves a field selection in a report."""
        symbol = self.symbol_table.lookup(node.name)
        node.symbol = symbol

    def visit_DefineFile(self, node):
        """Registers virtual fields from a DEFINE FILE block."""
        # For now, we define these in the current scope.
        # In a more complex implementation, we'd associate them with the specific MasterFile.
        for assignment in node.assignments:
            self.visit(assignment)

    def visit_DefineAssignment(self, node):
        """Registers a single virtual field definition."""
        self.symbol_table.define(node.name, symbol_type='VIRTUAL_FIELD', metadata={'definition': node})
        self.visit(node.expression)

    def visit_ComputeCommand(self, node):
        """Registers a COMPUTE field definition within a report request."""
        self.symbol_table.define(node.name, symbol_type='VIRTUAL_FIELD', metadata={'compute': node})
        self.visit(node.expression)
