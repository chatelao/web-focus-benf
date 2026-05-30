package com.transpiler.asg;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CommandTest {

    @Test
    void testGoto() {
        Goto gotoNode = new Goto("MYLABEL");
        assertEquals("MYLABEL", gotoNode.target());
        assertTrue(gotoNode instanceof Command);
        assertTrue(gotoNode instanceof ASGNode);
    }

    @Test
    void testLabel() {
        Label labelNode = new Label("MYLABEL");
        assertEquals("MYLABEL", labelNode.name());
        assertTrue(labelNode instanceof Command);
        assertTrue(labelNode instanceof ASGNode);
    }

    @Test
    void testIfDM() {
        Expression condition = new BinaryOperation(new AmperVar("A"), "EQ", new Literal(10));
        IfDM ifDM = new IfDM(condition, "THEN_LABEL", "ELSE_LABEL");

        assertEquals(condition, ifDM.condition());
        assertEquals("THEN_LABEL", ifDM.thenTarget());
        assertEquals("ELSE_LABEL", ifDM.elseTarget());
        assertTrue(ifDM instanceof Command);

        IfDM ifDMNoElse = new IfDM(condition, "THEN_LABEL");
        assertNull(ifDMNoElse.elseTarget());
    }
}
