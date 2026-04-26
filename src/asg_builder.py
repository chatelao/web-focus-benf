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

    def visitDm_set(self, ctx: WebFocusReportParser.Dm_setContext):
        variable = ctx.amper_var().getText()
        expression = self.visit(ctx.dm_expression())
        return SetDM(variable=variable, expression=expression)

    def visitDm_type(self, ctx: WebFocusReportParser.Dm_typeContext):
        messages = [child.getText() for child in ctx.dm_primary()]
        return TypeDM(messages=messages)

    def visitDm_expression(self, ctx: WebFocusReportParser.Dm_expressionContext):
        return self.visit(ctx.getChild(0))

    def visitDm_logical_expression(self, ctx: WebFocusReportParser.Dm_logical_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
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

    def visitDm_additive_expression(self, ctx: WebFocusReportParser.Dm_additive_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))
        return BinaryOperation(left=left, operator=operator, right=right)

    def visitDm_multiplicative_expression(self, ctx: WebFocusReportParser.Dm_multiplicative_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))
        return BinaryOperation(left=left, operator=operator, right=right)

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

    def visitAmper_var(self, ctx: WebFocusReportParser.Amper_varContext):
        return AmperVar(name=ctx.getText())
