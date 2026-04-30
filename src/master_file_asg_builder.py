from MasterFileVisitor import MasterFileVisitor
from MasterFileParser import MasterFileParser
from asg import MasterFile, Segment, Field, DefineAssignment, Dimension, Hierarchy

class MasterFileASGBuilder(MasterFileVisitor):
    """
    Transforms a MasterFile parse tree into an Abstract Semantic Graph (ASG).
    """

    def __init__(self):
        self.master_file = None
        self.current_segment = None

    def visitStart(self, ctx: MasterFileParser.StartContext):
        if ctx.item():
            for item in ctx.item():
                self.visit(item)
        return self.master_file

    def visitFile_decl(self, ctx: MasterFileParser.File_declContext):
        name = self._get_value_text(ctx.value())
        attrs = self._get_attrs(ctx.attr_val())
        suffix = attrs.get("SUFFIX")

        # Handle positional suffix if not explicitly named
        if not suffix:
            positional_vals = [self._get_value_text(av.value()) for av in ctx.attr_val() if av.value()]
            if positional_vals:
                suffix = positional_vals[0]

        self.master_file = MasterFile(name=name, suffix=suffix, **attrs)
        return self.master_file

    def visitSegment_decl(self, ctx: MasterFileParser.Segment_declContext):
        name = self._get_value_text(ctx.value())
        attrs = self._get_attrs(ctx.attr_val())
        segtype = attrs.get("SEGTYPE")
        parent = attrs.get("PARENT")

        # Handle positional attributes
        positional_vals = [self._get_value_text(av.value()) for av in ctx.attr_val() if av.value()]
        if not segtype and len(positional_vals) > 0:
            segtype = positional_vals[0]
        if not parent and len(positional_vals) > 1:
            parent = positional_vals[1]

        segment = Segment(name=name, segtype=segtype, parent=parent, **attrs)
        if self.master_file:
            self.master_file.segments.append(segment)
        self.current_segment = segment
        return segment

    def visitField_decl(self, ctx: MasterFileParser.Field_declContext):
        name = self._get_value_text(ctx.value())
        attrs = self._get_attrs(ctx.attr_val())

        # Handle positional attributes if they are not explicitly named
        # Typical order: FIELDNAME, ALIAS, USAGE, [ACTUAL], $
        positional_vals = [self._get_value_text(av.value()) for av in ctx.attr_val() if av.value()]

        alias = attrs.get("ALIAS")
        usage = attrs.get("USAGE")

        if not alias and len(positional_vals) > 0:
            alias = positional_vals[0]
        if not usage and len(positional_vals) > 1:
            usage = positional_vals[1]

        field = Field(name=name, alias=alias, format=usage, **attrs)
        if self.current_segment:
            self.current_segment.fields.append(field)
        return field

    def visitDefine_decl(self, ctx: MasterFileParser.Define_declContext):
        nf = ctx.name_format()
        name_part = self._get_value_text(nf.value(0))
        if '/' in name_part:
            name, format = name_part.split('/', 1)
        else:
            name = name_part
            format = self._get_value_text(nf.value(1)) if len(nf.value()) > 1 else None

        expression_text = ctx.expression().getText()
        attrs = self._get_attrs(ctx.attr_val())

        assignment = DefineAssignment(name=name, expression=expression_text, format=format, **attrs)

        # Attach to segment or master file
        if self.current_segment:
            self.current_segment.virtual_fields.append(assignment)
        elif self.master_file:
            self.master_file.virtual_fields.append(assignment)

        return assignment

    def visitDimension_decl(self, ctx: MasterFileParser.Dimension_declContext):
        value = self._get_value_text(ctx.value())
        attrs = self._get_attrs(ctx.attr_val())
        dimension = Dimension(name=value, **attrs)
        if self.master_file:
            self.master_file.dimensions.append(dimension)
        return dimension

    def visitHierarchy_decl(self, ctx: MasterFileParser.Hierarchy_declContext):
        value = self._get_value_text(ctx.value())
        attrs = self._get_attrs(ctx.attr_val())
        hierarchy = Hierarchy(name=value, **attrs)
        if self.master_file:
            self.master_file.hierarchies.append(hierarchy)
        return hierarchy

    def visitOther_decl(self, ctx: MasterFileParser.Other_declContext):
        return None

    def _get_value_text(self, value_ctx):
        if not value_ctx:
            return None
        text = value_ctx.getText()
        if value_ctx.STRING():
            return text[1:-1]
        return text

    def _get_attrs(self, attr_vals):
        attrs = {}
        for av in attr_vals:
            if av.assignment():
                key = av.assignment().ATTR().getText().upper()
                val = self._get_value_text(av.assignment().value())
                attrs[key] = val
            elif av.value():
                # For non-assignments, we don't have a key here,
                # but they might be handled positionally by the caller.
                pass
        return attrs
