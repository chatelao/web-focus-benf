class ASGNode:
    """Base class for all nodes in the Abstract Semantic Graph (ASG)."""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class Expression(ASGNode):
    """Base class for all expression nodes in the ASG."""
    pass

class Literal(Expression):
    """Represents a literal value (number, string, etc.)."""
    def __init__(self, value, **kwargs):
        super().__init__(value=value, **kwargs)

class Identifier(Expression):
    """Represents a field or variable name."""
    def __init__(self, name, **kwargs):
        super().__init__(name=name, **kwargs)

class AmperVar(Expression):
    """Represents a Dialogue Manager variable (e.g., &VAR)."""
    def __init__(self, name, **kwargs):
        super().__init__(name=name, **kwargs)

class BinaryOperation(Expression):
    """Represents a binary operation (e.g., a + b, a AND b)."""
    def __init__(self, left, operator, right, **kwargs):
        super().__init__(left=left, operator=operator, right=right, **kwargs)

class UnaryOperation(Expression):
    """Represents a unary operation (e.g., -a, NOT a)."""
    def __init__(self, operator, operand, **kwargs):
        super().__init__(operator=operator, operand=operand, **kwargs)

class FunctionCall(Expression):
    """Represents a function call (e.g., ABS(field))."""
    def __init__(self, function_name, arguments=None, **kwargs):
        super().__init__(function_name=function_name, arguments=arguments or [], **kwargs)

class IfExpression(Expression):
    """Represents an inline IF expression (IF condition THEN expr1 ELSE expr2)."""
    def __init__(self, condition, then_expr, else_expr, **kwargs):
        super().__init__(condition=condition, then_expr=then_expr, else_expr=else_expr, **kwargs)

class BetweenExpression(Expression):
    """Represents a BETWEEN or FROM...TO expression."""
    def __init__(self, expression, lower, upper, **kwargs):
        super().__init__(expression=expression, lower=lower, upper=upper, **kwargs)

class InExpression(Expression):
    """Represents an IN expression (e.g., field IN (val1, val2))."""
    def __init__(self, expression, values, **kwargs):
        super().__init__(expression=expression, values=values, **kwargs)

class Statement(ASGNode):
    """Base class for all statement nodes in the ASG."""
    pass

class Command(ASGNode):
    """Base class for all command nodes in the ASG."""
    pass

class Goto(Command):
    """Represents a Dialogue Manager -GOTO command."""
    def __init__(self, target, **kwargs):
        super().__init__(target=target, **kwargs)

class Label(Command):
    """Represents a Dialogue Manager label."""
    def __init__(self, name, **kwargs):
        super().__init__(name=name, **kwargs)

class IfDM(Command):
    """Represents a Dialogue Manager -IF command."""
    def __init__(self, condition, then_target, else_target=None, **kwargs):
        super().__init__(condition=condition, then_target=then_target, else_target=else_target, **kwargs)

class Repeat(Command):
    """Represents a Dialogue Manager -REPEAT command."""
    def __init__(self, label, **kwargs):
        super().__init__(label=label, **kwargs)

class SetDM(Command):
    """Represents a Dialogue Manager -SET command."""
    def __init__(self, variable, expression, **kwargs):
        super().__init__(variable=variable, expression=expression, **kwargs)

class TypeDM(Command):
    """Represents a Dialogue Manager -TYPE command."""
    def __init__(self, messages=None, **kwargs):
        super().__init__(messages=messages or [], **kwargs)

class IncludeDM(Command):
    """Represents a Dialogue Manager -INCLUDE command."""
    def __init__(self, filename, **kwargs):
        super().__init__(filename=filename, **kwargs)

class RunDM(Command):
    """Represents a Dialogue Manager -RUN command."""
    pass

class ExitDM(Command):
    """Represents a Dialogue Manager -EXIT command."""
    pass

class ReportRequest(Statement):
    """Represents a TABLE FILE report request."""
    def __init__(self, filename, components=None, **kwargs):
        super().__init__(filename=filename, components=components or [], **kwargs)

class VerbCommand(Command):
    """Represents a report verb command (PRINT, SUM, etc.)."""
    def __init__(self, verb, fields=None, **kwargs):
        super().__init__(verb=verb, fields=fields or [], **kwargs)

class FieldSelection(ASGNode):
    """Represents a field selection in a verb or sort command."""
    def __init__(self, name, prefix_operators=None, alias=None, **kwargs):
        super().__init__(name=name, prefix_operators=prefix_operators or [], alias=alias, **kwargs)

class SortCommand(Command):
    """Represents a sort phrase (BY or ACROSS)."""
    def __init__(self, sort_type, field, options=None, **kwargs):
        super().__init__(sort_type=sort_type, field=field, options=options or {}, **kwargs)

class WhereClause(Command):
    """Represents a WHERE clause in a report request."""
    def __init__(self, condition, is_total=False, **kwargs):
        super().__init__(condition=condition, is_total=is_total, **kwargs)

class Heading(Command):
    """Represents a HEADING command."""
    def __init__(self, text, centered=False, **kwargs):
        super().__init__(text=text, centered=centered, **kwargs)

class Footing(Command):
    """Represents a FOOTING command."""
    def __init__(self, text, centered=False, **kwargs):
        super().__init__(text=text, centered=centered, **kwargs)

class OnCommand(Command):
    """Represents an ON command (ON TABLE or ON field)."""
    def __init__(self, target, actions=None, **kwargs):
        super().__init__(target=target, actions=actions or [], **kwargs)

class ComputeCommand(Command):
    """Represents a COMPUTE command."""
    def __init__(self, name, expression, format=None, **kwargs):
        super().__init__(name=name, expression=expression, format=format, **kwargs)

class Join(Command):
    """Represents a JOIN command."""
    def __init__(self, left_file, left_field, right_file, right_field, join_as=None, outer=False, **kwargs):
        super().__init__(left_file=left_file, left_field=left_field, right_file=right_file, right_field=right_field, join_as=join_as, outer=outer, **kwargs)

class SetCommand(Command):
    """Represents a SET (non-Dialogue Manager) command."""
    def __init__(self, parameter, value, **kwargs):
        super().__init__(parameter=parameter, value=value, **kwargs)

class DefineFile(Statement):
    """Represents a DEFINE FILE block."""
    def __init__(self, filename, assignments=None, **kwargs):
        super().__init__(filename=filename, assignments=assignments or [], **kwargs)

class DataModelNode(ASGNode):
    """Base class for nodes related to the data model (Master Files)."""
    pass

class MasterFile(DataModelNode):
    """Represents a WebFOCUS Master File (metadata)."""
    def __init__(self, name, suffix=None, **kwargs):
        super().__init__(name=name, suffix=suffix, segments=[], **kwargs)

class Segment(DataModelNode):
    """Represents a segment within a Master File."""
    def __init__(self, name, segtype=None, parent=None, **kwargs):
        super().__init__(name=name, segtype=segtype, parent=parent, fields=[], **kwargs)

class Field(DataModelNode):
    """Represents a field within a segment."""
    def __init__(self, name, alias=None, format=None, **kwargs):
        super().__init__(name=name, alias=alias, format=format, **kwargs)
