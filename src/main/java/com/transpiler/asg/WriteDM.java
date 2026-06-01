package com.transpiler.asg;

import java.util.List;

/**
 * Represents a Dialogue Manager -WRITE command.
 */
public record WriteDM(String filename, List<Expression> messages) implements Command {
    public WriteDM {
        messages = List.copyOf(messages);
    }
}
