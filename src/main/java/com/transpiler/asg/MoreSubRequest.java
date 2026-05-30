package com.transpiler.asg;

import java.util.List;

/**
 * Represents a FILE entry within a MORE phrase.
 */
public record MoreSubRequest(
    String filename,
    List<WhereClause> whereClauses
) implements ASGNode {
    public MoreSubRequest {
        whereClauses = List.copyOf(whereClauses);
    }
}
