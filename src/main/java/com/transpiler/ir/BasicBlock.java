package com.transpiler.ir;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * Represents a basic block: a linear sequence of instructions.
 */
public final class BasicBlock implements IRNode {
    private final String name;
    private final List<Instruction> instructions;

    public BasicBlock(String name) {
        this.name = Objects.requireNonNull(name);
        this.instructions = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public List<Instruction> getInstructions() {
        return List.copyOf(instructions);
    }

    public void addInstruction(Instruction instruction) {
        instructions.add(Objects.requireNonNull(instruction));
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        BasicBlock that = (BasicBlock) o;
        return Objects.equals(name, that.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }

    @Override
    public String toString() {
        return "BasicBlock{" +
                "name='" + name + '\'' +
                ", instructionsCount=" + instructions.size() +
                '}';
    }
}
