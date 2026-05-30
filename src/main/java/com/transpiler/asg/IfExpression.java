package com.transpiler.asg;

/**
 * Represents an inline IF expression (IF condition THEN expr1 ELSE expr2).
 */
public record IfExpression(Expression condition, Expression thenExpression, Expression elseExpression) implements Expression {
}
