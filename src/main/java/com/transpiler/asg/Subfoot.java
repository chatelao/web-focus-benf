package com.transpiler.asg;

/**
 * Represents a SUBFOOT command.
 */
public record Subfoot(
    String text,
    boolean centered
) implements Command {
}
