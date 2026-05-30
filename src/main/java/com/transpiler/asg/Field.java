package com.transpiler.asg;

/**
 * Represents a field within a segment.
 */
public record Field(
    String name,
    String alias,
    String format
) implements ASGNode {
}
