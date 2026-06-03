package com.transpiler.asg;

import java.util.List;

/**
 * Represents a RECAP command.
 */
public record RecapCommand(
    List<RecapAssignment> assignments
) implements Command {
    public RecapCommand(List<RecapAssignment> assignments) {
        this.assignments = assignments != null ? List.copyOf(assignments) : List.of();
    }
}
