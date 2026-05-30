package com.transpiler.ir;

import org.junit.jupiter.api.Test;
import org.jgrapht.graph.DefaultEdge;

import java.util.Set;

import static org.junit.jupiter.api.Assertions.*;

class IRInfrastructureTest {

    @Test
    void testBasicBlock() {
        BasicBlock block = new BasicBlock("block1");
        assertEquals("block1", block.getName());
        assertTrue(block.getInstructions().isEmpty());

        // Dummy instruction for testing
        Instruction instr = new Instruction() {};
        block.addInstruction(instr);
        assertEquals(1, block.getInstructions().size());
        assertEquals(instr, block.getInstructions().get(0));
    }

    @Test
    void testControlFlowGraph() {
        ControlFlowGraph cfg = new ControlFlowGraph();
        BasicBlock b1 = new BasicBlock("b1");
        BasicBlock b2 = new BasicBlock("b2");

        cfg.addBlock(b1);
        cfg.addBlock(b2);

        assertEquals(2, cfg.getBlocks().size());
        assertEquals(b1, cfg.getEntryBlock());

        cfg.addEdge("b1", "b2");
        Set<DefaultEdge> edges = cfg.getOutgoingEdges(b1);
        assertEquals(1, edges.size());

        DefaultEdge edge = edges.iterator().next();
        assertEquals(b2, cfg.getEdgeTarget(edge));
        assertEquals(b1, cfg.getEdgeSource(edge));
    }

    @Test
    void testSetEntryBlock() {
        ControlFlowGraph cfg = new ControlFlowGraph();
        BasicBlock b1 = new BasicBlock("b1");
        BasicBlock b2 = new BasicBlock("b2");

        cfg.setEntryBlock(b2);
        assertEquals(b2, cfg.getEntryBlock());
        assertTrue(cfg.getBlocks().contains(b2));

        cfg.addBlock(b1);
        assertEquals(b2, cfg.getEntryBlock());
    }
}
