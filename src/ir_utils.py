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
        'header_block': header_name,
        'counter': counter_var,
        'start': start_val,
        'limit': limit,
        'step': step,
        'body_blocks': body_blocks,
        'closing_block': label,
        'after_block': after_block
    }

def collect_fields_from_component(node, mark_field_used, used_files=None):
    """
    Recursively collects field references from report components.
    """
    if node is None: return
    class_name = node.__class__.__name__

    if class_name == 'VerbCommand':
        for f in node.fields:
            if f.name == '*':
                # If PRINT * is used, we must keep all files
                if used_files is not None:
                    used_files.add('*')
            else:
                mark_field_used(f.name)
    elif class_name == 'SortCommand':
        mark_field_used(node.field.name)
    elif class_name == 'ComputeCommand':
        collect_fields_from_expression(node.expression, mark_field_used)
    elif class_name == 'WhereClause':
        collect_fields_from_expression(node.condition, mark_field_used)
    elif class_name == 'WhenCommand':
        collect_fields_from_expression(node.condition, mark_field_used)
    elif class_name == 'OnCommand':
        for action in node.actions:
            collect_fields_from_component(action, mark_field_used, used_files)

def collect_fields_from_expression(expr, mark_field_used, source_fn=None):
    """
    Recursively collects field references from ASG expressions.
    """
    if expr is None: return
    class_name = expr.__class__.__name__

    if class_name == 'Identifier':
        mark_field_used(expr.name, source_fn)
    elif class_name == 'BinaryOperation':
        collect_fields_from_expression(expr.left, mark_field_used, source_fn)
        collect_fields_from_expression(expr.right, mark_field_used, source_fn)
    elif class_name == 'UnaryOperation':
        collect_fields_from_expression(expr.operand, mark_field_used, source_fn)
    elif class_name == 'FunctionCall':
        for arg in expr.arguments:
            collect_fields_from_expression(arg, mark_field_used, source_fn)
    elif class_name == 'IfExpression':
        collect_fields_from_expression(expr.condition, mark_field_used, source_fn)
        collect_fields_from_expression(expr.then_expr, mark_field_used, source_fn)
        collect_fields_from_expression(expr.else_expr, mark_field_used, source_fn)
    elif class_name == 'BetweenExpression':
        collect_fields_from_expression(expr.expression, mark_field_used, source_fn)
        collect_fields_from_expression(expr.lower, mark_field_used, source_fn)
        collect_fields_from_expression(expr.upper, mark_field_used, source_fn)
    elif class_name == 'InExpression':
        collect_fields_from_expression(expr.expression, mark_field_used, source_fn)
        for val in expr.values:
            collect_fields_from_expression(val, mark_field_used, source_fn)
    elif class_name == 'IsMissingExpression':
        collect_fields_from_expression(expr.expression, mark_field_used, source_fn)

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

    # Verify body is a sequence of blocks leading to the closing block
    body_blocks = []
    worklist = [body_start]
    visited = {header_name, after_block}
    while worklist:
        curr = worklist.pop(0)
        if curr == label or curr in visited:
            continue
        visited.add(curr)
        body_blocks.append(curr)

        b = cfg.blocks.get(curr)
        if not b: return None
        for succ in b.successors:
            worklist.append(succ.name)

    return {
        'type': 'WHILE',
        'header_block': header_name,
        'condition': cond,
        'body_blocks': body_blocks,
        'closing_block': label,
        'after_block': after_block
    }
