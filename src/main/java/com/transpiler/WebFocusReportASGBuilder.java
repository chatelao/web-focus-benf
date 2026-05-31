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
        if (ctx.dm_logical_expression() != null && ctx.getChildCount() == 1) {
            return visit(ctx.dm_logical_expression());
        }
        return null; // IF-THEN-ELSE not handled yet
    }

    @Override
    public Object visitDm_logical_expression(WebFocusReportParser.Dm_logical_expressionContext ctx) {
        if (ctx.getChildCount() == 3 && ctx.getChild(0).getText().equals("(")) {
            return visit(ctx.dm_logical_expression(0));
        }
        if (ctx.dm_relational_expression() != null && ctx.getChildCount() == 1) {
            return visit(ctx.dm_relational_expression());
        }
        return null; // NOT, AND, OR not handled yet
    }

    @Override
    public Object visitDm_relational_expression(WebFocusReportParser.Dm_relational_expressionContext ctx) {
        if (ctx.dm_concat_expression() != null && ctx.getChildCount() == 1) {
            return visit(ctx.dm_concat_expression(0));
        }
        return null; // MISSING, FROM-TO, IN, etc not handled yet
    }

    @Override
    public Object visitDm_concat_expression(WebFocusReportParser.Dm_concat_expressionContext ctx) {
        if (ctx.dm_additive_expression() != null && ctx.getChildCount() == 1) {
            return visit(ctx.dm_additive_expression(0));
        }
        return null; // CONCAT not handled yet
    }

    @Override
    public Object visitDm_additive_expression(WebFocusReportParser.Dm_additive_expressionContext ctx) {
        if (ctx.dm_multiplicative_expression() != null && ctx.getChildCount() == 1) {
            return visit(ctx.dm_multiplicative_expression(0));
        }
        return null; // ADD, SUB not handled yet
    }

    @Override
    public Object visitDm_multiplicative_expression(WebFocusReportParser.Dm_multiplicative_expressionContext ctx) {
        if (ctx.dm_unary_expression() != null && ctx.getChildCount() == 1) {
            return visit(ctx.dm_unary_expression(0));
        }
        return null; // MUL, DIV not handled yet
    }

    @Override
    public Object visitDm_unary_expression(WebFocusReportParser.Dm_unary_expressionContext ctx) {
        if (ctx.dm_primary() != null) {
            return visit(ctx.dm_primary());
        }
        return null; // Unary ops not handled yet
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
                return null; // FunctionCall not handled yet
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
}
