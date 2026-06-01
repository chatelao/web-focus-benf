package com.transpiler.asg;

import java.util.List;

/**
 * Represents an IN expression (e.g., field IN (val1, val2)).
 */
public record InExpression(Expression expression, List<Expression> values, String filename) implements Expression {
    public InExpression {
        values = List.copyOf(values);
    }

    public InExpression(Expression expression, List<Expression> values) {
        this(expression, values, null);
    }
}
