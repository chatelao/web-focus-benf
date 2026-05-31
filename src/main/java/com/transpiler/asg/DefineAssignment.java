package com.transpiler.asg;

/**
 * Represents a single assignment within a DEFINE FILE block or Master File.
 */
public record DefineAssignment(
    String name,
    String expression,
    String format
) implements ASGNode {
}
