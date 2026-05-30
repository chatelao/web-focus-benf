package com.transpiler.asg;

/**
 * Represents a binary operation (e.g., a + b, a AND b).
 */
public record BinaryOperation(Expression left, String operator, Expression right) implements Expression {
}
