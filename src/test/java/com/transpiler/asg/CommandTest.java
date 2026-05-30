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

    @Test
    void testSetDM() {
        Expression expr = new Literal(100);
        SetDM setDM = new SetDM("&MYVAR", expr);

        assertEquals("&MYVAR", setDM.variable());
        assertEquals(expr, setDM.expression());
        assertTrue(setDM instanceof Command);
    }

    @Test
    void testDefaultDM() {
        Expression expr = new Literal("DEFAULT_VAL");
        DefaultDM defaultDM = new DefaultDM("&MYVAR", expr);

        assertEquals("&MYVAR", defaultDM.variable());
        assertEquals(expr, defaultDM.expression());
        assertTrue(defaultDM instanceof Command);
    }

    @Test
    void testReadDM() {
        ReadDM readDM = new java.util.ArrayList<String>() {{
            add("&VAR1");
            add("&VAR2");
        }}.stream().collect(java.util.stream.Collectors.collectingAndThen(
            java.util.stream.Collectors.toList(),
            vars -> new ReadDM("MYFILE", vars)
        ));

        assertEquals("MYFILE", readDM.filename());
        assertEquals(2, readDM.variables().size());
        assertEquals("&VAR1", readDM.variables().get(0));
        assertTrue(readDM instanceof Command);
    }

    @Test
    void testWriteDM() {
        WriteDM writeDM = new WriteDM("LOGFILE", java.util.List.of("Message 1", "Message 2"));

        assertEquals("LOGFILE", writeDM.filename());
        assertEquals(2, writeDM.messages().size());
        assertEquals("Message 1", writeDM.messages().get(0));
        assertTrue(writeDM instanceof Command);
    }

    @Test
    void testHtmlFormDM() {
        HtmlFormDM htmlFormDM = new HtmlFormDM("TEMPLATE.HTML", null);
        assertEquals("TEMPLATE.HTML", htmlFormDM.filename());
        assertNull(htmlFormDM.content());

        HtmlFormDM htmlBlock = new HtmlFormDM(null, "<html><body>Hello</body></html>");
        assertNull(htmlBlock.filename());
        assertEquals("<html><body>Hello</body></html>", htmlBlock.content());
        assertTrue(htmlFormDM instanceof Command);
    }
}
