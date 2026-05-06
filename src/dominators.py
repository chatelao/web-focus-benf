class DominatorAnalysis:
    """
    Computes immediate dominators and dominance frontiers for a ControlFlowGraph.
    """
    def __init__(self, cfg):
        self.cfg = cfg
        self.idoms = {}
        self.frontiers = {}
        self.dom_tree = {}
        self.post_order = []
        self.post_order_indices = {}

    def run(self):
        if not self.cfg.entry_block:
            return

        self._compute_post_order()
        self._compute_idoms()
        self._compute_dom_tree()
        self._compute_frontiers()

    def _compute_dom_tree(self):
        self.dom_tree = {name: [] for name in self.cfg.blocks}
        for node_name, idom_name in self.idoms.items():
            if node_name != idom_name:
                self.dom_tree[idom_name].append(node_name)

    def _compute_post_order(self):
        visited = set()
        self.post_order = []

        # Ensure entry_block is what we think it is.
        # If it has no predecessors but isn't marked as entry_block, we might have issues.
        # But IRBuilder sets it correctly.

        # Use an iterative approach to avoid recursion depth issues
        stack = [(self.cfg.entry_block, False)]
        while stack:
            block, visited_children = stack.pop()
            if not block: continue

            if visited_children:
                if block.name not in self.post_order: # Safeguard
                    self.post_order.append(block.name)
            else:
                if block.name not in visited:
                    visited.add(block.name)
                    stack.append((block, True))
                    # Push successors in reverse to maintain same order as recursive
                    for succ in reversed(block.successors):
                        if succ.name not in visited:
                            stack.append((succ, False))

        # Check if all blocks were reached. If not, maybe some blocks are only reachable via back-edges?
        # That shouldn't happen in a valid CFG starting from Entry.
        # But let's check.
        if len(self.post_order) < len(self.cfg.blocks):
             # Try to reach other blocks
             for name, block in self.cfg.blocks.items():
                 if name not in visited:
                      # This block is unreachable from entry!
                      pass

        for i, name in enumerate(self.post_order):
            self.post_order_indices[name] = i

    def _compute_idoms(self):
        entry_name = self.cfg.entry_block.name
        self.idoms = {entry_name: entry_name}

        # Reverse post-order (excluding entry)
        rpo = self.post_order[::-1]
        nodes = [name for name in rpo if name != entry_name]

        # Initialize idoms for other nodes
        for node_name in nodes:
            self.idoms[node_name] = None

        # Fixed point for idoms is tricky with back-edges if we don't start from a good initial guess
        # Actually, standard algorithm should work if we skip nodes with no idom yet.

        changed = True
        while changed:
            changed = False
            for node_name in nodes:
                node = self.cfg.blocks[node_name]

                # Find first predecessor that has an idom
                new_idom = None
                for pred in node.predecessors:
                    if self.idoms.get(pred.name) is not None:
                        new_idom = pred.name
                        break

                if new_idom:
                    for pred in node.predecessors:
                        if pred.name != new_idom and self.idoms.get(pred.name) is not None:
                            new_idom = self._intersect(pred.name, new_idom)

                    if self.idoms.get(node_name) != new_idom:
                        self.idoms[node_name] = new_idom
                        changed = True

    def _intersect(self, b1, b2):
        finger1 = b1
        finger2 = b2
        while finger1 != finger2:
            while self.post_order_indices[finger1] < self.post_order_indices[finger2]:
                finger1 = self.idoms[finger1]
            while self.post_order_indices[finger2] < self.post_order_indices[finger1]:
                finger2 = self.idoms[finger2]
        return finger1

    def _compute_frontiers(self):
        for block_name in self.cfg.blocks:
            self.frontiers[block_name] = set()

        for block_name, block in self.cfg.blocks.items():
            if block_name not in self.idoms:
                continue # Unreachable

            if len(block.predecessors) >= 2:
                for pred in block.predecessors:
                    if pred.name not in self.idoms:
                        continue
                    runner = pred.name
                    while runner != self.idoms[block_name]:
                        self.frontiers[runner].add(block_name)
                        runner = self.idoms[runner]
