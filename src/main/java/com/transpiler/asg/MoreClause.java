package com.transpiler.asg;

import java.util.List;

/**
 * Represents a MORE phrase.
 */
public record MoreClause(List<MoreSubRequest> subRequests) implements ASGNode {
    public MoreClause {
        subRequests = List.copyOf(subRequests);
    }
}
