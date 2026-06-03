package com.transpiler.asg;

/**
 * Represents a WHEN command in a report request.
 */
public record WhenCommand(Expression condition) implements Command {
}
