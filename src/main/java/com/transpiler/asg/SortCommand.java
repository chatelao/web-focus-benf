package com.transpiler.asg;

/**
 * Represents a sort phrase (BY or ACROSS).
 */
public record SortCommand(
    String sortType,
    FieldSelection field
) implements Command {
}
