package com.transpiler.ir;

import java.util.List;

/**
 * Represents a -TYPE message in the IR.
 */
public record Type(List<String> messages) implements Instruction {
    public Type {
        messages = List.copyOf(messages);
    }
}
