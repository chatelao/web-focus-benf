package com.transpiler.ir;

import com.transpiler.asg.Identifier;
import com.transpiler.asg.Literal;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class DataInstructionTest {

    @Test
    void testAssign() {
        Identifier source = new Identifier("VAR1");
        Assign assign = new Assign("target", source);
        assertEquals("target", assign.target());
        assertEquals(source, assign.source());
    }

    @Test
    void testSetEnv() {
        SetEnv setEnv = new SetEnv("AUTOCOMMIT", "ON");
        assertEquals("AUTOCOMMIT", setEnv.parameter());
        assertEquals("ON", setEnv.value());
    }

    @Test
    void testDefault() {
        Literal expression = new Literal("val1");
        Default defaultInstr = new Default("VAR1", expression);
        assertEquals("VAR1", defaultInstr.variable());
        assertEquals(expression, defaultInstr.expression());
    }
}
