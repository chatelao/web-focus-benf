package com.transpiler.ir;

import com.transpiler.asg.DefineAssignment;
import java.util.List;

/**
 * Represents a set of virtual field definitions (DEFINE FILE).
 */
public record Define(
    String filename,
    List<DefineAssignment> assignments
) implements Instruction {
    public Define(String filename, List<DefineAssignment> assignments) {
        this.filename = filename;
        this.assignments = assignments != null ? List.copyOf(assignments) : List.of();
    }
}
