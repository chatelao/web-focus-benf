package com.transpiler.ir;

import java.util.List;

/**
 * Represents a Phi node in SSA form: target = Phi(v1, v2, ...).
 */
public record Phi(String target, List<String> sources) implements Instruction {
    public Phi {
        sources = List.copyOf(sources);
    }
}
