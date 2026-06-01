package com.transpiler.ir;

import com.transpiler.asg.Expression;
import java.util.List;

/**
 * Represents a -TYPE message in the IR.
 */
public record Type(List<Expression> messages) implements Instruction {
    public Type {
        messages = List.copyOf(messages);
    }
}
