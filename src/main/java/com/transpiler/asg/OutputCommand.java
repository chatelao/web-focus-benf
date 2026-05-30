package com.transpiler.asg;

/**
 * Represents an output command (HOLD, PCHOLD, SAVE, SAVB).
 */
public record OutputCommand(
    String outputType,
    String filename,
    String format,
    String openClose
) implements Command {
}
