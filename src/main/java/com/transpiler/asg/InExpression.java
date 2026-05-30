package com.transpiler.asg;

import java.util.List;

/**
 * Represents an IN expression (e.g., field IN (val1, val2)).
 */
public record InExpression(Expression expression, List<Expression> values) implements Expression {
}
