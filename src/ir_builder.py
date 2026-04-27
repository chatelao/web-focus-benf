import ir
import asg

class IRBuilder:
    """
    Constructs a Control Flow Graph (CFG) from an Abstract Semantic Graph (ASG).
    """
    def __init__(self):
        self.cfg = ir.ControlFlowGraph()
        self.block_count = 0
        self.current_block = None
        self.labels = {} # label_name -> block_name

    def _new_block(self, name=None):
        if not name:
            name = f"B{self.block_count}"
            self.block_count += 1
        block = ir.BasicBlock(name=name)
        self.cfg.add_block(block)
        return block

    def build(self, asg_nodes):
        # Pass 1: Identify all labels and create blocks for them
        for node in asg_nodes:
            # Debug: print(f"Node: {type(node)}")
            if node.__class__.__name__ == 'Label':
                if node.name not in self.labels:
                    block = self._new_block(node.name)
                    self.labels[node.name] = block.name

        # Pass 2: Build instructions and edges
        self.current_block = self._new_block("ENTRY")

        for node in asg_nodes:
            class_name = node.__class__.__name__
            if class_name == 'Label':
                target_block_name = self.labels[node.name]
                target_block = self.cfg.blocks[target_block_name]

                # Fallthrough from current block to label block
                if self.current_block and self.current_block != target_block:
                    # Check if the last instruction was a jump. If so, no fallthrough.
                    has_jump = False
                    if self.current_block.instructions:
                        if self.current_block.instructions[-1].__class__.__name__ == 'Jump':
                            has_jump = True

                    if not has_jump:
                        self.cfg.add_edge(self.current_block.name, target_block.name)

                self.current_block = target_block

            elif class_name == 'Goto':
                target_label = node.target
                self.current_block.add_instruction(ir.Jump(target=target_label))

                # Add edge to the target block if it exists
                if target_label in self.labels:
                    self.cfg.add_edge(self.current_block.name, self.labels[target_label])

                # Subsequent instructions go to a new anonymous block
                self.current_block = self._new_block()

            elif class_name == 'SetDM':
                self.current_block.add_instruction(ir.Assign(target=node.variable, source=node.expression))
            elif class_name == 'TypeDM':
                self.current_block.add_instruction(ir.Type(messages=node.messages))
            elif class_name == 'IncludeDM':
                self.current_block.add_instruction(ir.Call(target=node.filename))
            elif class_name == 'SetCommand':
                self.current_block.add_instruction(ir.SetEnv(parameter=node.parameter, value=node.value))
            elif class_name == 'Join':
                args = [node.left_file, node.left_field, node.right_file, node.right_field]
                self.current_block.add_instruction(ir.Call(target='JOIN', arguments=args))
            elif class_name == 'DefineFile':
                self.current_block.add_instruction(ir.Define(filename=node.filename, assignments=node.assignments))
            elif class_name == 'ReportRequest':
                self.current_block.add_instruction(ir.Report(filename=node.filename, components=node.components))
            elif class_name == 'JoinClear':
                self.current_block.add_instruction(ir.Call(target='JOIN CLEAR'))
            elif class_name == 'RunDM':
                self.current_block.add_instruction(ir.Call(target='-RUN'))
            elif class_name == 'ExitDM':
                self.current_block.add_instruction(ir.Jump(target='EXIT'))
                # No edge to 'EXIT' yet unless we define an EXIT block.
                self.current_block = self._new_block()

        return self.cfg
