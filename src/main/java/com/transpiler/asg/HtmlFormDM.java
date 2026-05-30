package com.transpiler.asg;

/**
 * Represents a Dialogue Manager -HTMLFORM command or block.
 */
public record HtmlFormDM(String filename, String content) implements Command {
}
