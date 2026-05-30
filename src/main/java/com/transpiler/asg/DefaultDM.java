package com.transpiler.asg;

/**
 * Represents a Dialogue Manager -DEFAULT, -DEFAULTS, or -DEFAULTH command.
 */
public record DefaultDM(String variable, Expression expression) implements Command {
}
