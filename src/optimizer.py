import ir
import asg
import copy
from ir_utils import find_simple_for_loop, find_simple_while_loop

class RelationalLiftingOptimizer:
    """
    Identifies procedural loops that can be lifted to relational operations.
    """
    def find_data_loops(self, cfg):
        """
        Identifies loops in the CFG that contain -READ instructions.
        Returns a list of loop metadata dictionaries.
        """
        data_loops = []
        for b_name in cfg.blocks:
            loop = find_simple_for_loop(cfg, b_name)
            if not loop:
                loop = find_simple_while_loop(cfg, b_name)

            if loop:
                if self._contains_read(cfg, loop):
                    data_loops.append(loop)
        return data_loops

    def _contains_read(self, cfg, loop):
        """Checks if any block in the loop body contains an ir.Read instruction."""
        # Check body blocks
        for b_name in loop['body_blocks']:
            block = cfg.blocks.get(b_name)
            if block:
                for instr in block.instructions:
                    if isinstance(instr, ir.Read):
                        return True

        # Check closing block (minus terminal jump/increment)
        closing_block = cfg.blocks.get(loop['closing_block'])
        if closing_block:
            end_offset = 2 if loop['type'] == 'FOR' else 1
            for instr in closing_block.instructions[:-end_offset]:
                if isinstance(instr, ir.Read):
                    return True
        return False

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
            if isinstance(instr.target, str):
                return instr.target
            if hasattr(instr.target, 'name'):
                return instr.target.name
        return None

    def _get_constant_value(self, instr):
        """Determines if an instruction assigns a constant value."""
        if isinstance(instr, ir.Assign):
            return self._evaluate_constant(instr.source)

        if isinstance(instr, ir.Phi):
            if not instr.sources:
                return None

            first_val = self._evaluate_constant(asg.AmperVar(name=instr.sources[0]))
            if first_val is None:
                return None

            for source in instr.sources[1:]:
                val = self._evaluate_constant(asg.AmperVar(name=source))
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
            op = expr.operator.upper()
            left = self._evaluate_constant(expr.left)

            # Short-circuiting for AND/OR
            if op == 'AND' and left is not None and not left.value:
                return asg.Literal(value=False)
            if op == 'OR' and left is not None and left.value:
                return asg.Literal(value=True)

            right = self._evaluate_constant(expr.right)

            # Short-circuiting for AND/OR (right side)
            if op == 'AND' and right is not None and not right.value:
                return asg.Literal(value=False)
            if op == 'OR' and right is not None and right.value:
                return asg.Literal(value=True)

            if left and right:
                try:
                    res = None
                    if op == '+': res = left.value + right.value
                    elif op == '-': res = left.value - right.value
                    elif op == '*': res = left.value * right.value
                    elif op == '/': res = left.value / right.value
                    elif op in ('EQ', '='): res = left.value == right.value
                    elif op in ('NE', '!='): res = left.value != right.value
                    elif op in ('LT', '<'): res = left.value < right.value
                    elif op in ('GT', '>'): res = left.value > right.value
                    elif op in ('LE', '<='): res = left.value <= right.value
                    elif op in ('GE', '>='): res = left.value >= right.value
                    elif op in ('||', '|', 'CONCAT'):
                        res = str(left.value) + str(right.value)
                    elif op == 'AND': res = left.value and right.value
                    elif op == 'OR': res = left.value or right.value

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

class DeadCodeEliminator:
    """
    Removes unreachable blocks and unused assignments from a CFG.
    """
    def run(self, cfg):
        changed = True
        while changed:
            changed = False
            if self._remove_unreachable_blocks(cfg):
                changed = True
            if self._remove_unused_assignments(cfg):
                changed = True
        return cfg

    def _remove_unreachable_blocks(self, cfg):
        if not cfg.entry_block:
            return False

        reachable = set()
        worklist = [cfg.entry_block.name]
        while worklist:
            name = worklist.pop()
            if name not in reachable:
                reachable.add(name)
                block = cfg.blocks[name]
                for succ in block.successors:
                    worklist.append(succ.name)

        unreachable = set(cfg.blocks.keys()) - reachable
        if not unreachable:
            return False

        for name in unreachable:
            block = cfg.blocks[name]
            # Remove this block from its successors' predecessors
            for succ in block.successors:
                if block in succ.predecessors:
                    succ.predecessors.remove(block)
            del cfg.blocks[name]

        return True

    def _remove_unused_assignments(self, cfg):
        live_vars = set()

        # 1. Fixed-point iteration to find all live variables
        changed = True
        while changed:
            changed = False
            for block in cfg.blocks.values():
                for instr in block.instructions:
                    # Side-effecting instructions or those defining already live vars make their operands live
                    target = self._get_target_variable(instr)
                    if self._is_essential(instr) or (target is not None and target in live_vars):
                        old_size = len(live_vars)
                        self._add_usages(instr, live_vars)
                        if len(live_vars) > old_size:
                            changed = True

        # 2. Remove instructions that are not essential and don't define a live variable
        removed_any = False
        for block in cfg.blocks.values():
            new_instrs = []
            for instr in block.instructions:
                target = self._get_target_variable(instr)
                if target is not None:
                    if target in live_vars:
                        new_instrs.append(instr)
                    else:
                        removed_any = True
                else:
                    # Essential instructions (Type, Call, Report, etc.) or control flow (Jump, Branch)
                    new_instrs.append(instr)
            block.instructions = new_instrs

        return removed_any

    def _is_essential(self, instr):
        """Instructions with side effects are essential."""
        return isinstance(instr, (ir.Type, ir.Call, ir.SetEnv, ir.Define, ir.Report, ir.Branch, ir.Jump))

    def _get_target_variable(self, instr):
        """Extracts the target variable name from an instruction."""
        if isinstance(instr, (ir.Assign, ir.Phi)):
            if isinstance(instr.target, str):
                return instr.target
            if hasattr(instr.target, 'name'):
                return instr.target.name
        return None

    def _add_usages(self, instr, live_vars):
        if isinstance(instr, ir.Assign):
            self._collect_vars(instr.source, live_vars)
        elif isinstance(instr, ir.Phi):
            for src in instr.sources:
                live_vars.add(src)
        elif isinstance(instr, ir.Branch):
            self._collect_vars(instr.condition, live_vars)
        elif isinstance(instr, ir.Type):
            for msg in instr.messages:
                self._collect_vars(msg, live_vars)
        elif isinstance(instr, ir.Call):
            for arg in instr.arguments:
                self._collect_vars(arg, live_vars)
        elif isinstance(instr, ir.Report):
            for comp in instr.components:
                self._collect_vars_recursive(comp, live_vars)
        elif isinstance(instr, ir.Define):
            for assign in instr.assignments:
                self._collect_vars_recursive(assign, live_vars)

    def _collect_vars(self, expr, live_vars):
        if isinstance(expr, (asg.AmperVar, asg.Identifier)):
            live_vars.add(expr.name)
        elif isinstance(expr, asg.BinaryOperation):
            self._collect_vars(expr.left, live_vars)
            self._collect_vars(expr.right, live_vars)
        elif isinstance(expr, asg.UnaryOperation):
            self._collect_vars(expr.operand, live_vars)
        elif isinstance(expr, asg.FunctionCall):
            for arg in expr.arguments:
                self._collect_vars(arg, live_vars)
        elif isinstance(expr, asg.IfExpression):
            self._collect_vars(expr.condition, live_vars)
            self._collect_vars(expr.then_expr, live_vars)
            self._collect_vars(expr.else_expr, live_vars)

    def _collect_vars_recursive(self, node, live_vars):
        if node is None:
            return
        if hasattr(node, 'condition'):
            self._collect_vars(node.condition, live_vars)
        if hasattr(node, 'expression'):
            self._collect_vars(node.expression, live_vars)
        if hasattr(node, 'actions'):
            for action in node.actions:
                self._collect_vars_recursive(action, live_vars)
        if hasattr(node, 'components'):
            for comp in node.components:
                self._collect_vars_recursive(comp, live_vars)
