package com.transpiler.asg;

import java.util.List;

/**
 * Represents a DECODE expression.
 */
public record DecodeExpression(Expression expression, List<Pair> pairs, Expression defaultValue) implements Expression {
    /**
     * Represents a search-result pair in a DECODE expression.
     */
    public record Pair(Expression search, Expression result) {}
}
