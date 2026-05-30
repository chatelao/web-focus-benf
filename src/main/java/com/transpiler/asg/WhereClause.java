package com.transpiler.asg;

/**
 * Represents a WHERE clause in a report request.
 */
public record WhereClause(
    String condition,
    boolean isTotal
) implements Command {
}
