package com.transpiler.asg;

/**
 * Represents a COMPUTE command.
 */
public record ComputeCommand(
    String name,
    Expression expression,
    String format,
    String alias
) implements Command {
    public ComputeCommand(String name, Expression expression, String format) {
        this(name, expression, format, null);
    }
}
