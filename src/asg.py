class ASGNode:
    """Base class for all nodes in the Abstract Semantic Graph (ASG)."""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class Expression(ASGNode):
    """Base class for all expression nodes in the ASG."""
    pass

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
