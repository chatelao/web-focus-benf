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
}
