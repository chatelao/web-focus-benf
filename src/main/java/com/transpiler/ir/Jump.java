package com.transpiler.ir;

/**
 * Represents an unconditional jump: goto target.
 */
public record Jump(String target) implements Instruction {
}
