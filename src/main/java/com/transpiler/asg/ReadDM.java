package com.transpiler.asg;

import java.util.List;

/**
 * Represents a Dialogue Manager -READ command.
 */
public record ReadDM(String filename, List<String> variables) implements Command {
    public ReadDM {
        variables = List.copyOf(variables);
    }
}
