package com.transpiler.asg;

import java.util.List;

/**
 * Represents a DEFINE FILE block.
 */
public record DefineFile(
    String filename,
    List<DefineAssignment> assignments
) implements Statement {
    public DefineFile(String filename, List<DefineAssignment> assignments) {
        this.filename = filename;
        this.assignments = assignments != null ? List.copyOf(assignments) : List.of();
    }
}
