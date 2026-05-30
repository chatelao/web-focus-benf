package com.transpiler.asg;

/**
 * Represents a Dialogue Manager -GOTO command.
 */
public record Goto(String target) implements Command {
}
