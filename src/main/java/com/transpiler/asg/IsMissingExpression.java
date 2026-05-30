package com.transpiler.asg;

/**
 * Represents an IS MISSING expression.
 */
public record IsMissingExpression(Expression expression, boolean inverted) implements Expression {
}
