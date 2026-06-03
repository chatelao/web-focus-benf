package com.transpiler.asg;

import java.util.Map;

/**
 * Represents a sort phrase (BY or ACROSS).
 */
public record SortCommand(
    String sortType,
    FieldSelection field,
    Map<String, Object> options,
    SummarizeCommand summarize,
    boolean noprint,
    boolean acrossTotal,
    String totalAs,
    boolean isHierarchy
) implements Command {
    public SortCommand(
        String sortType,
        FieldSelection field,
        Map<String, Object> options,
        SummarizeCommand summarize,
        boolean noprint,
        boolean acrossTotal,
        String totalAs,
        boolean isHierarchy
    ) {
        this.sortType = sortType;
        this.field = field;
        this.options = options != null ? Map.copyOf(options) : Map.of();
        this.summarize = summarize;
        this.noprint = noprint;
        this.acrossTotal = acrossTotal;
        this.totalAs = totalAs;
        this.isHierarchy = isHierarchy;
    }

    public SortCommand(String sortType, FieldSelection field) {
        this(sortType, field, Map.of(), null, false, false, null, false);
    }
}
