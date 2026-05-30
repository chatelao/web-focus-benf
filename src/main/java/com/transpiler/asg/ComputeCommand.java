package com.transpiler.asg;

/**
 * Represents a COMPUTE command.
 */
public record ComputeCommand(
    String name,
    String expression,
    String format
) implements Command {
}
