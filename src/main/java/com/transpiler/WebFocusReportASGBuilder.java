package com.transpiler;

import com.transpiler.asg.*;
import org.antlr.v4.runtime.tree.TerminalNode;

import java.util.ArrayList;
import java.util.List;

/**
 * Transforms a WebFocusReport parse tree into an Abstract Semantic Graph (ASG).
 */
public class WebFocusReportASGBuilder extends WebFocusReportBaseVisitor<Object> {

    @Override
    public Object visitStart(WebFocusReportParser.StartContext ctx) {
        List<ASGNode> nodes = new ArrayList<>();
        if (ctx.children != null) {
            for (var child : ctx.children) {
                if (child instanceof TerminalNode) {
                    continue;
                }
                Object result = visit(child);
                if (result != null) {
                    if (result instanceof List<?>) {
                        for (Object item : (List<?>) result) {
                            if (item instanceof ASGNode) {
                                nodes.add((ASGNode) item);
                            }
                        }
                    } else if (result instanceof ASGNode) {
                        nodes.add((ASGNode) result);
                    }
                }
            }
        }
        return nodes;
    }

    @Override
    public Object visitWhen_command(WebFocusReportParser.When_commandContext ctx) {
        Expression condition = (Expression) visit(ctx.dm_logical_expression());
        return new WhenCommand(condition);
    }

    @Override
    public Object visitWhere_command(WebFocusReportParser.Where_commandContext ctx) {
        boolean isTotal = ctx.TOTAL() != null;
        Expression condition = (Expression) visit(ctx.dm_logical_expression());
        return new WhereClause(condition, isTotal);
    }

    @Override
    public Object visitRequest(WebFocusReportParser.RequestContext ctx) {
        String filename = (String) visit(ctx.table_file());
        List<Command> components = new ArrayList<>();
        MoreClause moreClause = null;

        // Iterate through all children except table_file (first) and end_command (last)
        for (int i = 1; i < ctx.getChildCount() - 1; i++) {
            var child = ctx.getChild(i);
            if (child instanceof TerminalNode) {
                continue;
            }
            if (child instanceof WebFocusReportParser.More_phraseContext) {
                Object visited = visit(child);
                if (visited instanceof MoreClause) {
                    moreClause = (MoreClause) visited;
                }
                continue;
            }
            Object result = visit(child);
            if (result != null) {
                if (result instanceof List<?>) {
                    for (Object item : (List<?>) result) {
                        if (item instanceof Command) {
                            components.add((Command) item);
                        }
                    }
                } else if (result instanceof Command) {
                    components.add((Command) result);
                }
            }
        }
        return new ReportRequest(filename, components, moreClause);
    }

    @Override
    public Object visitTable_file(WebFocusReportParser.Table_fileContext ctx) {
        return ctx.qualified_name().getText();
    }

    @Override
    public Object visitVerb_command(WebFocusReportParser.Verb_commandContext ctx) {
        String verb = (String) visit(ctx.verb());
        List<FieldSelection> fields;
        if (ctx.field_list() != null) {
            fields = (List<FieldSelection>) visit(ctx.field_list());
        } else {
            fields = List.of((FieldSelection) visit(ctx.asterisk()));
        }
        return new VerbCommand(verb, fields);
    }

    @Override
    public Object visitVerb(WebFocusReportParser.VerbContext ctx) {
        return ctx.getText().toUpperCase();
    }

    @Override
    public Object visitField_list(WebFocusReportParser.Field_listContext ctx) {
        List<FieldSelection> fields = new ArrayList<>();
        for (var f : ctx.field_or_prefixed()) {
            fields.add((FieldSelection) visit(f));
        }
        return fields;
    }

    @Override
    public Object visitField_or_prefixed(WebFocusReportParser.Field_or_prefixedContext ctx) {
        List<String> prefixes = ctx.prefix_operator().stream()
                .map(p -> p.getText().toUpperCase())
                .toList();
        FieldSelection selection = (FieldSelection) visit(ctx.field());
        return new FieldSelection(selection.name(), prefixes, selection.alias(), selection.format());
    }

    @Override
    public Object visitField(WebFocusReportParser.FieldContext ctx) {
        String name = ctx.qualified_name().getText();
        String format = ctx.format_name() != null ? ctx.format_name().getText() : null;
        String alias = ctx.as_phrase() != null ? (String) visit(ctx.as_phrase()) : null;
        return new FieldSelection(name, List.of(), alias, format);
    }

    @Override
    public Object visitAs_phrase(WebFocusReportParser.As_phraseContext ctx) {
        String val = ctx.STRING().getText();
        return val.substring(1, val.length() - 1);
    }

    @Override
    public Object visitAsterisk(WebFocusReportParser.AsteriskContext ctx) {
        return new FieldSelection("*");
    }

    @Override
    public Object visitDm_expression(WebFocusReportParser.Dm_expressionContext ctx) {
        return visit(ctx.dm_if_expression());
    }

    @Override
    public Object visitDm_if_expression(WebFocusReportParser.Dm_if_expressionContext ctx) {
        if (ctx.IF() != null) {
            Expression condition = (Expression) visit(ctx.dm_logical_expression());
            Expression thenExpr = (Expression) visit(ctx.dm_expression(0));
            Expression elseExpr = (Expression) visit(ctx.dm_expression(1));
            return new IfExpression(condition, thenExpr, elseExpr);
        }
        return visit(ctx.getChild(0));
    }

    @Override
    public Object visitDecode_expression(WebFocusReportParser.Decode_expressionContext ctx) {
        Expression expression = (Expression) visit(ctx.dm_primary(0));
        List<DecodeExpression.Pair> pairs = new ArrayList<>();

        int numPrimaries = ctx.dm_primary().size();
        boolean hasElse = ctx.ELSE() != null;
        int endPairsIdx = hasElse ? numPrimaries - 1 : numPrimaries;

        for (int i = 1; i < endPairsIdx; i += 2) {
            Expression search = (Expression) visit(ctx.dm_primary(i));
            Expression result = (Expression) visit(ctx.dm_primary(i + 1));
            pairs.add(new DecodeExpression.Pair(search, result));
        }

        Expression defaultValue = hasElse ? (Expression) visit(ctx.dm_primary(numPrimaries - 1)) : null;
        return new DecodeExpression(expression, pairs, defaultValue);
    }

    @Override
    public Object visitDm_logical_expression(WebFocusReportParser.Dm_logical_expressionContext ctx) {
        if (ctx.getChildCount() == 1) {
            return visit(ctx.getChild(0));
        }
        if (ctx.getChild(0).getText().equals("(")) {
            return visit(ctx.dm_logical_expression(0));
        }
        if (ctx.getChildCount() == 2) { // NOT case
            String operator = ctx.getChild(0).getText().toUpperCase();
            Expression operand = (Expression) visit(ctx.getChild(1));
            return new UnaryOperation(operator, operand);
        }
        // Handle binary logical operations (AND, OR)
        Expression left = (Expression) visit(ctx.getChild(0));
        String operator = ctx.getChild(1).getText().toUpperCase();
        Expression right = (Expression) visit(ctx.getChild(2));
        return new BinaryOperation(left, operator, right);
    }

    @Override
    public Object visitDm_relational_expression(WebFocusReportParser.Dm_relational_expressionContext ctx) {
        if (ctx.getChildCount() == 1) {
            return visit(ctx.dm_concat_expression(0));
        }

        // Case: MISSING
        if (ctx.MISSING() != null) {
            Expression expr = (Expression) visit(ctx.dm_concat_expression(0));
            boolean inverted = ctx.NE() != null || ctx.is_not_op() != null;
            return new IsMissingExpression(expr, inverted);
        }

        // Case: FROM...TO
        if (ctx.TO() != null) {
            Expression expr = (Expression) visit(ctx.dm_concat_expression(0));
            Expression lower = (Expression) visit(ctx.dm_concat_expression(1));
            Expression upper = (Expression) visit(ctx.dm_concat_expression(2));
            if (expr == null || lower == null || upper == null) {
                return null;
            }
            Expression node = new BetweenExpression(expr, lower, upper);
            if (ctx.not_from_op() != null) {
                return new UnaryOperation("NOT", node);
            }
            return node;
        }

        // Case: IN
        if (ctx.IN() != null) {
            Expression expr = (Expression) visit(ctx.dm_concat_expression(0));
            if (expr == null) return null;
            if (ctx.FILE() != null) {
                String filename = ctx.qualified_name().getText();
                return new InExpression(expr, List.of(), filename);
            } else {
                List<Expression> values = new ArrayList<>();
                for (int i = 1; i < ctx.dm_concat_expression().size(); i++) {
                    Expression v = (Expression) visit(ctx.dm_concat_expression(i));
                    if (v != null) {
                        values.add(v);
                    }
                }
                return new InExpression(expr, values);
            }
        }

        // Case: INCLUDES / EXCLUDES
        if (ctx.INCLUDES() != null || ctx.EXCLUDES() != null) {
            Expression left = (Expression) visit(ctx.dm_concat_expression(0));
            String op = ctx.INCLUDES() != null ? "CONTAINS" : "OMITS";
            List<WebFocusReportParser.Dm_concat_expressionContext> exprs = ctx.dm_concat_expression();

            Expression node = new BinaryOperation(left, op, (Expression) visit(exprs.get(1)));
            for (int i = 2; i < exprs.size(); i++) {
                Expression rightExpr = new BinaryOperation(left, op, (Expression) visit(exprs.get(i)));
                node = new BinaryOperation(node, "AND", rightExpr);
            }
            return node;
        }

        // Case: Relational op with optional OR
        if (ctx.dm_relational_op() != null) {
            Expression left = (Expression) visit(ctx.dm_concat_expression(0));
            String opText = ctx.dm_relational_op().getText().toUpperCase().replace("-", " ");
            List<WebFocusReportParser.Dm_concat_expressionContext> exprs = ctx.dm_concat_expression();

            Expression node = new BinaryOperation(left, opText, (Expression) visit(exprs.get(1)));
            for (int i = 2; i < exprs.size(); i++) {
                Expression rightExpr = new BinaryOperation(left, opText, (Expression) visit(exprs.get(i)));
                node = new BinaryOperation(node, "OR", rightExpr);
            }
            return node;
        }

        return visit(ctx.getChild(0));
    }

    @Override
    public Object visitDm_concat_expression(WebFocusReportParser.Dm_concat_expressionContext ctx) {
        if (ctx.getChildCount() == 1) {
            return visit(ctx.getChild(0));
        }
        Expression left = (Expression) visit(ctx.getChild(0));
        for (int i = 1; i < ctx.getChildCount(); i += 2) {
            String operator = ctx.getChild(i).getText();
            Expression right = (Expression) visit(ctx.getChild(i + 1));
            left = new BinaryOperation(left, operator, right);
        }
        return left;
    }

    @Override
    public Object visitDm_additive_expression(WebFocusReportParser.Dm_additive_expressionContext ctx) {
        if (ctx.getChildCount() == 1) {
            return visit(ctx.getChild(0));
        }
        Expression left = (Expression) visit(ctx.getChild(0));
        for (int i = 1; i < ctx.getChildCount(); i += 2) {
            String operator = ctx.getChild(i).getText();
            Expression right = (Expression) visit(ctx.getChild(i + 1));
            left = new BinaryOperation(left, operator, right);
        }
        return left;
    }

    @Override
    public Object visitDm_multiplicative_expression(WebFocusReportParser.Dm_multiplicative_expressionContext ctx) {
        if (ctx.getChildCount() == 1) {
            return visit(ctx.getChild(0));
        }
        Expression left = (Expression) visit(ctx.getChild(0));
        for (int i = 1; i < ctx.getChildCount(); i += 2) {
            String operator = ctx.getChild(i).getText();
            Expression right = (Expression) visit(ctx.getChild(i + 1));
            left = new BinaryOperation(left, operator, right);
        }
        return left;
    }

    @Override
    public Object visitDm_unary_expression(WebFocusReportParser.Dm_unary_expressionContext ctx) {
        if (ctx.getChildCount() == 1) {
            return visit(ctx.getChild(0));
        }
        String operator = ctx.getChild(0).getText();
        Expression operand = (Expression) visit(ctx.getChild(1));
        return new UnaryOperation(operator, operand);
    }

    @Override
    public Object visitDm_primary(WebFocusReportParser.Dm_primaryContext ctx) {
        if (ctx.NUMBER() != null) {
            return new Literal(Integer.parseInt(ctx.NUMBER().getText()));
        }
        if (ctx.dm_float() != null) {
            return visit(ctx.dm_float());
        }
        if (ctx.qualified_name() != null) {
            if (ctx.getChildCount() > 1 && ctx.getChild(1).getText().equals("(")) {
                String functionName = ctx.qualified_name().getText().toUpperCase();
                List<Expression> arguments = new ArrayList<>();
                for (var exprCtx : ctx.dm_expression()) {
                    arguments.add((Expression) visit(exprCtx));
                }
                return new FunctionCall(functionName, arguments);
            } else {
                return new Identifier(ctx.qualified_name().getText());
            }
        }
        if (ctx.amper_var() != null) {
            return visit(ctx.amper_var());
        }
        if (ctx.STRING() != null) {
            String val = ctx.STRING().getText();
            return new Literal(val.substring(1, val.length() - 1));
        }
        if (ctx.decode_expression() != null) {
            return visit(ctx.decode_expression());
        }
        if (ctx.getChildCount() == 3 && ctx.getChild(0).getText().equals("(")) {
            return visit(ctx.dm_expression(0));
        }
        return null;
    }

    @Override
    public Object visitAmper_var(WebFocusReportParser.Amper_varContext ctx) {
        return new AmperVar(ctx.getText());
    }

    @Override
    public Object visitDm_float(WebFocusReportParser.Dm_floatContext ctx) {
        return new Literal(Double.parseDouble(ctx.getText()));
    }

    @Override
    public Object visitDm_set(WebFocusReportParser.Dm_setContext ctx) {
        String variable = ctx.amper_var().getText();
        Expression expression = (Expression) visit(ctx.dm_expression());
        return new SetDM(variable, expression);
    }

    @Override
    public Object visitDm_default(WebFocusReportParser.Dm_defaultContext ctx) {
        String variable = ctx.amper_var().getText();
        Expression expression = (Expression) visit(ctx.dm_expression());
        return new DefaultDM(variable, expression);
    }

    @Override
    public Object visitDm_goto(WebFocusReportParser.Dm_gotoContext ctx) {
        return new Goto(ctx.NAME().getText());
    }

    @Override
    public Object visitDm_label(WebFocusReportParser.Dm_labelContext ctx) {
        // LABEL_DM starts with '-'
        return new Label(ctx.LABEL_DM().getText().substring(1));
    }

    @Override
    public Object visitDm_if(WebFocusReportParser.Dm_ifContext ctx) {
        Expression condition = (Expression) visit(ctx.dm_logical_expression());
        String thenTarget = ctx.NAME(0).getText();
        String elseTarget = ctx.NAME().size() > 1 ? ctx.NAME(1).getText() : null;
        return new IfDM(condition, thenTarget, elseTarget);
    }

    @Override
    public Object visitDm_run(WebFocusReportParser.Dm_runContext ctx) {
        return new RunDM();
    }

    @Override
    public Object visitDm_exit(WebFocusReportParser.Dm_exitContext ctx) {
        return new ExitDM();
    }

    @Override
    public Object visitDm_include(WebFocusReportParser.Dm_includeContext ctx) {
        return new IncludeDM(ctx.qualified_name().getText());
    }

    @Override
    public Object visitDm_htmlform(WebFocusReportParser.Dm_htmlformContext ctx) {
        if (ctx.HTMLFORM_BLOCK() != null) {
            return new HtmlFormDM(null, ctx.HTMLFORM_BLOCK().getText());
        }
        return new HtmlFormDM(ctx.qualified_name().getText(), null);
    }

    @Override
    public Object visitDm_type(WebFocusReportParser.Dm_typeContext ctx) {
        List<Expression> messages = new ArrayList<>();
        for (var prim : ctx.dm_primary()) {
            messages.add((Expression) visit(prim));
        }
        return new TypeDM(messages);
    }

    @Override
    public Object visitDm_read(WebFocusReportParser.Dm_readContext ctx) {
        String filename = ctx.qualified_name().getText();
        List<String> variables = new ArrayList<>();

        String currentVar = null;
        for (int i = 2; i < ctx.getChildCount(); i++) {
            var child = ctx.getChild(i);
            if (child instanceof WebFocusReportParser.Amper_varContext) {
                if (currentVar != null) {
                    variables.add(currentVar);
                }
                currentVar = child.getText();
            } else if (child instanceof WebFocusReportParser.Format_nameContext) {
                currentVar += "." + child.getText();
                variables.add(currentVar);
                currentVar = null;
            } else if (child instanceof TerminalNode && child.getText().equals(";")) {
                if (currentVar != null) {
                    variables.add(currentVar);
                }
                currentVar = null;
            }
        }
        if (currentVar != null) {
            variables.add(currentVar);
        }
        return new ReadDM(filename, variables);
    }

    @Override
    public Object visitDm_write(WebFocusReportParser.Dm_writeContext ctx) {
        String filename = ctx.qualified_name().getText();
        List<Expression> messages = new ArrayList<>();
        for (var prim : ctx.dm_primary()) {
            messages.add((Expression) visit(prim));
        }
        return new WriteDM(filename, messages);
    }

    @Override
    public Object visitDm_repeat(WebFocusReportParser.Dm_repeatContext ctx) {
        String label = ctx.NAME().getText();
        Expression condition = null;
        String conditionType = null;
        Expression times = null;
        String loopVar = null;
        Expression startVal = null;
        Expression endVal = null;
        Expression stepVal = null;

        if (ctx.WHILE() != null) {
            condition = (Expression) visit(ctx.dm_logical_expression());
            conditionType = "WHILE";
        } else if (ctx.UNTIL() != null) {
            condition = (Expression) visit(ctx.dm_logical_expression());
            conditionType = "UNTIL";
        } else if (ctx.TIMES() != null) {
            times = (Expression) visit(ctx.dm_primary(0));
        } else if (ctx.FOR() != null) {
            loopVar = ctx.amper_var().getText();
            startVal = (Expression) visit(ctx.dm_primary(0));
            endVal = (Expression) visit(ctx.dm_primary(1));
            if (ctx.STEP() != null) {
                stepVal = (Expression) visit(ctx.dm_primary(2));
            }
        }
        return new Repeat(label, condition, conditionType, times, loopVar, startVal, endVal, stepVal);
    }
}
