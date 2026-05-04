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
        self.active_loops = [] # stack of {label, header_block, after_block, repeat_node}
        self.active_joins = []

    def _new_block(self, name=None):
        if not name:
            name = f"B{self.block_count}"
            self.block_count += 1
        block = ir.BasicBlock(name=name)
        self.cfg.add_block(block)
        return block

    def _discover_labels(self, nodes):
        for node in nodes:
            class_name = node.__class__.__name__
            if class_name == 'Label':
                if node.name not in self.labels:
                    block = self._new_block(node.name)
                    self.labels[node.name] = block.name
            elif class_name == 'CompoundLayout':
                self._discover_labels(node.components)

    def build(self, asg_nodes):
        # Pass 1: Identify all labels
        self._discover_labels(asg_nodes)

        # Pass 2: Build instructions and edges
        self.current_block = self._new_block("ENTRY")
        self._process_nodes(asg_nodes)
        return self.cfg

    def _process_nodes(self, nodes):
        for node in nodes:
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

                # Check if this label closes an active loop
                if self.active_loops and self.active_loops[-1]['label'] == node.name:
                    matching_loop = self.active_loops.pop()
                    loop_node = matching_loop['repeat_node']
                    header_block = matching_loop['header_block']
                    after_block = matching_loop['after_block']

                    # Increment logic for TIMES/FOR
                    if loop_node.times:
                        counter_var = f"&REPEAT_COUNTER_{node.name}"
                        self.current_block.add_instruction(ir.Assign(
                            target=counter_var,
                            source=asg.BinaryOperation(asg.AmperVar(counter_var), "+", asg.Literal(1))
                        ))
                    elif loop_node.loop_var:
                        step = loop_node.step_val if loop_node.step_val else asg.Literal(1)
                        self.current_block.add_instruction(ir.Assign(
                            target=loop_node.loop_var,
                            source=asg.BinaryOperation(asg.AmperVar(loop_node.loop_var), "+", step)
                        ))

                    # Back-edge to header
                    self.current_block.add_instruction(ir.Jump(target=header_block.name))
                    self.cfg.add_edge(self.current_block.name, header_block.name)

                    # Next instructions go to the after block
                    self.current_block = after_block

            elif class_name == 'Goto':
                target_label = node.target
                self.current_block.add_instruction(ir.Jump(target=target_label))

                # Add edge to the target block if it exists
                if target_label in self.labels:
                    self.cfg.add_edge(self.current_block.name, self.labels[target_label])

                # Subsequent instructions go to a new anonymous block
                self.current_block = self._new_block()

            elif class_name == 'Repeat':
                header_block = self._new_block(f"LOOP_HEADER_{node.label}")
                body_block = self._new_block(f"LOOP_BODY_{node.label}")
                after_block = self._new_block(f"LOOP_AFTER_{node.label}")

                # Initialization
                if node.times:
                    counter_var = f"&REPEAT_COUNTER_{node.label}"
                    self.current_block.add_instruction(ir.Assign(target=counter_var, source=asg.Literal(1)))
                elif node.loop_var:
                    self.current_block.add_instruction(ir.Assign(target=node.loop_var, source=node.start_val))

                # Jump to header
                self.current_block.add_instruction(ir.Jump(target=header_block.name))
                self.cfg.add_edge(self.current_block.name, header_block.name)

                # Header condition
                condition = None
                if node.condition_type == "WHILE":
                    condition = node.condition
                elif node.condition_type == "UNTIL":
                    # UNTIL condition == WHILE NOT condition
                    condition = asg.UnaryOperation(operator="NOT", operand=node.condition)
                elif node.times:
                    counter_var = f"&REPEAT_COUNTER_{node.label}"
                    condition = asg.BinaryOperation(asg.AmperVar(counter_var), "LE", node.times)
                elif node.loop_var:
                    condition = asg.BinaryOperation(asg.AmperVar(node.loop_var), "LE", node.end_val)

                if condition:
                    header_block.add_instruction(ir.Branch(
                        condition=condition,
                        true_target=body_block.name,
                        false_target=after_block.name
                    ))
                    self.cfg.add_edge(header_block.name, body_block.name)
                    self.cfg.add_edge(header_block.name, after_block.name)
                else:
                    # Infinite loop or handled differently
                    header_block.add_instruction(ir.Jump(target=body_block.name))
                    self.cfg.add_edge(header_block.name, body_block.name)

                self.active_loops.append({
                    'label': node.label,
                    'header_block': header_block,
                    'after_block': after_block,
                    'repeat_node': node
                })
                self.current_block = body_block

            elif class_name == 'IfDM':
                true_label = node.then_target
                false_label = node.else_target

                if false_label:
                    self.current_block.add_instruction(ir.Branch(
                        condition=node.condition,
                        true_target=true_label,
                        false_target=false_label
                    ))
                    if true_label in self.labels:
                        self.cfg.add_edge(self.current_block.name, self.labels[true_label])
                    if false_label in self.labels:
                        self.cfg.add_edge(self.current_block.name, self.labels[false_label])
                    self.current_block = self._new_block()
                else:
                    fallthrough_block = self._new_block()
                    self.current_block.add_instruction(ir.Branch(
                        condition=node.condition,
                        true_target=true_label,
                        false_target=fallthrough_block.name
                    ))
                    if true_label in self.labels:
                        self.cfg.add_edge(self.current_block.name, self.labels[true_label])
                    self.cfg.add_edge(self.current_block.name, fallthrough_block.name)
                    self.current_block = fallthrough_block

            elif class_name == 'SetDM':
                self.current_block.add_instruction(ir.Assign(target=node.variable, source=node.expression))
            elif class_name == 'TypeDM':
                self.current_block.add_instruction(ir.Type(messages=node.messages))
            elif class_name == 'IncludeDM':
                self.current_block.add_instruction(ir.Call(target=node.filename))
            elif class_name == 'HtmlFormDM':
                self.current_block.add_instruction(ir.HtmlForm(filename=node.filename, content=node.content))
            elif class_name == 'ReadDM':
                self.current_block.add_instruction(ir.Read(filename=node.filename, variables=node.variables))
            elif class_name == 'WriteDM':
                self.current_block.add_instruction(ir.Write(filename=node.filename, messages=node.messages))
            elif class_name == 'DefaultDM':
                self.current_block.add_instruction(ir.Default(variable=node.variable, expression=node.expression))
            elif class_name == 'SetCommand':
                self.current_block.add_instruction(ir.SetEnv(parameter=node.parameter, value=node.value))
            elif class_name == 'Join':
                instr = ir.Join(
                    left_file=node.left_file,
                    left_field=node.left_field,
                    right_file=node.right_file,
                    right_field=node.right_field,
                    join_as=node.join_as,
                    outer=node.outer,
                    is_all=node.is_all
                )
                self.current_block.add_instruction(instr)
                self.active_joins.append(instr)
            elif class_name == 'DefineFile':
                self.current_block.add_instruction(ir.Define(filename=node.filename, assignments=node.assignments))
            elif class_name == 'ReportRequest':
                self.current_block.add_instruction(ir.Report(
                    filename=node.filename,
                    components=node.components,
                    joins=list(self.active_joins),
                    more_clause=node.more_clause
                ))
            elif class_name == 'MatchRequest':
                self.current_block.add_instruction(ir.Match(
                    filename=node.filename,
                    components=node.components,
                    sub_matches=node.sub_matches,
                    more_clause=node.more_clause
                ))
            elif class_name == 'JoinClear':
                self.current_block.add_instruction(ir.JoinClear())
                self.active_joins = []
            elif class_name == 'CompoundLayout':
                self.current_block.add_instruction(ir.CompoundLayout(
                    output_command=node.output_command,
                    statements=node.statements
                ))
                self._process_nodes(node.components)
                self.current_block.add_instruction(ir.CompoundEnd())
            elif class_name == 'RunDM':
                self.current_block.add_instruction(ir.Call(target='-RUN'))
            elif class_name == 'ExitDM':
                self.current_block.add_instruction(ir.Jump(target='EXIT'))
                # No edge to 'EXIT' yet unless we define an EXIT block.
                self.current_block = self._new_block()
