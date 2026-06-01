package com.transpiler.asg;

import java.util.List;

/**
 * Represents a Dialogue Manager -TYPE command.
 */
public record TypeDM(List<Expression> messages) implements Command {
    public TypeDM {
        messages = List.copyOf(messages);
    }
}
