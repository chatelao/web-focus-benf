package com.transpiler.ir;

import java.util.List;

/**
 * Represents a call to another procedure or an external action (JOIN, INCLUDE).
 */
public record Call(String target, List<String> arguments) implements Instruction {
    public Call {
        arguments = List.copyOf(arguments);
    }
}
