package com.transpiler.asg;

/**
 * Represents a HEADING command.
 */
public record Heading(
    String text,
    boolean centered
) implements Command {
}
