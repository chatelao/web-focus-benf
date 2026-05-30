package com.transpiler.asg;

/**
 * Represents a Dialogue Manager -REPEAT command.
 */
public record Repeat(
    String label,
    Expression condition,
    String conditionType,
    Expression times,
    String loopVar,
    Expression startVal,
    Expression endVal,
    Expression stepVal
) implements Command {
    // Simplified constructor for just label
    public Repeat(String label) {
        this(label, null, null, null, null, null, null, null);
    }
}
