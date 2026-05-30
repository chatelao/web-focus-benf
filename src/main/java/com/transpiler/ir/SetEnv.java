package com.transpiler.ir;

/**
 * Represents an environment setting (SET parameter = value).
 */
public record SetEnv(String parameter, String value) implements Instruction {
}
