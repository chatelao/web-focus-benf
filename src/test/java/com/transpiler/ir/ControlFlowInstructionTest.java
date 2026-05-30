package com.transpiler.ir;

import com.transpiler.asg.Identifier;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class ControlFlowInstructionTest {

    @Test
    void testLabel() {
        Label label = new Label("START");
        assertEquals("START", label.name());
    }

    @Test
    void testJump() {
        Jump jump = new Jump("END");
        assertEquals("END", jump.target());
    }

    @Test
    void testBranch() {
        Identifier condition = new Identifier("VAR1");
        Branch branch = new Branch(condition, "TRUE_BLOCK", "FALSE_BLOCK");
        assertEquals(condition, branch.condition());
        assertEquals("TRUE_BLOCK", branch.trueTarget());
        assertEquals("FALSE_BLOCK", branch.falseTarget());
    }

    @Test
    void testPhi() {
        List<String> sources = new java.util.ArrayList<>(List.of("v1", "v2"));
        Phi phi = new Phi("x", sources);
        assertEquals("x", phi.target());
        assertEquals(sources, phi.sources());
        assertNotSame(sources, phi.sources()); // Ensure copy
        assertThrows(UnsupportedOperationException.class, () -> phi.sources().add("v3"));
    }
}
