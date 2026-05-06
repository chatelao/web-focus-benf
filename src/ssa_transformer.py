import ir
import asg
import copy
from dominators import DominatorAnalysis

class SSATransformer:
    """
    Handles Transformation of a ControlFlowGraph into Static Single Assignment (SSA) form.
    """
    def __init__(self):
        pass

    def transform(self, cfg):
        """
        Performs full SSA transformation: Phi placement and variable renaming.
        """
        self.place_phi_nodes(cfg)
        self.rename_variables(cfg)

    def place_phi_nodes(self, cfg):
        """
        Inserts Phi instructions into the basic blocks of the CFG using the
        iterative dominance frontier algorithm.
        """
        # 0. Ensure entry block is set
        if not cfg.entry_block and cfg.blocks:
            cfg.entry_block = next(iter(cfg.blocks.values()))

        # 1. Compute dominators and frontiers
        analysis = DominatorAnalysis(cfg)
        analysis.run()
        frontiers = analysis.frontiers

        # 2. Discovery: Find all variables and which blocks they are defined in
        variables = self._get_all_variables(cfg)
        defining_blocks = self._get_defining_blocks(cfg, variables)

        # 3. Iterative placement
        for var in variables:
            phi_inserted_in = set()
            added_to_worklist = set(defining_blocks[var])
            worklist = list(defining_blocks[var])

            while worklist:
                n_name = worklist.pop(0)
                for m_name in frontiers.get(n_name, []):
                    if m_name not in phi_inserted_in:
                        m_block = cfg.blocks[m_name]
                        # Phi nodes must be at the beginning of the block.
                        phi = ir.Phi(target=var, sources=[var] * len(m_block.predecessors))
                        # Store the original variable name for renaming pass
                        phi.original_var = var
                        m_block.instructions.insert(0, phi)

                        phi_inserted_in.add(m_name)
                        if m_name not in added_to_worklist:
                            added_to_worklist.add(m_name)
                            worklist.append(m_name)

    def rename_variables(self, cfg):
        """
        Renames variables to ensure each is assigned exactly once.
        """
        analysis = DominatorAnalysis(cfg)
        analysis.run()
        dom_tree = analysis.dom_tree

        variables = self._get_all_variables(cfg)
        stacks = {var: [] for var in variables}
        counters = {var: 0 for var in variables}

        def get_current_name(var):
            if var in stacks and stacks[var]:
                return stacks[var][-1]
            return f"{var}_0"

        def generate_new_name(var):
            name = f"{var}_{counters[var]}"
            counters[var] += 1
            stacks[var].append(name)
            return name

        def rename(block_name):
            block = cfg.blocks[block_name]
            pushed_vars = []

            # 1. Rename uses and definitions in ordinary instructions
            for instr in block.instructions:
                if not isinstance(instr, ir.Phi):
                    self._rename_uses(instr, stacks)

                target = self._get_target_variable(instr)
                if target:
                    original_target = target
                    if isinstance(instr, ir.Phi):
                        original_target = getattr(instr, 'original_var', target)

                    new_name = generate_new_name(original_target)
                    instr.target = new_name
                    pushed_vars.append(original_target)

            # 2. Fill in Phi node parameters in successors
            for succ in block.successors:
                try:
                    pred_index = succ.predecessors.index(block)
                except ValueError:
                    continue # Should not happen in a valid CFG

                for instr in succ.instructions:
                    if isinstance(instr, ir.Phi):
                        orig_var = getattr(instr, 'original_var', None)
                        if orig_var:
                            instr.sources[pred_index] = get_current_name(orig_var)

            # 3. Recurse on children in dominator tree
            for child_name in dom_tree.get(block_name, []):
                rename(child_name)

            # 4. Pop stacks
            for var in pushed_vars:
                stacks[var].pop()

        if cfg.entry_block:
            rename(cfg.entry_block.name)

    def _get_all_variables(self, cfg):
        """Identifies all variables assigned in any block of the CFG."""
        variables = set()
        for block in cfg.blocks.values():
            for instr in block.instructions:
                target = self._get_target_variable(instr)
                if target:
                    variables.add(target)
        return variables

    def _get_defining_blocks(self, cfg, variables):
        """Maps each variable to a set of block names where it is assigned."""
        def_blocks = {var: set() for var in variables}
        for block_name, block in cfg.blocks.items():
            for instr in block.instructions:
                target = self._get_target_variable(instr)
                if target and target in def_blocks:
                    def_blocks[target].add(block_name)
        return def_blocks

    def _get_target_variable(self, instr):
        """Helper to extract the target variable name from an instruction."""
        class_name = instr.__class__.__name__
        if class_name in ('Assign', 'Phi'):
            if isinstance(instr.target, str):
                return instr.target
            if hasattr(instr.target, 'name'):
                return instr.target.name
        return None

    def _rename_uses(self, instr, stacks):
        """Renames variable uses in an instruction based on current stacks."""
        if isinstance(instr, ir.Assign):
            instr.source = self._rename_in_expr(instr.source, stacks)
        elif isinstance(instr, ir.Branch):
            instr.condition = self._rename_in_expr(instr.condition, stacks)
        elif isinstance(instr, ir.Type):
            instr.messages = [self._rename_in_expr(m, stacks) for m in instr.messages]
        elif isinstance(instr, ir.Report):
            for comp in instr.components:
                self._rename_asg_node_recursive(comp, stacks)
        elif isinstance(instr, ir.Define):
            for assign in instr.assignments:
                self._rename_asg_node_recursive(assign, stacks)
        elif isinstance(instr, ir.Call):
            instr.arguments = [self._rename_in_expr(arg, stacks) for arg in instr.arguments]
        # Phi uses are handled separately during predecessor processing

    def _rename_asg_node_recursive(self, node, stacks):
        """Recursively renames variable references in ASG nodes."""
        if node is None:
            return

        # Handle nodes that have conditions (WhereClause, IfDM, etc.)
        if hasattr(node, 'condition'):
            node.condition = self._rename_in_expr(node.condition, stacks)

        # Handle nodes that have expressions (ComputeCommand, DefineAssignment, etc.)
        if hasattr(node, 'expression'):
            node.expression = self._rename_in_expr(node.expression, stacks)

        # Handle nodes that have sub-actions (OnCommand)
        if hasattr(node, 'actions'):
            for action in node.actions:
                self._rename_asg_node_recursive(action, stacks)

        # Handle nodes that have sub-components (ReportRequest - though usually it is in ir.Report)
        if hasattr(node, 'components'):
            for comp in node.components:
                self._rename_asg_node_recursive(comp, stacks)

    def _rename_in_expr(self, expr, stacks):
        """Recursively renames variable references in an expression."""
        if expr is None:
            return None

        if isinstance(expr, (asg.AmperVar, asg.Identifier)):
            if expr.name in stacks:
                new_expr = copy.copy(expr)
                if stacks[expr.name]:
                    new_expr.name = stacks[expr.name][-1]
                else:
                    new_expr.name = f"{expr.name}_0"
                return new_expr
            return expr

        if isinstance(expr, asg.BinaryOperation):
            new_expr = copy.copy(expr)
            new_expr.left = self._rename_in_expr(expr.left, stacks)
            new_expr.right = self._rename_in_expr(expr.right, stacks)
            return new_expr

        if isinstance(expr, asg.UnaryOperation):
            new_expr = copy.copy(expr)
            new_expr.operand = self._rename_in_expr(expr.operand, stacks)
            return new_expr

        if isinstance(expr, asg.FunctionCall):
            new_expr = copy.copy(expr)
            new_expr.arguments = [self._rename_in_expr(arg, stacks) for arg in expr.arguments]
            return new_expr

        if isinstance(expr, asg.IfExpression):
            new_expr = copy.copy(expr)
            new_expr.condition = self._rename_in_expr(expr.condition, stacks)
            new_expr.then_expr = self._rename_in_expr(expr.then_expr, stacks)
            new_expr.else_expr = self._rename_in_expr(expr.else_expr, stacks)
            return new_expr

        return expr
