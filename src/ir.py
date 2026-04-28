class IRNode:
    """Base class for all Intermediate Representation (IR) nodes."""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class Instruction(IRNode):
    """Base class for instructions in the IR."""
    pass

class Label(Instruction):
    """Represents a label in the instruction stream."""
    def __init__(self, name, **kwargs):
        super().__init__(name=name, **kwargs)

class Assign(Instruction):
    """Represents an assignment: target = source."""
    def __init__(self, target, source, **kwargs):
        super().__init__(target=target, source=source, **kwargs)

class Jump(Instruction):
    """Represents an unconditional jump: goto target."""
    def __init__(self, target, **kwargs):
        super().__init__(target=target, **kwargs)

class Branch(Instruction):
    """Represents a conditional branch: if condition goto true_target else goto false_target."""
    def __init__(self, condition, true_target, false_target=None, **kwargs):
        super().__init__(condition=condition, true_target=true_target, false_target=false_target, **kwargs)

class Phi(Instruction):
    """Represents a Phi node in SSA form: target = Phi(v1, v2, ...)."""
    def __init__(self, target, sources, **kwargs):
        super().__init__(target=target, sources=sources or [], **kwargs)

class Type(Instruction):
    """Represents a -TYPE message."""
    def __init__(self, messages, **kwargs):
        super().__init__(messages=messages, **kwargs)

class Call(Instruction):
    """Represents a call to another procedure or an external action (JOIN, INCLUDE)."""
    def __init__(self, target, arguments=None, **kwargs):
        super().__init__(target=target, arguments=arguments or [], **kwargs)

class SetEnv(Instruction):
    """Represents an environment setting (SET parameter = value)."""
    def __init__(self, parameter, value, **kwargs):
        super().__init__(parameter=parameter, value=value, **kwargs)

class Join(Instruction):
    """Represents a JOIN command."""
    def __init__(self, left_file, left_field, right_file, right_field, join_as=None, outer=False, is_all=False, **kwargs):
        super().__init__(
            left_file=left_file,
            left_field=left_field,
            right_file=right_file,
            right_field=right_field,
            join_as=join_as,
            outer=outer,
            is_all=is_all,
            **kwargs
        )

class JoinClear(Instruction):
    """Represents a JOIN CLEAR * command."""
    pass

class Define(Instruction):
    """Represents a set of virtual field definitions (DEFINE FILE)."""
    def __init__(self, filename, assignments, **kwargs):
        super().__init__(filename=filename, assignments=assignments, **kwargs)

class Report(Instruction):
    """Represents a report request (TABLE FILE)."""
    def __init__(self, filename, components, joins=None, **kwargs):
        super().__init__(filename=filename, components=components, joins=joins or [], **kwargs)

class CompoundLayout(Instruction):
    """Represents the start of a COMPOUND LAYOUT block."""
    def __init__(self, output_command, statements=None, **kwargs):
        super().__init__(output_command=output_command, statements=statements or [], **kwargs)

class CompoundEnd(Instruction):
    """Represents the end of a COMPOUND LAYOUT block."""
    pass

class BasicBlock(IRNode):
    """Represents a basic block: a linear sequence of instructions."""
    def __init__(self, name, **kwargs):
        super().__init__(name=name, instructions=[], predecessors=[], successors=[], **kwargs)

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

class ControlFlowGraph(IRNode):
    """Represents a control flow graph (CFG)."""
    def __init__(self, **kwargs):
        super().__init__(blocks={}, entry_block=None, **kwargs)

    def add_block(self, block):
        self.blocks[block.name] = block
        if not self.entry_block:
            self.entry_block = block

    def add_edge(self, from_block_name, to_block_name):
        from_block = self.blocks[from_block_name]
        to_block = self.blocks[to_block_name]
        if to_block not in from_block.successors:
            from_block.successors.append(to_block)
        if from_block not in to_block.predecessors:
            to_block.predecessors.append(from_block)
