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
}
