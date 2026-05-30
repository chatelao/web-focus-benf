package com.transpiler.ir;

import com.transpiler.asg.Expression;

/**
 * Represents a -DEFAULT, -DEFAULTS, or -DEFAULTH command.
 */
public record Default(String variable, Expression expression) implements Instruction {
}
