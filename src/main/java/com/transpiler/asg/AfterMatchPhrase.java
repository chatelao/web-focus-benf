package com.transpiler.asg;

/**
 * Represents an AFTER MATCH phrase.
 */
public record AfterMatchPhrase(
    String mergeType,
    OutputCommand outputCommand
) implements ASGNode {
}
