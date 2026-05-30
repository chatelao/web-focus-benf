package com.transpiler.asg;

/**
 * Represents a field or variable name.
 */
public record Identifier(String name) implements Expression {
}
