package com.transpiler.asg;

/**
 * Represents a unary operation (e.g., -a, NOT a).
 */
public record UnaryOperation(String operator, Expression operand) implements Expression {
}
