package com.transpiler.ir;

import com.transpiler.asg.Expression;

/**
 * Represents an assignment: target = source.
 */
public record Assign(String target, Expression source) implements Instruction {
}
