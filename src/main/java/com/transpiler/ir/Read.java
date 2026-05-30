package com.transpiler.ir;

import java.util.List;

/**
 * Represents a -READ command in the IR.
 */
public record Read(String filename, List<String> variables) implements Instruction {
    public Read {
        variables = List.copyOf(variables);
    }
}
