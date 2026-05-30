package com.transpiler.asg;

import java.util.List;

/**
 * Represents a TABLE FILE report request.
 */
public record ReportRequest(
    String filename,
    List<Command> components
) implements Statement {
    public ReportRequest(String filename, List<Command> components) {
        this.filename = filename;
        this.components = components != null ? List.copyOf(components) : List.of();
    }

    public ReportRequest(String filename) {
        this(filename, List.of());
    }
}
