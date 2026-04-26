from antlr4 import TerminalNode
from WebFocusReportVisitor import WebFocusReportVisitor
from WebFocusReportParser import WebFocusReportParser
from asg import *

class ReportASGBuilder(WebFocusReportVisitor):
    """
    Transforms a WebFocusReport parse tree into an Abstract Semantic Graph (ASG).
    """

    def visitStart(self, ctx: WebFocusReportParser.StartContext):
        nodes = []
        if ctx.children:
            for child in ctx.children:
                if isinstance(child, TerminalNode):
                    continue
                node = self.visit(child)
                if node:
                    if isinstance(node, list):
                        nodes.extend(node)
                    else:
                        nodes.append(node)
        return nodes

    def visitRequest(self, ctx: WebFocusReportParser.RequestContext):
        filename = self.visit(ctx.table_file())
        components = []
        # Iterate through all children except table_file (first) and end_command (last)
        for i in range(1, ctx.getChildCount() - 1):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                continue
            node = self.visit(child)
            if node:
                if isinstance(node, list):
                    components.extend(node)
                else:
                    components.append(node)
        return ReportRequest(filename=filename, components=components)

    def visitTable_file(self, ctx: WebFocusReportParser.Table_fileContext):
        return ctx.qualified_name().getText()

    def visitVerb_command(self, ctx: WebFocusReportParser.Verb_commandContext):
        verb = self.visit(ctx.verb())
        if ctx.field_list():
            fields = self.visit(ctx.field_list())
        else:
            fields = [self.visit(ctx.asterisk())]
        return VerbCommand(verb=verb, fields=fields)

    def visitVerb(self, ctx: WebFocusReportParser.VerbContext):
        return ctx.getText().upper()

    def visitField_list(self, ctx: WebFocusReportParser.Field_listContext):
        return [self.visit(f) for f in ctx.field_or_prefixed()]

    def visitField_or_prefixed(self, ctx: WebFocusReportParser.Field_or_prefixedContext):
        prefixes = [p.getText().upper() for p in ctx.prefix_operator()]
        field_selection = self.visit(ctx.field())
        field_selection.prefix_operators = prefixes
        return field_selection

    def visitField(self, ctx: WebFocusReportParser.FieldContext):
        name = ctx.qualified_name().getText()
        alias = self.visit(ctx.as_phrase()) if ctx.as_phrase() else None
        return FieldSelection(name=name, alias=alias)

    def visitAs_phrase(self, ctx: WebFocusReportParser.As_phraseContext):
        val = ctx.STRING().getText()
        return val[1:-1]

    def visitAsterisk(self, ctx: WebFocusReportParser.AsteriskContext):
        return FieldSelection(name='*')

    def visitBy_command(self, ctx: WebFocusReportParser.By_commandContext):
        sort_type = "BY"
        options = self.visit(ctx.sort_options()) if ctx.sort_options() else {}
        field = self.visit(ctx.field())
        # Note: summarize_command and NOPRINT are not yet fully implemented in ASG
        return SortCommand(sort_type=sort_type, field=field, options=options)

    def visitAcross_command(self, ctx: WebFocusReportParser.Across_commandContext):
        sort_type = "ACROSS"
        options = self.visit(ctx.sort_options()) if ctx.sort_options() else {}
        field = self.visit(ctx.field())
        return SortCommand(sort_type=sort_type, field=field, options=options)

    def visitSort_options(self, ctx: WebFocusReportParser.Sort_optionsContext):
        options = {}
        if ctx.HIGHEST(): options["order"] = "HIGHEST"
        if ctx.LOWEST(): options["order"] = "LOWEST"
        if ctx.TOP(): options["order"] = "TOP"
        if ctx.BOTTOM(): options["order"] = "BOTTOM"
        if ctx.NUMBER():
            options["limit"] = int(ctx.NUMBER().getText())
        return options

    def visitDm_set(self, ctx: WebFocusReportParser.Dm_setContext):
        variable = ctx.amper_var().getText()
        expression = self.visit(ctx.dm_expression())
        return SetDM(variable=variable, expression=expression)

    def visitDm_type(self, ctx: WebFocusReportParser.Dm_typeContext):
        messages = [child.getText() for child in ctx.dm_primary()]
        return TypeDM(messages=messages)

    def visitDm_expression(self, ctx: WebFocusReportParser.Dm_expressionContext):
        return self.visit(ctx.getChild(0))

    def visitDm_if_expression(self, ctx: WebFocusReportParser.Dm_if_expressionContext):
        if ctx.IF():
            condition = self.visit(ctx.dm_logical_expression())
            then_expr = self.visit(ctx.dm_expression(0))
            else_expr = self.visit(ctx.dm_expression(1))
            return IfExpression(condition=condition, then_expr=then_expr, else_expr=else_expr)
        return self.visit(ctx.getChild(0))

    def visitDm_logical_expression(self, ctx: WebFocusReportParser.Dm_logical_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        if ctx.getChild(0).getText() == '(':
            return self.visit(ctx.dm_logical_expression(0))
        if ctx.getChildCount() == 2: # NOT case
            operator = ctx.getChild(0).getText().upper()
            operand = self.visit(ctx.getChild(1))
            return UnaryOperation(operator=operator, operand=operand)
        # Handle binary logical operations (AND, OR)
        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText().upper()
        right = self.visit(ctx.getChild(2))
        return BinaryOperation(left=left, operator=operator, right=right)

    def visitDm_relational_expression(self, ctx: WebFocusReportParser.Dm_relational_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText().upper()
        right = self.visit(ctx.getChild(2))
        return BinaryOperation(left=left, operator=operator, right=right)

    def visitDm_concat_expression(self, ctx: WebFocusReportParser.Dm_concat_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        # ANTLR4 creates a flat structure for (CONCAT dm_additive_expression)*
        # We'll transform it into a left-associative tree
        left = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            operator = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i+1))
            left = BinaryOperation(left=left, operator=operator, right=right)
        return left

    def visitDm_additive_expression(self, ctx: WebFocusReportParser.Dm_additive_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            operator = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i+1))
            left = BinaryOperation(left=left, operator=operator, right=right)
        return left

    def visitDm_multiplicative_expression(self, ctx: WebFocusReportParser.Dm_multiplicative_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            operator = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i+1))
            left = BinaryOperation(left=left, operator=operator, right=right)
        return left

    def visitDm_primary(self, ctx: WebFocusReportParser.Dm_primaryContext):
        if ctx.STRING():
            val = ctx.STRING().getText()
            # Remove quotes
            return Literal(value=val[1:-1])
        if ctx.NUMBER():
            return Literal(value=int(ctx.NUMBER().getText()))
        if ctx.dm_float():
            return Literal(value=float(ctx.dm_float().getText()))
        if ctx.amper_var():
            return self.visit(ctx.amper_var())
        if ctx.qualified_name():
            if ctx.getChildCount() > 1 and ctx.getChild(1).getText() == '(':
                # Function call
                name = ctx.qualified_name().getText()
                args = []
                if ctx.dm_expression():
                    args = [self.visit(expr) for expr in ctx.dm_expression()]
                return FunctionCall(function_name=name, arguments=args)
            else:
                return Identifier(name=ctx.qualified_name().getText())
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))
        return None

    def visitDm_command(self, ctx: WebFocusReportParser.Dm_commandContext):
        return self.visit(ctx.getChild(0))

    def visitDm_goto(self, ctx: WebFocusReportParser.Dm_gotoContext):
        target = ctx.NAME().getText()
        return Goto(target=target)

    def visitDm_label(self, ctx: WebFocusReportParser.Dm_labelContext):
        name = ctx.LABEL_DM().getText()[1:] # Strip leading '-'
        return Label(name=name)

    def visitDm_if(self, ctx: WebFocusReportParser.Dm_ifContext):
        condition = self.visit(ctx.dm_logical_expression())
        then_target = ctx.NAME(0).getText()
        else_target = ctx.NAME(1).getText() if ctx.NAME(1) else None
        return IfDM(condition=condition, then_target=then_target, else_target=else_target)

    def visitDm_include(self, ctx: WebFocusReportParser.Dm_includeContext):
        filename = ctx.qualified_name().getText()
        return IncludeDM(filename=filename)

    def visitDm_run(self, ctx: WebFocusReportParser.Dm_runContext):
        return RunDM()

    def visitDm_exit(self, ctx: WebFocusReportParser.Dm_exitContext):
        return ExitDM()

    def visitDm_repeat(self, ctx: WebFocusReportParser.Dm_repeatContext):
        label = ctx.NAME().getText()
        kwargs = {"label": label}
        if ctx.WHILE():
            kwargs["condition"] = self.visit(ctx.dm_logical_expression())
            kwargs["condition_type"] = "WHILE"
        elif ctx.UNTIL():
            kwargs["condition"] = self.visit(ctx.dm_logical_expression())
            kwargs["condition_type"] = "UNTIL"
        elif ctx.TIMES():
            kwargs["times"] = self.visit(ctx.dm_primary(0))
        elif ctx.FOR():
            kwargs["loop_var"] = ctx.amper_var().getText()
            kwargs["start_val"] = self.visit(ctx.dm_primary(0))
            kwargs["end_val"] = self.visit(ctx.dm_primary(1))
            if ctx.STEP():
                kwargs["step_val"] = self.visit(ctx.dm_primary(2))
        return Repeat(**kwargs)

    def visitAmper_var(self, ctx: WebFocusReportParser.Amper_varContext):
        return AmperVar(name=ctx.getText())
