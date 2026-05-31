package com.transpiler.ir;

import java.util.List;
import java.util.Map;

/**
 * Represents a set of virtual field definitions (DEFINE FILE).
 */
public record Define(
    String filename,
    List<Map<String, String>> assignments
) implements Instruction {
    public Define(String filename, List<Map<String, String>> assignments) {
        this.filename = filename;
        this.assignments = assignments != null ? List.copyOf(assignments) : List.of();
    }
}
