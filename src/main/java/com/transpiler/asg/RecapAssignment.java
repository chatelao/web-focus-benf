package com.transpiler.asg;

/**
 * Represents a single assignment within a RECAP command.
 */
public record RecapAssignment(
    String name,
    Expression expression,
    Expression columnRef,
    String format,
    String alias,
    Integer indent,
    boolean noprint
) implements ASGNode {
}
