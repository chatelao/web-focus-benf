package com.transpiler.asg;

/**
 * Represents a JOIN command.
 */
public record Join(
    String leftFile,
    String leftField,
    String rightFile,
    String rightField,
    String joinAs,
    boolean outer
) implements Command {
}
