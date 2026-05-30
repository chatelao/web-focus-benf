package com.transpiler.asg;

/**
 * Represents a FOOTING command.
 */
public record Footing(
    String text,
    boolean centered
) implements Command {
    public Footing(String text) {
        this(text, false);
    }
}
