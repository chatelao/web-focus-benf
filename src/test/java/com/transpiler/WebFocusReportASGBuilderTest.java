package com.transpiler;

import com.transpiler.asg.*;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class WebFocusReportASGBuilderTest {

    @Test
    public void testBasicTableFile() {
        String input = "TABLE FILE CAR\nEND";
        WebFocusReportLexer lexer = new WebFocusReportLexer(CharStreams.fromString(input));
        WebFocusReportParser parser = new WebFocusReportParser(new CommonTokenStream(lexer));
        WebFocusReportParser.StartContext tree = parser.start();

        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();
        Object result = builder.visit(tree);

        assertTrue(result instanceof List);
        List<?> nodes = (List<?>) result;
        assertEquals(1, nodes.size());
        assertTrue(nodes.get(0) instanceof ReportRequest);

        ReportRequest request = (ReportRequest) nodes.get(0);
        assertEquals("CAR", request.filename());
        assertTrue(request.components().isEmpty());
        assertNull(request.moreClause());
    }

    @Test
    public void testTableWithVerbAndFields() {
        String input = "TABLE FILE CAR\nPRINT COUNTRY AS 'Nation' MODEL\nEND";
        WebFocusReportLexer lexer = new WebFocusReportLexer(CharStreams.fromString(input));
        WebFocusReportParser parser = new WebFocusReportParser(new CommonTokenStream(lexer));
        WebFocusReportParser.StartContext tree = parser.start();

        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();
        Object result = builder.visit(tree);

        List<?> nodes = (List<?>) result;
        ReportRequest request = (ReportRequest) nodes.get(0);
        assertEquals("CAR", request.filename());
        assertEquals(1, request.components().size());

        com.transpiler.asg.VerbCommand verbCmd = (com.transpiler.asg.VerbCommand) request.components().get(0);
        assertEquals("PRINT", verbCmd.verb());
        assertEquals(2, verbCmd.fields().size());

        com.transpiler.asg.FieldSelection f1 = verbCmd.fields().get(0);
        assertEquals("COUNTRY", f1.name());
        assertEquals("Nation", f1.alias());

        com.transpiler.asg.FieldSelection f2 = verbCmd.fields().get(1);
        assertEquals("MODEL", f2.name());
        assertNull(f2.alias());
    }

    @Test
    public void testTableWithAsterisk() {
        String input = "TABLE FILE CAR\nSUM *\nEND";
        WebFocusReportLexer lexer = new WebFocusReportLexer(CharStreams.fromString(input));
        WebFocusReportParser parser = new WebFocusReportParser(new CommonTokenStream(lexer));
        WebFocusReportParser.StartContext tree = parser.start();

        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();
        Object result = builder.visit(tree);

        List<?> nodes = (List<?>) result;
        ReportRequest request = (ReportRequest) nodes.get(0);
        com.transpiler.asg.VerbCommand verbCmd = (com.transpiler.asg.VerbCommand) request.components().get(0);
        assertEquals("SUM", verbCmd.verb());
        assertEquals(1, verbCmd.fields().size());
        assertEquals("*", verbCmd.fields().get(0).name());
    }

    @Test
    public void testExpressionLiterals() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // Integer literal
        WebFocusReportParser parser = createParser("123");
        Literal litInt = (Literal) builder.visit(parser.dm_expression());
        assertEquals(123, litInt.value());

        // Float literal
        parser = createParser("12.34");
        Literal litFloat = (Literal) builder.visit(parser.dm_expression());
        assertEquals(12.34, litFloat.value());

        // String literal
        parser = createParser("'Hello'");
        Literal litStr = (Literal) builder.visit(parser.dm_expression());
        assertEquals("Hello", litStr.value());
    }

    @Test
    public void testExpressionIdentifierAndAmperVar() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // Identifier
        WebFocusReportParser parser = createParser("COUNTRY");
        Identifier ident = (Identifier) builder.visit(parser.dm_expression());
        assertEquals("COUNTRY", ident.name());

        // AmperVar
        parser = createParser("&VAR");
        AmperVar amper = (AmperVar) builder.visit(parser.dm_expression());
        assertEquals("&VAR", amper.name());
    }

    @Test
    public void testNestedExpression() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();
        WebFocusReportParser parser = createParser("((123))");
        Literal lit = (Literal) builder.visit(parser.dm_expression());
        assertEquals(123, lit.value());
    }

    @Test
    public void testArithmeticOperations() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // Addition
        WebFocusReportParser parser = createParser("1 + 2");
        BinaryOperation op = (BinaryOperation) builder.visit(parser.dm_expression());
        assertEquals("+", op.operator());
        assertEquals(1, ((Literal) op.left()).value());
        assertEquals(2, ((Literal) op.right()).value());

        // Precedence: 1 + 2 * 3
        parser = createParser("1 + 2 * 3");
        op = (BinaryOperation) builder.visit(parser.dm_expression());
        assertEquals("+", op.operator());
        assertEquals(1, ((Literal) op.left()).value());
        BinaryOperation rightOp = (BinaryOperation) op.right();
        assertEquals("*", rightOp.operator());

        // Unary: -1
        parser = createParser("-1");
        UnaryOperation unary = (UnaryOperation) builder.visit(parser.dm_expression());
        assertEquals("-", unary.operator());
        assertEquals(1, ((Literal) unary.operand()).value());
    }

    @Test
    public void testLogicalOperations() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // AND
        WebFocusReportParser parser = createParser("A AND B");
        BinaryOperation op = (BinaryOperation) builder.visit(parser.dm_expression());
        assertEquals("AND", op.operator());
        assertEquals("A", ((Identifier) op.left()).name());
        assertEquals("B", ((Identifier) op.right()).name());

        // NOT
        parser = createParser("NOT A");
        UnaryOperation unary = (UnaryOperation) builder.visit(parser.dm_expression());
        assertEquals("NOT", unary.operator());
        assertEquals("A", ((Identifier) unary.operand()).name());
    }

    @Test
    public void testRelationalOperations() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // EQ
        WebFocusReportParser parser = createParser("A EQ B");
        BinaryOperation op = (BinaryOperation) builder.visit(parser.dm_expression());
        assertEquals("EQ", op.operator());

        // Multiple RHS: A EQ B OR C
        parser = createParser("A EQ B OR C");
        op = (BinaryOperation) builder.visit(parser.dm_expression());
        assertEquals("OR", op.operator());
        BinaryOperation left = (BinaryOperation) op.left();
        assertEquals("EQ", left.operator());
        assertEquals("A", ((Identifier) left.left()).name());
        assertEquals("B", ((Identifier) left.right()).name());
        BinaryOperation right = (BinaryOperation) op.right();
        assertEquals("EQ", right.operator());
        assertEquals("A", ((Identifier) right.left()).name());
        assertEquals("C", ((Identifier) right.right()).name());
    }

    @Test
    public void testIncludesExcludes() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // INCLUDES
        WebFocusReportParser parser = createParser("A INCLUDES B AND C");
        BinaryOperation op = (BinaryOperation) builder.visit(parser.dm_expression());
        assertEquals("AND", op.operator());
        BinaryOperation left = (BinaryOperation) op.left();
        assertEquals("CONTAINS", left.operator());
        assertEquals("A", ((Identifier) left.left()).name());
        assertEquals("B", ((Identifier) left.right()).name());
        BinaryOperation right = (BinaryOperation) op.right();
        assertEquals("CONTAINS", right.operator());
        assertEquals("A", ((Identifier) right.left()).name());
        assertEquals("C", ((Identifier) right.right()).name());
    }

    @Test
    public void testIfExpression() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();
        WebFocusReportParser parser = createParser("IF A EQ B THEN 1 ELSE 2");
        IfExpression ifExpr = (IfExpression) builder.visit(parser.dm_expression());

        BinaryOperation condition = (BinaryOperation) ifExpr.condition();
        assertEquals("EQ", condition.operator());
        assertEquals(1, ((Literal) ifExpr.thenExpression()).value());
        assertEquals(2, ((Literal) ifExpr.elseExpression()).value());
    }

    @Test
    public void testDecodeExpression() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // Without ELSE
        WebFocusReportParser parser = createParser("DECODE A (1 10 2 20)");
        DecodeExpression decodeExpr = (DecodeExpression) builder.visit(parser.dm_expression());
        assertEquals("A", ((Identifier) decodeExpr.expression()).name());
        assertEquals(2, decodeExpr.pairs().size());
        assertEquals(1, ((Literal) decodeExpr.pairs().get(0).search()).value());
        assertEquals(10, ((Literal) decodeExpr.pairs().get(0).result()).value());
        assertNull(decodeExpr.defaultValue());

        // With ELSE
        parser = createParser("DECODE A (1 10 ELSE 30)");
        decodeExpr = (DecodeExpression) builder.visit(parser.dm_expression());
        assertEquals(1, decodeExpr.pairs().size());
        assertEquals(30, ((Literal) decodeExpr.defaultValue()).value());
    }

    @Test
    public void testSetAndDefaultCommands() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // -SET
        WebFocusReportParser parser = createParser("-SET &VAR = 123;");
        SetDM setDM = (SetDM) builder.visit(parser.dm_command());
        assertEquals("&VAR", setDM.variable());
        assertEquals(123, ((Literal) setDM.expression()).value());

        // -DEFAULT
        parser = createParser("-DEFAULT &VAR = 'Hello';");
        DefaultDM defaultDM = (DefaultDM) builder.visit(parser.dm_command());
        assertEquals("&VAR", defaultDM.variable());
        assertEquals("Hello", ((Literal) defaultDM.expression()).value());
    }

    @Test
    public void testSetBasedExpressions() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // IS MISSING
        WebFocusReportParser parser = createParser("A IS MISSING");
        IsMissingExpression missingExpr = (IsMissingExpression) builder.visit(parser.dm_expression());
        assertEquals("A", ((Identifier) missingExpr.expression()).name());
        assertFalse(missingExpr.inverted());

        // IS NOT MISSING
        parser = createParser("A IS NOT MISSING");
        missingExpr = (IsMissingExpression) builder.visit(parser.dm_expression());
        assertTrue(missingExpr.inverted());

        // FROM...TO
        parser = createParser("A FROM 1 TO 10");
        BetweenExpression betweenExpr = (BetweenExpression) builder.visit(parser.dm_expression());
        assertEquals("A", ((Identifier) betweenExpr.expression()).name());
        assertEquals(1, ((Literal) betweenExpr.lower()).value());
        assertEquals(10, ((Literal) betweenExpr.upper()).value());

        // NOT FROM...TO
        parser = createParser("A NOT FROM 1 TO 10");
        UnaryOperation notBetween = (UnaryOperation) builder.visit(parser.dm_expression());
        assertEquals("NOT", notBetween.operator());
        assertTrue(notBetween.operand() instanceof BetweenExpression);

        // IN (list)
        parser = createParser("A IN (1, 2, 3)");
        InExpression inExpr = (InExpression) builder.visit(parser.dm_expression());
        assertEquals("A", ((Identifier) inExpr.expression()).name());
        assertEquals(3, inExpr.values().size());
        assertNull(inExpr.filename());

        // IN FILE
        parser = createParser("A IN FILE CAR");
        inExpr = (InExpression) builder.visit(parser.dm_expression());
        assertEquals("A", ((Identifier) inExpr.expression()).name());
        assertEquals(0, inExpr.values().size());
        assertEquals("CAR", inExpr.filename());
    }

    @Test
    public void testControlFlowCommands() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // -GOTO
        WebFocusReportParser parser = createParser("-GOTO TARGET;");
        Goto gotoNode = (Goto) builder.visit(parser.dm_command());
        assertEquals("TARGET", gotoNode.target());

        // -LABEL
        parser = createParser("-TARGET");
        Label labelNode = (Label) builder.visit(parser.dm_command());
        assertEquals("TARGET", labelNode.name());

        // -IF
        parser = createParser("-IF &VAR EQ 1 THEN GOTO TARGET1 ELSE GOTO TARGET2;");
        IfDM ifDM = (IfDM) builder.visit(parser.dm_command());
        assertTrue(ifDM.condition() instanceof BinaryOperation);
        assertEquals("TARGET1", ifDM.thenTarget());
        assertEquals("TARGET2", ifDM.elseTarget());

        // -IF without ELSE
        parser = createParser("-IF &VAR EQ 1 THEN GOTO TARGET1;");
        ifDM = (IfDM) builder.visit(parser.dm_command());
        assertEquals("TARGET1", ifDM.thenTarget());
        assertNull(ifDM.elseTarget());
    }

    @Test
    public void testFunctionCall() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // ABS(HEIGHT)
        WebFocusReportParser parser = createParser("ABS(HEIGHT)");
        FunctionCall call = (FunctionCall) builder.visit(parser.dm_expression());
        assertEquals("ABS", call.functionName());
        assertEquals(1, call.arguments().size());
        assertEquals("HEIGHT", ((Identifier) call.arguments().get(0)).name());

        // MAX(1, 2) - testing multiple arguments if supported by grammar
        parser = createParser("MAX(1, 2)");
        call = (FunctionCall) builder.visit(parser.dm_expression());
        assertEquals("MAX", call.functionName());
        assertEquals(2, call.arguments().size());
        assertEquals(1, ((Literal) call.arguments().get(0)).value());
        assertEquals(2, ((Literal) call.arguments().get(1)).value());
    }

    @Test
    public void testExecutionControlCommands() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // -RUN
        WebFocusReportParser parser = createParser("-RUN;");
        RunDM runDM = (RunDM) builder.visit(parser.dm_command());
        assertNotNull(runDM);

        // -EXIT
        parser = createParser("-EXIT;");
        ExitDM exitDM = (ExitDM) builder.visit(parser.dm_command());
        assertNotNull(exitDM);
    }

    @Test
    public void testIncludeCommand() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();
        WebFocusReportParser parser = createParser("-INCLUDE MYFILE;");
        IncludeDM includeDM = (IncludeDM) builder.visit(parser.dm_command());
        assertEquals("MYFILE", includeDM.filename());
    }

    @Test
    public void testHtmlFormCommand() {
        WebFocusReportASGBuilder builder = new WebFocusReportASGBuilder();

        // File-based
        WebFocusReportParser parser = createParser("-HTMLFORM MYFORM;");
        HtmlFormDM formDM = (HtmlFormDM) builder.visit(parser.dm_command());
        assertEquals("MYFORM", formDM.filename());
        assertNull(formDM.content());

        // Block-based
        parser = createParser("-HTMLFORM BEGIN\n<html><body>Hello</body></html>\n-HTMLFORM END");
        formDM = (HtmlFormDM) builder.visit(parser.dm_command());
        assertNull(formDM.filename());
        assertTrue(formDM.content().contains("<html><body>Hello</body></html>"));
    }

    private WebFocusReportParser createParser(String input) {
        WebFocusReportLexer lexer = new WebFocusReportLexer(CharStreams.fromString(input));
        return new WebFocusReportParser(new CommonTokenStream(lexer));
    }
}
