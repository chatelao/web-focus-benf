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
        format = ctx.format_name().getText() if ctx.format_name() else None
        alias = self.visit(ctx.as_phrase()) if ctx.as_phrase() else None
        return FieldSelection(name=name, alias=alias, format=format)

    def visitAs_phrase(self, ctx: WebFocusReportParser.As_phraseContext):
        val = ctx.STRING().getText()
        return val[1:-1]

    def visitAsterisk(self, ctx: WebFocusReportParser.AsteriskContext):
        return FieldSelection(name='*')

    def visitBy_command(self, ctx: WebFocusReportParser.By_commandContext):
        sort_type = "BY"
        options = self.visit(ctx.sort_options()) if ctx.sort_options() else {}
        field = self.visit(ctx.field())
        summarize = self.visit(ctx.summarize_command()) if ctx.summarize_command() else None
        noprint = ctx.NOPRINT() is not None
        return SortCommand(sort_type=sort_type, field=field, options=options, summarize=summarize, noprint=noprint)

    def visitAcross_command(self, ctx: WebFocusReportParser.Across_commandContext):
        sort_type = "ACROSS"
        options = self.visit(ctx.sort_options()) if ctx.sort_options() else {}
        field = self.visit(ctx.field())
        noprint = ctx.NOPRINT() is not None
        return SortCommand(sort_type=sort_type, field=field, options=options, noprint=noprint)

    def visitWhere_command(self, ctx: WebFocusReportParser.Where_commandContext):
        is_total = ctx.TOTAL() is not None
        condition = self.visit(ctx.dm_logical_expression())
        return WhereClause(condition=condition, is_total=is_total)

    def visitHeading_command(self, ctx: WebFocusReportParser.Heading_commandContext):
        centered = ctx.CENTER() is not None
        text = " ".join([s.getText()[1:-1] for s in ctx.STRING()])
        return Heading(text=text, centered=centered)

    def visitFooting_command(self, ctx: WebFocusReportParser.Footing_commandContext):
        centered = ctx.CENTER() is not None
        text = " ".join([s.getText()[1:-1] for s in ctx.STRING()])
        return Footing(text=text, centered=centered)

    def visitOn_command(self, ctx: WebFocusReportParser.On_commandContext):
        if ctx.TABLE():
            target = "TABLE"
            actions = self.visit(ctx.on_table_options())
        else:
            target = ctx.qualified_name().getText()
            actions = self.visit(ctx.on_field_options())

        if not isinstance(actions, list):
            actions = [actions]
        return OnCommand(target=target, actions=actions)

    def visitOn_table_options(self, ctx: WebFocusReportParser.On_table_optionsContext):
        if ctx.SUBHEAD() or ctx.SUBFOOT():
            centered = ctx.CENTER() is not None
            text = " ".join([s.getText()[1:-1] for s in ctx.STRING()])
            return Subhead(text=text, centered=centered) if ctx.SUBHEAD() else Subfoot(text=text, centered=centered)
        if ctx.COLUMN_TOTAL_KW():
            return SetCommand(parameter="COLUMN-TOTAL", value="ON")
        if ctx.ROW_TOTAL_KW():
            return SetCommand(parameter="ROW-TOTAL", value="ON")
        if ctx.output_command():
            return self.visit(ctx.output_command())
        if ctx.summarize_command():
            return self.visit(ctx.summarize_command())
        if ctx.recap_command():
            return self.visit(ctx.recap_command())
        if ctx.set_command():
            return self.visit(ctx.set_command())
        return None

    def visitOn_field_options(self, ctx: WebFocusReportParser.On_field_optionsContext):
        if ctx.SUBHEAD() or ctx.SUBFOOT():
            centered = ctx.CENTER() is not None
            text = " ".join([s.getText()[1:-1] for s in ctx.STRING()])
            return Subhead(text=text, centered=centered) if ctx.SUBHEAD() else Subfoot(text=text, centered=centered)
        if ctx.summarize_command():
            return self.visit(ctx.summarize_command())
        if ctx.recap_command():
            return self.visit(ctx.recap_command())
        return None

    def visitOutput_command(self, ctx: WebFocusReportParser.Output_commandContext):
        output_type = ctx.getChild(0).getText().upper()
        filename = ctx.qualified_name().getText() if ctx.qualified_name() else None
        format = None
        if ctx.FORMAT():
            if ctx.NAME():
                format = ctx.NAME().getText()
            elif ctx.verb():
                format = ctx.verb().getText()
        return OutputCommand(output_type=output_type, filename=filename, format=format)

    def visitCompute_command(self, ctx: WebFocusReportParser.Compute_commandContext):
        name = ctx.qualified_name().getText()
        format = ctx.format_name().getText() if ctx.format_name() else None
        expression = self.visit(ctx.dm_expression())
        return ComputeCommand(name=name, format=format, expression=expression)

    def visitRecap_command(self, ctx: WebFocusReportParser.Recap_commandContext):
        assignments = [self.visit(a) for a in ctx.recap_assignment()]
        return RecapCommand(assignments=assignments)

    def visitRecap_assignment(self, ctx: WebFocusReportParser.Recap_assignmentContext):
        name = ctx.qualified_name().getText()

        # Check if '(' immediately follows qualified_name
        has_col_ref = ctx.getChild(1).getText() == '('
        column_ref = self.visit(ctx.dm_expression(0)) if has_col_ref else None

        # The main expression is the first dm_expression if no col_ref, or the second if col_ref exists.
        expr_idx = 1 if has_col_ref else 0
        expression = self.visit(ctx.dm_expression(expr_idx))

        format = ctx.format_name().getText() if ctx.format_name() else None

        alias = None
        indent = None
        noprint = False

        for opt in ctx.recap_option():
            res = self.visit(opt)
            if isinstance(res, str):
                alias = res
            elif isinstance(res, int):
                indent = res
            elif res is True:
                noprint = True

        return RecapAssignment(
            name=name,
            expression=expression,
            column_ref=column_ref,
            format=format,
            alias=alias,
            indent=indent,
            noprint=noprint
        )

    def visitRecap_option(self, ctx: WebFocusReportParser.Recap_optionContext):
        if ctx.as_phrase():
            return self.visit(ctx.as_phrase())
        if ctx.INDENT():
            return int(ctx.NUMBER().getText())
        if ctx.NOPRINT():
            return True
        return None

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
        messages = [self.visit(child) for child in ctx.dm_primary()]
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
            return self.visit(ctx.dm_concat_expression(0))

        # Case: MISSING
        if ctx.MISSING():
            expr = self.visit(ctx.dm_concat_expression(0))
            inverted = False
            if ctx.NE() or ctx.is_not_op():
                inverted = True
            return IsMissingExpression(expression=expr, inverted=inverted)

        # Case: FROM...TO
        if ctx.TO():
            expr = self.visit(ctx.dm_concat_expression(0))
            lower = self.visit(ctx.dm_concat_expression(1))
            upper = self.visit(ctx.dm_concat_expression(2))
            node = BetweenExpression(expression=expr, lower=lower, upper=upper)
            if ctx.not_from_op():
                return UnaryOperation(operator='NOT', operand=node)
            return node

        # Case: IN
        if ctx.IN():
            expr = self.visit(ctx.dm_concat_expression(0))
            if ctx.FILE():
                filename = ctx.qualified_name().getText()
                return InExpression(expression=expr, values=[], filename=filename)
            else:
                values = [self.visit(e) for i, e in enumerate(ctx.dm_concat_expression()) if i > 0]
                return InExpression(expression=expr, values=values)

        # Case: INCLUDES / EXCLUDES
        if ctx.INCLUDES() or ctx.EXCLUDES():
            left = self.visit(ctx.dm_concat_expression(0))
            op = "INCLUDES" if ctx.INCLUDES() else "EXCLUDES"
            values = [self.visit(e) for i, e in enumerate(ctx.dm_concat_expression()) if i > 0]
            return BinaryOperation(left=left, operator=op, right=values)

        # Case: Relational op with optional OR
        if ctx.dm_relational_op():
            left = self.visit(ctx.dm_concat_expression(0))
            op_text = ctx.dm_relational_op().getText().upper().replace('-', ' ')
            rights = [self.visit(e) for i, e in enumerate(ctx.dm_concat_expression()) if i > 0]

            node = BinaryOperation(left=left, operator=op_text, right=rights[0])
            for i in range(1, len(rights)):
                right_expr = BinaryOperation(left=left, operator=op_text, right=rights[i])
                node = BinaryOperation(left=node, operator="OR", right=right_expr)
            return node

        return self.visit(ctx.getChild(0))

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

    def visitDm_unary_expression(self, ctx: WebFocusReportParser.Dm_unary_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        operator = ctx.getChild(0).getText()
        operand = self.visit(ctx.getChild(1))
        return UnaryOperation(operator=operator, operand=operand)

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

    def visitJoin_command(self, ctx: WebFocusReportParser.Join_commandContext):
        if ctx.CLEAR():
            return JoinClear()

        left_field = ctx.qualified_name(0).getText()
        left_file = ctx.qualified_name(1).getText()
        right_field = ctx.qualified_name(2).getText()
        right_file = ctx.qualified_name(3).getText()
        join_as = ctx.NAME().getText() if ctx.NAME() else None
        outer = ctx.OUTER() is not None
        is_all = ctx.ALL() is not None

        return Join(
            left_file=left_file,
            left_field=left_field,
            right_file=right_file,
            right_field=right_field,
            join_as=join_as,
            outer=outer,
            is_all=is_all
        )

    def visitDefine_file(self, ctx: WebFocusReportParser.Define_fileContext):
        filename = ctx.qualified_name().getText()
        assignments = [self.visit(a) for a in ctx.define_assignment()]
        return DefineFile(filename=filename, assignments=assignments)

    def visitDefine_assignment(self, ctx: WebFocusReportParser.Define_assignmentContext):
        name = ctx.qualified_name().getText()
        format = ctx.format_name().getText() if ctx.format_name() else None
        expression = self.visit(ctx.dm_expression())
        return DefineAssignment(name=name, expression=expression, format=format)

    def visitSummarize_command(self, ctx: WebFocusReportParser.Summarize_commandContext):
        verb = ctx.getChild(0).getText().upper()
        options = self.visit(ctx.summarize_options()) if ctx.summarize_options() else {}

        field_node = self.visit(ctx.field()) if ctx.field() else None
        field_name = field_node.name if field_node else None
        alias = field_node.alias if field_node else None

        # If there's an explicit as_phrase in the summarize_command, it overrides
        if ctx.as_phrase():
            alias = self.visit(ctx.as_phrase())

        return SummarizeCommand(verb=verb, field=field_name, alias=alias, options=options)

    def visitSummarize_options(self, ctx: WebFocusReportParser.Summarize_optionsContext):
        options = {}
        if ctx.ROLL_DOT():
            options["roll"] = True

        prefixes = [p.getText().upper() for p in ctx.prefix_operator()]
        if prefixes:
            options["prefixes"] = prefixes
        return options

    def visitSet_command(self, ctx: WebFocusReportParser.Set_commandContext):
        parameter = ctx.hyphenated_name().getText()
        value = None
        if ctx.set_value():
            value = ctx.set_value().getText()
        return SetCommand(parameter=parameter, value=value)

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
