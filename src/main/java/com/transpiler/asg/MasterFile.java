package com.transpiler.asg;

import java.util.List;

/**
 * Represents a WebFOCUS Master File (metadata).
 */
public record MasterFile(
    String name,
    String suffix,
    List<Segment> segments
) implements ASGNode {
    public MasterFile(String name, String suffix, List<Segment> segments) {
        this.name = name;
        this.suffix = suffix;
        this.segments = segments != null ? List.copyOf(segments) : List.of();
    }

    public MasterFile(String name, String suffix) {
        this(name, suffix, List.of());
    }
}
