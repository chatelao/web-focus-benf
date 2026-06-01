package com.transpiler.ir;

import com.transpiler.asg.Expression;
import java.util.List;

/**
 * Represents a -WRITE command in the IR.
 */
public record Write(String filename, List<Expression> messages) implements Instruction {
    public Write {
        messages = List.copyOf(messages);
    }
}
