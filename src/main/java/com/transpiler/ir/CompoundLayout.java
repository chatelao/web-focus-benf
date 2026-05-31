package com.transpiler.ir;

import com.transpiler.asg.OutputCommand;
import com.transpiler.asg.Statement;
import java.util.List;

/**
 * Represents the start of a COMPOUND LAYOUT block.
 */
public record CompoundLayout(
    OutputCommand outputCommand,
    List<Statement> statements
) implements Instruction {
    public CompoundLayout(OutputCommand outputCommand, List<Statement> statements) {
        this.outputCommand = outputCommand;
        this.statements = statements != null ? List.copyOf(statements) : List.of();
    }
}
