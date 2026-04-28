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

    def visitRequest_element(self, ctx: WebFocusReportParser.Request_elementContext):
        return self.visit(ctx.getChild(0))

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
        fs = FieldSelection(name=name, alias=alias)
        if format: fs.format = format
        return fs

    def visitAs_phrase(self, ctx: WebFocusReportParser.As_phraseContext):
        if ctx.STRING():
            val = ctx.STRING().getText()
            return val[1:-1]
        if ctx.identifier():
            return ctx.identifier().getText()
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        return None

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
        parts = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                txt = child.getText().upper()
                if txt in ['HEADING', 'FOOTING', 'CENTER']:
                    continue
            parts.append(child.getText())
        text = " ".join(parts).replace("'", "").replace('"', "")
        return Heading(text=text, centered=centered) if ctx.getChild(0).getText().upper() == 'HEADING' else Footing(text=text, centered=centered)

    def visitFooting_command(self, ctx: WebFocusReportParser.Footing_commandContext):
        centered = ctx.CENTER() is not None
        parts = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                txt = child.getText().upper()
                if txt in ['HEADING', 'FOOTING', 'CENTER']:
                    continue
            parts.append(child.getText())
        text = " ".join(parts).replace("'", "").replace('"', "")
        return Footing(text=text, centered=centered)

    def visitOn_command(self, ctx: WebFocusReportParser.On_commandContext):
        if ctx.TABLE():
             target = "TABLE"
        else:
             target = ctx.qualified_name().getText()

        actions = self.visit(ctx.on_options())

        if not isinstance(actions, list):
            actions = [actions]
        return OnCommand(target=target, actions=actions)

    def visitOn_options(self, ctx: WebFocusReportParser.On_optionsContext):
        if ctx.SUBHEAD() or ctx.SUBFOOT():
            centered = ctx.CENTER() is not None
            parts = []
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if isinstance(child, TerminalNode):
                    txt = child.getText().upper()
                    if txt in ['SUBHEAD', 'SUBFOOT', 'CENTER']: continue
                parts.append(child.getText())
            text = " ".join(parts).replace("'", "").replace('"', "")
            return Subhead(text=text, centered=centered) if ctx.SUBHEAD() else Subfoot(text=text, centered=centered)
        if ctx.COLUMN_TOTAL_KW():
            return SetCommand(parameter="COLUMN-TOTAL", value="ON")
        if ctx.ROW_TOTAL_KW():
            return SetCommand(parameter="ROW-TOTAL", value="ON")
        if ctx.style_block():
            return self.visit(ctx.style_block())
        if ctx.output_command():
            return self.visit(ctx.output_command())
        if ctx.summarize_command():
            return self.visit(ctx.summarize_command())
        if ctx.set_command():
             return self.visit(ctx.set_command())
        return None

    def visitOn_table_set_value(self, ctx: WebFocusReportParser.On_table_set_valueContext):
        return ctx.getText()

    def visitStyle_block(self, ctx: WebFocusReportParser.Style_blockContext):
        return SetCommand(parameter="STYLE", value="BLOCK")

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
        assignments = [self.visit(a) for a in ctx.compute_assignment()]
        return assignments # ReportRequest will extend this list

    def visitCompute_assignment(self, ctx: WebFocusReportParser.Compute_assignmentContext):
        name = ctx.qualified_name().getText() if ctx.qualified_name() else None
        if not name and ctx.prefix_operator():
            name = f"{ctx.prefix_operator().getText()}.{ctx.identifier().getText()}"

        format = ctx.format_name().getText() if ctx.format_name() else None
        expression = self.visit(ctx.dm_expression())
        alias = self.visit(ctx.as_phrase()) if ctx.as_phrase() else None
        return ComputeCommand(name=name, format=format, expression=expression, alias=alias)

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
        messages = [self.visit(child) for child in ctx.dm_type_element()]
        return TypeDM(messages=messages)

    def visitDm_type_element(self, ctx: WebFocusReportParser.Dm_type_elementContext):
        if ctx.dm_primary():
            return self.visit(ctx.dm_primary())
        return Literal(value=ctx.getText())

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
            return Literal(value=val[1:-1])
        if ctx.NUMBER():
            return Literal(value=int(ctx.NUMBER().getText()))
        if ctx.dm_float():
            return Literal(value=float(ctx.dm_float().getText()))
        if ctx.amper_var():
            return self.visit(ctx.amper_var())
        if ctx.qualified_name():
            if ctx.getChildCount() > 1 and ctx.getChild(1).getText() == '(':
                name = ctx.qualified_name().getText()
                args = []
                if ctx.dm_expression():
                    args = [self.visit(expr) for expr in ctx.dm_expression()]
                return FunctionCall(function_name=name, arguments=args)
            else:
                return Identifier(name=ctx.qualified_name().getText())
        if ctx.identifier() and ctx.prefix_operator():
             # Handle prefix_operator DOT identifier case
             name = f"{ctx.prefix_operator().getText()}.{ctx.identifier().getText()}"
             if ctx.getChildCount() > 3 and ctx.getChild(3).getText() == '(':
                 args = [self.visit(expr) for expr in ctx.dm_expression()]
                 return FunctionCall(function_name=name, arguments=args)
             return Identifier(name=name)

        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))
        return None

    def visitDm_command(self, ctx: WebFocusReportParser.Dm_commandContext):
        return self.visit(ctx.getChild(0))

    def visitDm_goto(self, ctx: WebFocusReportParser.Dm_gotoContext):
        target = ctx.identifier().getText()
        return Goto(target=target)

    def visitDm_label(self, ctx: WebFocusReportParser.Dm_labelContext):
        name = ctx.LABEL_DM().getText()[1:]
        return Label(name=name)

    def visitDm_if(self, ctx: WebFocusReportParser.Dm_ifContext):
        condition = self.visit(ctx.dm_logical_expression())
        then_target = ctx.identifier(0).getText()
        else_target = ctx.identifier(1).getText() if ctx.identifier(1) else None
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
        join_as = self.visit(ctx.as_phrase()) if ctx.as_phrase() else None
        outer = ctx.OUTER() is not None

        return Join(
            left_file=left_file,
            left_field=left_field,
            right_file=right_file,
            right_field=right_field,
            join_as=join_as,
            outer=outer
        )

    def visitDefine_file(self, ctx: WebFocusReportParser.Define_fileContext):
        filename = ctx.qualified_name().getText()
        assignments = [self.visit(a) for a in ctx.define_assignment()]
        return DefineFile(filename=filename, assignments=assignments)

    def visitDefine_assignment(self, ctx: WebFocusReportParser.Define_assignmentContext):
        fs = self.visit(ctx.field())
        expression = self.visit(ctx.dm_expression())
        return DefineAssignment(name=fs.name, expression=expression, format=fs.format if hasattr(fs, 'format') else None)

    def visitSummarize_command(self, ctx: WebFocusReportParser.Summarize_commandContext):
        verb = ctx.getChild(0).getText().upper()
        options = self.visit(ctx.summarize_options()) if ctx.summarize_options() else {}

        field_node = self.visit(ctx.field()) if ctx.field() else None
        field_name = field_node.name if field_node else None
        alias = field_node.alias if field_node else None

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
        if ctx.identifier():
             parameter = ctx.identifier().getText()
        else:
             parameter = ctx.hyphenated_name().getText()
        value = self.visit(ctx.on_table_set_value()) if ctx.on_table_set_value() else None
        return SetCommand(parameter=parameter, value=value)

    def visitDm_repeat(self, ctx: WebFocusReportParser.Dm_repeatContext):
        label = ctx.identifier().getText()
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
