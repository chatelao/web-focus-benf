package com.transpiler;

import com.transpiler.asg.ASGNode;
import com.transpiler.asg.ReportRequest;
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
}
