package com.transpiler.asg;

/**
 * Represents a WHERE clause in a report request.
 */
public record WhereClause(
    Expression condition,
    boolean isTotal
) implements Command {
}
