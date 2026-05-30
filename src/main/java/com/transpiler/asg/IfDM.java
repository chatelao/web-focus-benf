package com.transpiler.asg;

/**
 * Represents a Dialogue Manager -IF command.
 */
public record IfDM(Expression condition, String thenTarget, String elseTarget) implements Command {
    public IfDM(Expression condition, String thenTarget) {
        this(condition, thenTarget, null);
    }
}
