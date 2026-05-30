package com.transpiler.ir;

/**
 * Represents a -HTMLFORM command or block in the IR.
 */
public record HtmlForm(String filename, String content) implements Instruction {
}
