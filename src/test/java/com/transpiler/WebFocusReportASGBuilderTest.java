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
}
