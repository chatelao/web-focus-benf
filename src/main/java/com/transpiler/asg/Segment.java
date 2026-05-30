package com.transpiler.asg;

import java.util.List;

/**
 * Represents a segment within a Master File.
 */
public record Segment(
    String name,
    String segtype,
    String parent,
    List<Field> fields
) implements ASGNode {
    public Segment(String name, String segtype, String parent, List<Field> fields) {
        this.name = name;
        this.segtype = segtype;
        this.parent = parent;
        this.fields = fields != null ? List.copyOf(fields) : List.of();
    }

    public Segment(String name, String segtype) {
        this(name, segtype, null, List.of());
    }
}
