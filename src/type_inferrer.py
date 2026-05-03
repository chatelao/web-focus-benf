from asg import *

class TypeInferrer:
    """
    Traverses the Abstract Semantic Graph (ASG) to infer and propagate data types.
    Sets a 'data_type' attribute on expression nodes.
    """
    def infer(self, nodes):
        """Main entry point for inferring types in a list of ASG nodes or a single node."""
        if isinstance(nodes, list):
            for node in nodes:
                self.visit(node)
        else:
            self.visit(nodes)
        return nodes

    def visit(self, node):
        """Dispatches to specific visit methods based on node type."""
        if node is None or not isinstance(node, ASGNode):
            return None

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
        return None

    def _get_base_type(self, format_str):
        """Extracts the base type or normalized format string from a WebFOCUS format string."""
        if not format_str:
            return None
        return format_str.upper()

    def visit_Literal(self, node):
        if isinstance(node.value, int):
            node.data_type = 'I'
        elif isinstance(node.value, float):
            node.data_type = 'F'
        elif isinstance(node.value, str):
            node.data_type = 'A'
        else:
            node.data_type = None
        return node.data_type

    def visit_Identifier(self, node):
        if hasattr(node, 'symbol') and node.symbol:
            metadata = node.symbol.metadata
            if 'field' in metadata:
                node.data_type = self._get_base_type(metadata['field'].format)
            elif 'definition' in metadata:
                # VIRTUAL_FIELD from DefineFile
                node.data_type = self._get_base_type(metadata['definition'].format)
                if not node.data_type:
                    node.data_type = self.visit(metadata['definition'].expression)
            elif 'define' in metadata:
                # VIRTUAL_FIELD from MasterFile segment
                node.data_type = self._get_base_type(metadata['define'].format)
            elif 'compute' in metadata:
                # VIRTUAL_FIELD from ComputeCommand
                node.data_type = self._get_base_type(metadata['compute'].format)
                if not node.data_type:
                    node.data_type = self.visit(metadata['compute'].expression)
        else:
            node.data_type = None
        return node.data_type

    def visit_FieldSelection(self, node):
        node.data_type = None
        if hasattr(node, 'symbol') and node.symbol:
            metadata = node.symbol.metadata
            if 'field' in metadata:
                node.data_type = self._get_base_type(metadata['field'].format)
            elif 'define' in metadata:
                node.data_type = self._get_base_type(metadata['define'].format)
            elif 'compute' in metadata:
                node.data_type = self._get_base_type(metadata['compute'].format)
            elif 'definition' in metadata:
                # Procedural DEFINE
                node.data_type = self._get_base_type(metadata['definition'].format)
                if not node.data_type:
                    node.data_type = self.visit(metadata['definition'].expression)
        return node.data_type

    def visit_AmperVar(self, node):
        # Dialogue Manager variables are typically strings in WebFOCUS unless used in arithmetic
        node.data_type = 'A'
        return node.data_type

    def _pick_precise_type(self, type1, type2, category_prefix):
        """Helper to pick the more specific/precise type between two format strings."""
        t1 = type1 if type1 and type1.startswith(category_prefix) else None
        t2 = type2 if type2 and type2.startswith(category_prefix) else None

        if not t1: return t2
        if not t2: return t1

        # Pick the one with more information (longer string usually means precision/scale)
        return t1 if len(t1) >= len(t2) else t2

    def visit_BinaryOperation(self, node):
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)

        op = node.operator.upper()
        if op in ('+', '-', '*', '/'):
            if any(t and t.startswith(('F', 'D', 'P')) for t in (left_type, right_type)):
                # If either is float-like, result is float-like.
                node.data_type = self._pick_precise_type(left_type, right_type, ('F', 'D', 'P')) or 'F'
            elif any(t and t.startswith('I') for t in (left_type, right_type)):
                # If both are integer-like, pick the largest
                node.data_type = self._pick_precise_type(left_type, right_type, 'I') or 'I'
            else:
                node.data_type = left_type or right_type
        elif op in ('|', '||', 'CONCAT'):
            node.data_type = 'A'
        elif op in ('AND', 'OR', 'EQ', 'NE', 'GT', 'GE', 'LT', 'LE', 'CONTAINS', 'LIKE', 'OMITS', 'INCLUDES', 'EXCLUDES', 'IS'):
            node.data_type = 'LOGICAL'
        else:
            node.data_type = None

        return node.data_type

    def visit_UnaryOperation(self, node):
        operand_type = self.visit(node.operand)
        op = node.operator.upper()
        if op == 'NOT':
            node.data_type = 'LOGICAL'
        else:
            node.data_type = operand_type
        return node.data_type

    def visit_IfExpression(self, node):
        self.visit(node.condition)
        then_type = self.visit(node.then_expr)
        else_type = self.visit(node.else_expr)

        if any(t and t.startswith(('F', 'D', 'P')) for t in (then_type, else_type)):
            node.data_type = self._pick_precise_type(then_type, else_type, ('F', 'D', 'P')) or 'F'
        elif any(t and t.startswith('I') for t in (then_type, else_type)):
            node.data_type = self._pick_precise_type(then_type, else_type, 'I') or 'I'
        else:
            node.data_type = then_type or else_type

        return node.data_type

    def visit_FunctionCall(self, node):
        for arg in node.arguments:
            self.visit(arg)

        # Simple heuristics for built-in functions
        name = node.function_name.upper()
        if name in ('ABS', 'INT', 'MAX', 'MIN', 'SQRT'):
            # These usually return the type of their arguments (or F for SQRT)
            if name == 'SQRT':
                node.data_type = 'F'
            elif node.arguments:
                # Use the type of the first argument as a proxy
                node.data_type = getattr(node.arguments[0], 'data_type', 'F')
            else:
                node.data_type = 'F'
        elif name in ('UPCASE', 'LOWCASE', 'SUBSTR', 'TRIM'):
            node.data_type = 'A'
        else:
            # Default to F for unknown functions
            node.data_type = 'F'
        return node.data_type

    def visit_InExpression(self, node):
        self.visit(node.expression)
        for val in node.values:
            self.visit(val)
        node.data_type = 'LOGICAL'
        return node.data_type

    def visit_BetweenExpression(self, node):
        self.visit(node.expression)
        self.visit(node.lower)
        self.visit(node.upper)
        node.data_type = 'LOGICAL'
        return node.data_type

    def visit_IsMissingExpression(self, node):
        self.visit(node.expression)
        node.data_type = 'LOGICAL'
        return node.data_type
