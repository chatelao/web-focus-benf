package com.transpiler.asg;

/**
 * Represents a SUBHEAD command.
 */
public record Subhead(
    String text,
    boolean centered
) implements Command {
}
