package com.transpiler.asg;

import java.util.List;

/**
 * Represents a MATCH FILE request.
 */
public record MatchRequest(
    String filename,
    List<ASGNode> components,
    MoreClause moreClause,
    List<SubMatch> subMatches
) implements Statement {
    public MatchRequest {
        components = List.copyOf(components);
        subMatches = List.copyOf(subMatches);
    }
}
