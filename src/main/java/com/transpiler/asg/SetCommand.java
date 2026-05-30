package com.transpiler.asg;

/**
 * Represents a SET (non-Dialogue Manager) command.
 */
public record SetCommand(
    String parameter,
    String value
) implements Command {
}
