package com.transpiler.ir;

/**
 * Represents a JOIN command in the IR.
 */
public record Join(
    String leftFile,
    String leftField,
    String rightFile,
    String rightField,
    String joinAs,
    boolean outer,
    boolean isAll
) implements Instruction {
}
