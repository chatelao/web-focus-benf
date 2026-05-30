package com.transpiler.asg;

/**
 * Represents a literal value (number, string, etc.).
 */
public record Literal(Object value) implements Expression {
}
