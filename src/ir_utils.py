import ir
import asg

def get_base_name(name):
    """
    Strips numeric version suffixes from SSA-renamed variables.
    Example: &X_1 -> &X
    """
    if '_' in name:
        parts = name.split('_')
        if parts[-1].isdigit():
            return "_".join(parts[:-1])
    return name

def find_simple_for_loop(cfg, header_name):
    """
    Identifies if a block is the header of a simple REPEAT...TIMES or REPEAT...FOR loop.
    """
    if not header_name.startswith('LOOP_HEADER_'):
        return None

    label = header_name[len('LOOP_HEADER_'):]
    header_block = cfg.blocks.get(header_name)
    if not header_block:
        return None

    # In SSA, header might have a Phi node followed by the Branch.
    branch_instr = None
    for instr in header_block.instructions:
        if isinstance(instr, ir.Branch):
            branch_instr = instr
            break

    if not branch_instr:
        return None

    # condition should be counter <= limit
    cond = branch_instr.condition
    if not (isinstance(cond, asg.BinaryOperation) and cond.operator == 'LE'):
        return None

    if not isinstance(cond.left, asg.AmperVar):
        return None

    counter_var = cond.left.name
    counter_base = get_base_name(counter_var)
    limit = cond.right

    body_start = branch_instr.true_target
    after_block = branch_instr.false_target

    # Find the closing label block
    closing_block = cfg.blocks.get(label)
    if not closing_block:
        return None

    # Verify closing block ends with increment and jump to header
    if len(closing_block.instructions) < 2:
        return None

    last_instr = closing_block.instructions[-1]
    inc_instr = closing_block.instructions[-2]

    if not (isinstance(last_instr, ir.Jump) and last_instr.target == header_name):
        return None

    if not isinstance(inc_instr, ir.Assign):
        return None

    target_name = inc_instr.target if isinstance(inc_instr.target, str) else inc_instr.target.name
    if get_base_name(target_name) != counter_base:
        return None

    # Extract step from increment: counter = counter + step
    if not (isinstance(inc_instr.source, asg.BinaryOperation) and inc_instr.source.operator == '+'):
        return None

    step = inc_instr.source.right

    # Verify body is a linear sequence of blocks leading to the closing block
    body_blocks = []
    curr = body_start
    visited = {header_name, after_block}
    while curr != label:
        if curr in visited:
            return None
        visited.add(curr)
        body_blocks.append(curr)

        b = cfg.blocks.get(curr)
        if not b or len(b.successors) != 1:
            return None
        curr = b.successors[0].name

    # Find start value
    start_val = asg.Literal(value=1) # Default for TIMES
    if not counter_base.startswith('&REPEAT_COUNTER_'):
        # Find the predecessor block that is not the back-edge
        preds = [p for p in header_block.predecessors if p.name != label]
        if len(preds) == 1:
            pred = preds[0]
            # Look for assignment in the last few instructions
            for i in reversed(range(len(pred.instructions))):
                item = pred.instructions[i]
                if isinstance(item, ir.Assign):
                    target = item.target if isinstance(item.target, str) else item.target.name
                    if get_base_name(target) == counter_base:
                        start_val = item.source
                        break

    return {
        'type': 'FOR',
        'counter': counter_var,
        'start': start_val,
        'limit': limit,
        'step': step,
        'body_blocks': body_blocks,
        'closing_block': label,
        'after_block': after_block
    }

def find_simple_while_loop(cfg, header_name):
    """
    Identifies if a block is the header of a simple REPEAT...WHILE or REPEAT...UNTIL loop.
    """
    if not header_name.startswith('LOOP_HEADER_'):
        return None

    label = header_name[len('LOOP_HEADER_'):]
    header_block = cfg.blocks.get(header_name)
    if not header_block:
        return None

    branch_instr = None
    for instr in header_block.instructions:
        if isinstance(instr, ir.Branch):
            branch_instr = instr
            break

    if not branch_instr:
        return None

    cond = branch_instr.condition
    body_start = branch_instr.true_target
    after_block = branch_instr.false_target

    # Find the closing label block
    closing_block = cfg.blocks.get(label)
    if not closing_block:
        return None

    # Verify closing block ends with jump to header
    if not closing_block.instructions:
        return None

    last_instr = closing_block.instructions[-1]
    if not (isinstance(last_instr, ir.Jump) and last_instr.target == header_name):
        return None

    # Verify body is a linear sequence of blocks leading to the closing block
    body_blocks = []
    curr = body_start
    visited = {header_name, after_block}
    while curr != label:
        if curr in visited:
            return None
        visited.add(curr)
        body_blocks.append(curr)

        b = cfg.blocks.get(curr)
        if not b or len(b.successors) != 1:
            return None
        curr = b.successors[0].name

    return {
        'type': 'WHILE',
        'condition': cond,
        'body_blocks': body_blocks,
        'closing_block': label,
        'after_block': after_block
    }
