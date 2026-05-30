package com.transpiler.ir;

import org.jgrapht.Graph;
import org.jgrapht.graph.DefaultDirectedGraph;
import org.jgrapht.graph.DefaultEdge;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.Set;

/**
 * Represents a control flow graph (CFG) using JGraphT.
 */
public final class ControlFlowGraph implements IRNode {
    private final Graph<BasicBlock, DefaultEdge> graph;
    private final Map<String, BasicBlock> blocks;
    private BasicBlock entryBlock;

    public ControlFlowGraph() {
        this.graph = new DefaultDirectedGraph<>(DefaultEdge.class);
        this.blocks = new HashMap<>();
    }

    public void addBlock(BasicBlock block) {
        Objects.requireNonNull(block);
        if (!blocks.containsKey(block.getName())) {
            blocks.put(block.getName(), block);
            graph.addVertex(block);
            if (entryBlock == null) {
                entryBlock = block;
            }
        }
    }

    public void addEdge(String fromBlockName, String toBlockName) {
        BasicBlock from = blocks.get(fromBlockName);
        BasicBlock to = blocks.get(toBlockName);
        if (from == null || to == null) {
            throw new IllegalArgumentException("Both blocks must exist in the CFG");
        }
        graph.addEdge(from, to);
    }

    public BasicBlock getBlock(String name) {
        return blocks.get(name);
    }

    public Set<BasicBlock> getBlocks() {
        return Collections.unmodifiableSet(graph.vertexSet());
    }

    public BasicBlock getEntryBlock() {
        return entryBlock;
    }

    public void setEntryBlock(BasicBlock entryBlock) {
        if (!blocks.containsKey(entryBlock.getName())) {
            addBlock(entryBlock);
        }
        this.entryBlock = entryBlock;
    }

    public Set<DefaultEdge> getOutgoingEdges(BasicBlock block) {
        return graph.outgoingEdgesOf(block);
    }

    public Set<DefaultEdge> getIncomingEdges(BasicBlock block) {
        return graph.incomingEdgesOf(block);
    }

    public BasicBlock getEdgeTarget(DefaultEdge edge) {
        return graph.getEdgeTarget(edge);
    }

    public BasicBlock getEdgeSource(DefaultEdge edge) {
        return graph.getEdgeSource(edge);
    }
}
