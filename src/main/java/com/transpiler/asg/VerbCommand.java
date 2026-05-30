package com.transpiler.asg;

import java.util.List;

/**
 * Represents a report verb command (PRINT, SUM, etc.).
 */
public record VerbCommand(
    String verb,
    List<FieldSelection> fields
) implements Command {
    public VerbCommand(String verb, List<FieldSelection> fields) {
        this.verb = verb;
        this.fields = fields != null ? List.copyOf(fields) : List.of();
    }
}
