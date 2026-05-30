package com.transpiler.asg;

import java.util.List;

/**
 * Represents an ON command (ON TABLE or ON field).
 */
public record OnCommand(
    String target,
    List<String> actions
) implements Command {
    public OnCommand(String target, List<String> actions) {
        this.target = target;
        this.actions = actions != null ? List.copyOf(actions) : List.of();
    }
}
