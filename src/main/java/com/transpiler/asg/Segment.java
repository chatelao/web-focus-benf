package com.transpiler.asg;

import java.util.List;

/**
 * Represents a segment within a Master File.
 */
public record Segment(
    String name,
    String segtype,
    String parent,
    List<Field> fields,
    List<Field> virtualFields
) implements ASGNode {
    public Segment(String name, String segtype, String parent, List<Field> fields, List<Field> virtualFields) {
        this.name = name;
        this.segtype = segtype;
        this.parent = parent;
        this.fields = fields != null ? List.copyOf(fields) : List.of();
        this.virtualFields = virtualFields != null ? List.copyOf(virtualFields) : List.of();
    }

    public Segment(String name, String segtype) {
        this(name, segtype, null, List.of(), List.of());
    }
}
