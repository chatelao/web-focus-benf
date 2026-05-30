package com.transpiler.asg;

import java.util.List;

/**
 * Represents a function call (e.g., ABS(field)).
 */
public record FunctionCall(String functionName, List<Expression> arguments) implements Expression {
}
