package com.transpiler.ir;

import com.transpiler.asg.Command;
import com.transpiler.asg.MoreClause;
import java.util.List;

/**
 * Represents a report request (TABLE FILE) in the IR.
 */
public record Report(
    String filename,
    List<Command> components,
    List<Join> joins,
    MoreClause moreClause
) implements Instruction {
    public Report(String filename, List<Command> components, List<Join> joins, MoreClause moreClause) {
        this.filename = filename;
        this.components = components != null ? List.copyOf(components) : List.of();
        this.joins = joins != null ? List.copyOf(joins) : List.of();
        this.moreClause = moreClause;
    }
}
