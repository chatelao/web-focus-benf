package com.transpiler.ir;

import com.transpiler.asg.ASGNode;
import com.transpiler.asg.MoreClause;
import com.transpiler.asg.SubMatch;
import java.util.List;

/**
 * Represents a match request (MATCH FILE) in the IR.
 */
public record Match(
    String filename,
    List<ASGNode> components,
    List<SubMatch> subMatches,
    MoreClause moreClause
) implements Instruction {
    public Match(String filename, List<ASGNode> components, List<SubMatch> subMatches, MoreClause moreClause) {
        this.filename = filename;
        this.components = components != null ? List.copyOf(components) : List.of();
        this.subMatches = subMatches != null ? List.copyOf(subMatches) : List.of();
        this.moreClause = moreClause;
    }
}
