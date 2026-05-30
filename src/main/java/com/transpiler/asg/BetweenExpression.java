package com.transpiler.asg;

/**
 * Represents a BETWEEN or FROM...TO expression.
 */
public record BetweenExpression(Expression expression, Expression lower, Expression upper) implements Expression {
}
