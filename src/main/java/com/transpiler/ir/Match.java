package com.transpiler.ir;

import com.transpiler.asg.Command;
import com.transpiler.asg.MoreClause;
import com.transpiler.asg.SubMatch;
import java.util.List;

/**
 * Represents a match request (MATCH FILE).
 */
public record Match(
    String filename,
    List<Command> components,
    List<SubMatch> subMatches,
    MoreClause moreClause
) implements Instruction {
    public Match(String filename, List<Command> components, List<SubMatch> subMatches, MoreClause moreClause) {
        this.filename = filename;
        this.components = components != null ? List.copyOf(components) : List.of();
        this.subMatches = subMatches != null ? List.copyOf(subMatches) : List.of();
        this.moreClause = moreClause;
    }

    public Match(String filename, List<Command> components) {
        this(filename, components, List.of(), null);
    }
}
