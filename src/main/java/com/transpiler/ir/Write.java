package com.transpiler.ir;

import java.util.List;

/**
 * Represents a -WRITE command in the IR.
 */
public record Write(String filename, List<String> messages) implements Instruction {
    public Write {
        messages = List.copyOf(messages);
    }
}
