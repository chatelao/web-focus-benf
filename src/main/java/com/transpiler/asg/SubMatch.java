package com.transpiler.asg;

import java.util.List;

/**
 * Represents a FILE entry within a MATCH request.
 */
public record SubMatch(
    String filename,
    List<ASGNode> components,
    MoreClause moreClause,
    AfterMatchPhrase afterMatch
) implements ASGNode {
    public SubMatch {
        components = List.copyOf(components);
    }
}
