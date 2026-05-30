package com.transpiler.ir;

/**
 * Represents a label in the instruction stream.
 */
public record Label(String name) implements Instruction {
}
