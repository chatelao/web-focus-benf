package com.transpiler.asg;

import java.util.Map;

/**
 * Represents a summarization command (SUBTOTAL, SUMMARIZE, etc.).
 */
public record SummarizeCommand(
    String verb,
    String field,
    String alias,
    Map<String, Object> options
) implements Command {
    public SummarizeCommand(
        String verb,
        String field,
        String alias,
        Map<String, Object> options
    ) {
        this.verb = verb;
        this.field = field;
        this.alias = alias;
        this.options = options != null ? Map.copyOf(options) : Map.of();
    }
}
