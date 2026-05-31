package com.transpiler.asg;

import java.util.List;

/**
 * Represents a WebFOCUS Master File (metadata).
 */
public record MasterFile(
    String name,
    String suffix,
    List<Segment> segments,
    List<Field> virtualFields,
    List<Dimension> dimensions,
    List<Hierarchy> hierarchies
) implements ASGNode {
    public MasterFile(String name, String suffix, List<Segment> segments,
                      List<Field> virtualFields, List<Dimension> dimensions,
                      List<Hierarchy> hierarchies) {
        this.name = name;
        this.suffix = suffix;
        this.segments = segments != null ? List.copyOf(segments) : List.of();
        this.virtualFields = virtualFields != null ? List.copyOf(virtualFields) : List.of();
        this.dimensions = dimensions != null ? List.copyOf(dimensions) : List.of();
        this.hierarchies = hierarchies != null ? List.copyOf(hierarchies) : List.of();
    }

    public MasterFile(String name, String suffix) {
        this(name, suffix, List.of(), List.of(), List.of(), List.of());
    }
}
