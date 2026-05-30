package com.transpiler.asg;

/**
 * Represents a Dialogue Manager -SET command.
 */
public record SetDM(String variable, Expression expression) implements Command {
}
