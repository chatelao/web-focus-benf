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
