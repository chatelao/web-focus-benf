package com.transpiler.asg;

import java.util.List;

/**
 * Represents a field selection in a verb or sort command.
 */
public record FieldSelection(
    String name,
    List<String> prefixOperators,
    String alias,
    String format
) implements ASGNode {
    public FieldSelection(String name, List<String> prefixOperators, String alias, String format) {
        this.name = name;
        this.prefixOperators = prefixOperators != null ? List.copyOf(prefixOperators) : List.of();
        this.alias = alias;
        this.format = format;
    }

    public FieldSelection(String name) {
        this(name, List.of(), null, null);
    }
}
