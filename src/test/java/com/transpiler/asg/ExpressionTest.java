package com.transpiler.asg;

import org.junit.jupiter.api.Test;

import java.util.List;

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

    @Test
    void testBinaryOperation() {
        Expression left = new Literal(1);
        Expression right = new Literal(2);
        BinaryOperation op = new BinaryOperation(left, "+", right);

        assertEquals(left, op.left());
        assertEquals("+", op.operator());
        assertEquals(right, op.right());
        assertTrue(op instanceof Expression);
    }

    @Test
    void testUnaryOperation() {
        Expression operand = new Identifier("MYFIELD");
        UnaryOperation op = new UnaryOperation("-", operand);

        assertEquals("-", op.operator());
        assertEquals(operand, op.operand());
        assertTrue(op instanceof Expression);
    }

    @Test
    void testFunctionCall() {
        Expression arg1 = new Identifier("FIELD1");
        Expression arg2 = new Literal(10);
        List<Expression> args = List.of(arg1, arg2);
        FunctionCall call = new FunctionCall("ABS", args);

        assertEquals("ABS", call.functionName());
        assertEquals(args, call.arguments());
        assertEquals(2, call.arguments().size());
        assertTrue(call instanceof Expression);
    }

    @Test
    void testIfExpression() {
        Expression condition = new BinaryOperation(new Identifier("A"), ">", new Literal(0));
        Expression thenExpr = new Literal(1);
        Expression elseExpr = new Literal(-1);
        IfExpression ifExpr = new IfExpression(condition, thenExpr, elseExpr);

        assertEquals(condition, ifExpr.condition());
        assertEquals(thenExpr, ifExpr.thenExpression());
        assertEquals(elseExpr, ifExpr.elseExpression());
        assertTrue(ifExpr instanceof Expression);
    }

    @Test
    void testDecodeExpression() {
        Expression target = new Identifier("COUNTRY");
        List<DecodeExpression.Pair> pairs = List.of(
            new DecodeExpression.Pair(new Literal("ENGLAND"), new Literal("UK")),
            new DecodeExpression.Pair(new Literal("FRANCE"), new Literal("EU"))
        );
        Expression defaultValue = new Literal("OTHER");
        DecodeExpression decode = new DecodeExpression(target, pairs, defaultValue);

        assertEquals(target, decode.expression());
        assertEquals(pairs, decode.pairs());
        assertEquals(2, decode.pairs().size());
        assertEquals(defaultValue, decode.defaultValue());
        assertTrue(decode instanceof Expression);
    }
}
