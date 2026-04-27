import ir
import asg
import copy

class ConstantPropagator:
    """
    Performs constant propagation and constant folding on a CFG in SSA form.
    """
    def __init__(self):
        self.constants = {} # var_name -> Literal node

    def run(self, cfg):
        """
        Runs the constant propagation pass on the given CFG.
        """
        # We might need multiple passes if constants propagate through multiple assignments
        changed = True
        iteration = 0
        while changed:
            iteration += 1
            if iteration > 100: # Safety break
                break
            changed = False

            # Pass 1: Identify constants
            for block in cfg.blocks.values():
                for instr in block.instructions:
                    target = self._get_target_variable(instr)
                    if not target:
                        continue

                    const_val = self._get_constant_value(instr)
                    if const_val is not None:
                        if target not in self.constants or self.constants[target].value != const_val.value:
                            self.constants[target] = const_val
                            changed = True

            # Pass 2: Substitute constants
            for block in cfg.blocks.values():
                for instr in block.instructions:
                    if self._substitute_constants(instr):
                        changed = True

        return cfg

    def _get_target_variable(self, instr):
        """Extracts the target variable name from an instruction."""
        if isinstance(instr, (ir.Assign, ir.Phi)):
            return instr.target
        return None

    def _get_constant_value(self, instr):
        """Determines if an instruction assigns a constant value."""
        if isinstance(instr, ir.Assign):
            return self._evaluate_constant(instr.source)

        if isinstance(instr, ir.Phi):
            if not instr.sources:
                return None

            first_val = self._evaluate_constant(asg.AmperVar(instr.sources[0]))
            if first_val is None:
                return None

            for source in instr.sources[1:]:
                val = self._evaluate_constant(asg.AmperVar(source))
                if val is None or val.value != first_val.value:
                    return None
            return first_val

        return None

    def _evaluate_constant(self, expr):
        """Recursively evaluates an expression to a constant Literal if possible."""
        if isinstance(expr, asg.Literal):
            return expr

        if isinstance(expr, (asg.AmperVar, asg.Identifier)):
            return self.constants.get(expr.name)

        if isinstance(expr, asg.BinaryOperation):
            left = self._evaluate_constant(expr.left)
            right = self._evaluate_constant(expr.right)
            if left and right:
                try:
                    res = None
                    if expr.operator == '+': res = left.value + right.value
                    elif expr.operator == '-': res = left.value - right.value
                    elif expr.operator == '*': res = left.value * right.value
                    elif expr.operator == '/': res = left.value / right.value
                    elif expr.operator == 'EQ' or expr.operator == '=': res = left.value == right.value
                    elif expr.operator == 'NE' or expr.operator == '!=': res = left.value != right.value
                    elif expr.operator == 'LT' or expr.operator == '<': res = left.value < right.value
                    elif expr.operator == 'GT' or expr.operator == '>': res = left.value > right.value
                    elif expr.operator == 'LE' or expr.operator == '<=': res = left.value <= right.value
                    elif expr.operator == 'GE' or expr.operator == '>=': res = left.value >= right.value

                    if res is not None:
                        return asg.Literal(value=res)
                except:
                    pass

        if isinstance(expr, asg.UnaryOperation):
            operand = self._evaluate_constant(expr.operand)
            if operand:
                try:
                    if expr.operator == '-': return asg.Literal(value=-operand.value)
                    if expr.operator == '+': return operand
                    if expr.operator == 'NOT': return asg.Literal(value=not operand.value)
                except:
                    pass

        return None

    def _substitute_constants(self, instr):
        """Substitutes variable uses with constants in an instruction."""
        changed = False
        if isinstance(instr, ir.Assign):
            # Check if the entire expression can be folded to a literal
            folded = self._evaluate_constant(instr.source)
            if folded:
                if not isinstance(instr.source, asg.Literal) or instr.source.value != folded.value:
                    instr.source = folded
                    return True

            new_source = self._substitute_in_expr(instr.source)
            if new_source != instr.source:
                instr.source = new_source
                changed = True
        elif isinstance(instr, ir.Branch):
            folded = self._evaluate_constant(instr.condition)
            if folded:
                if not isinstance(instr.condition, asg.Literal) or instr.condition.value != folded.value:
                    instr.condition = folded
                    return True
            new_cond = self._substitute_in_expr(instr.condition)
            if new_cond != instr.condition:
                instr.condition = new_cond
                changed = True
        elif isinstance(instr, ir.Type):
            new_msgs = [self._substitute_in_expr(m) for m in instr.messages]
            if new_msgs != instr.messages:
                instr.messages = new_msgs
                changed = True
        elif isinstance(instr, ir.Report):
            for comp in instr.components:
                if self._substitute_recursive_asg(comp):
                    changed = True
        elif isinstance(instr, ir.Define):
            for assign in instr.assignments:
                if self._substitute_recursive_asg(assign):
                    changed = True
        elif isinstance(instr, ir.Call):
            new_args = [self._substitute_in_expr(arg) for arg in instr.arguments]
            if new_args != instr.arguments:
                instr.arguments = new_args
                changed = True
        # Phi nodes sources are variable names (strings), we don't substitute them directly
        # but _get_constant_value will use self.constants to identify constant Phis.
        return changed

    def _substitute_in_expr(self, expr):
        """Recursively substitutes constants in an expression."""
        if expr is None:
            return None

        if isinstance(expr, (asg.AmperVar, asg.Identifier)):
            const = self.constants.get(expr.name)
            return copy.deepcopy(const) if const else expr

        if isinstance(expr, asg.BinaryOperation):
            new_left = self._substitute_in_expr(expr.left)
            new_right = self._substitute_in_expr(expr.right)
            if new_left != expr.left or new_right != expr.right:
                new_expr = copy.copy(expr)
                new_expr.left = new_left
                new_expr.right = new_right
                return new_expr
            return expr

        if isinstance(expr, asg.UnaryOperation):
            new_operand = self._substitute_in_expr(expr.operand)
            if new_operand != expr.operand:
                new_expr = copy.copy(expr)
                new_expr.operand = new_operand
                return new_expr
            return expr

        if isinstance(expr, asg.FunctionCall):
            new_args = [self._substitute_in_expr(arg) for arg in expr.arguments]
            if new_args != expr.arguments:
                new_expr = copy.copy(expr)
                new_expr.arguments = new_args
                return new_expr
            return expr

        if isinstance(expr, asg.IfExpression):
            new_cond = self._substitute_in_expr(expr.condition)
            new_then = self._substitute_in_expr(expr.then_expr)
            new_else = self._substitute_in_expr(expr.else_expr)
            if new_cond != expr.condition or new_then != expr.then_expr or new_else != expr.else_expr:
                new_expr = copy.copy(expr)
                new_expr.condition = new_cond
                new_expr.then_expr = new_then
                new_expr.else_expr = new_else
                return new_expr
            return expr

        return expr

    def _substitute_recursive_asg(self, node):
        """Recursively substitutes constants in complex ASG nodes."""
        if node is None:
            return False

        changed = False
        if hasattr(node, 'condition'):
            new_cond = self._substitute_in_expr(node.condition)
            if new_cond != node.condition:
                node.condition = new_cond
                changed = True

        if hasattr(node, 'expression'):
            new_expr = self._substitute_in_expr(node.expression)
            if new_expr != node.expression:
                node.expression = new_expr
                changed = True

        if hasattr(node, 'actions'):
            for action in node.actions:
                if self._substitute_recursive_asg(action):
                    changed = True

        if hasattr(node, 'components'):
            for comp in node.components:
                if self._substitute_recursive_asg(comp):
                    changed = True

        return changed
