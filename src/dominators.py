class DominatorAnalysis:
    """
    Computes immediate dominators and dominance frontiers for a ControlFlowGraph.
    """
    def __init__(self, cfg):
        self.cfg = cfg
        self.idoms = {}
        self.frontiers = {}
        self.post_order = []
        self.post_order_indices = {}

    def run(self):
        if not self.cfg.entry_block:
            return

        self._compute_post_order()
        self._compute_idoms()
        self._compute_frontiers()

    def _compute_post_order(self):
        visited = set()
        self.post_order = []

        def walk(block):
            visited.add(block.name)
            for succ in block.successors:
                if succ.name not in visited:
                    walk(succ)
            self.post_order.append(block.name)

        walk(self.cfg.entry_block)

        for i, name in enumerate(self.post_order):
            self.post_order_indices[name] = i

    def _compute_idoms(self):
        entry_name = self.cfg.entry_block.name
        self.idoms = {entry_name: entry_name}

        # Reverse post-order (excluding entry)
        rpo = self.post_order[::-1]
        nodes = [name for name in rpo if name != entry_name]

        changed = True
        while changed:
            changed = False
            for node_name in nodes:
                node = self.cfg.blocks[node_name]

                # Find first predecessor that has an idom
                new_idom = None
                for pred in node.predecessors:
                    if pred.name in self.idoms:
                        new_idom = pred.name
                        break

                if new_idom:
                    for pred in node.predecessors:
                        if pred.name != new_idom and pred.name in self.idoms:
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
