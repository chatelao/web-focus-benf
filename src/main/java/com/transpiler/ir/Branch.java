package com.transpiler.ir;

import com.transpiler.asg.Expression;

/**
 * Represents a conditional branch: if condition goto trueTarget else goto falseTarget.
 */
public record Branch(Expression condition, String trueTarget, String falseTarget) implements Instruction {
}
