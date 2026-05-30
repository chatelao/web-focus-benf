package com.transpiler.asg;

import java.util.List;
import java.util.Map;

/**
 * Represents a DEFINE FILE block.
 */
public record DefineFile(
    String filename,
    List<Map<String, String>> assignments
) implements Statement {
    public DefineFile(String filename, List<Map<String, String>> assignments) {
        this.filename = filename;
        this.assignments = assignments != null ? List.copyOf(assignments) : List.of();
    }
}
