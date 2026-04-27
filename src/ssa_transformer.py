import ir
from dominators import DominatorAnalysis

class SSATransformer:
    """
    Handles Transformation of a ControlFlowGraph into Static Single Assignment (SSA) form.
    """
    def __init__(self):
        pass

    def place_phi_nodes(self, cfg):
        """
        Inserts Phi instructions into the basic blocks of the CFG using the
        iterative dominance frontier algorithm.
        """
        # 1. Compute dominators and frontiers if not already present or just always run for safety
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
                # For each block m in the dominance frontier of n
                for m_name in frontiers.get(n_name, []):
                    if m_name not in phi_inserted_in:
                        m_block = cfg.blocks[m_name]

                        # Phi nodes must be at the beginning of the block.
                        # We use the variable name itself as the source for now;
                        # Renaming will replace these with versioned names.
                        phi = ir.Phi(target=var, sources=[var] * len(m_block.predecessors))
                        m_block.instructions.insert(0, phi)

                        phi_inserted_in.add(m_name)
                        if m_name not in added_to_worklist:
                            added_to_worklist.add(m_name)
                            worklist.append(m_name)

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
        # Note: In the future, other instructions like Define or Compute might be handled here
        # if they are lowered or if we want to include them in SSA.
        return None
