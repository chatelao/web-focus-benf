package com.transpiler.asg;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ExpressionTest {

    @Test
    void testLiteral() {
        Literal stringLiteral = new Literal("hello");
        assertEquals("hello", stringLiteral.value());

        Literal numberLiteral = new Literal(42);
        assertEquals(42, numberLiteral.value());
    }

    @Test
    void testIdentifier() {
        Identifier id = new Identifier("MYFIELD");
        assertEquals("MYFIELD", id.name());
    }

    @Test
    void testAmperVar() {
        AmperVar var = new AmperVar("MYVAR");
        assertEquals("MYVAR", var.name());
    }

    @Test
    void testExpressionInterfaces() {
        Literal lit = new Literal(1);
        Identifier id = new Identifier("A");
        AmperVar var = new AmperVar("V");

        assertTrue(lit instanceof Expression);
        assertTrue(id instanceof Expression);
        assertTrue(var instanceof Expression);

        assertTrue(lit instanceof ASGNode);
        assertTrue(id instanceof ASGNode);
        assertTrue(var instanceof ASGNode);
    }
}
