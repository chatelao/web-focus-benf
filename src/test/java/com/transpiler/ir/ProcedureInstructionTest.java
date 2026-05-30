package com.transpiler.ir;

import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

class ProcedureInstructionTest {

    @Test
    void testType() {
        List<String> messages = List.of("Hello", "World");
        Type type = new Type(messages);
        assertEquals(messages, type.messages());

        // Verify immutability
        List<String> mutableMessages = new ArrayList<>();
        mutableMessages.add("Test");
        Type type2 = new Type(mutableMessages);
        mutableMessages.add("Changed");
        assertEquals(1, type2.messages().size());
        assertEquals("Test", type2.messages().get(0));
        assertThrows(UnsupportedOperationException.class, () -> type2.messages().add("New"));
    }

    @Test
    void testCall() {
        List<String> args = List.of("arg1", "arg2");
        Call call = new Call("proc.fex", args);
        assertEquals("proc.fex", call.target());
        assertEquals(args, call.arguments());

        // Verify immutability
        List<String> mutableArgs = new ArrayList<>();
        mutableArgs.add("a");
        Call call2 = new Call("target", mutableArgs);
        mutableArgs.add("b");
        assertEquals(1, call2.arguments().size());
        assertThrows(UnsupportedOperationException.class, () -> call2.arguments().add("c"));
    }

    @Test
    void testHtmlForm() {
        HtmlForm form = new HtmlForm("template.html", "<html></html>");
        assertEquals("template.html", form.filename());
        assertEquals("<html></html>", form.content());
    }

    @Test
    void testRead() {
        List<String> vars = List.of("&VAR1", "&VAR2");
        Read read = new Read("data.txt", vars);
        assertEquals("data.txt", read.filename());
        assertEquals(vars, read.variables());

        // Verify immutability
        List<String> mutableVars = new ArrayList<>();
        mutableVars.add("v");
        Read read2 = new Read("file", mutableVars);
        mutableVars.add("v2");
        assertEquals(1, read2.variables().size());
    }

    @Test
    void testWrite() {
        List<String> msgs = List.of("Line 1", "Line 2");
        Write write = new Write("output.txt", msgs);
        assertEquals("output.txt", write.filename());
        assertEquals(msgs, write.messages());

        // Verify immutability
        List<String> mutableMsgs = new ArrayList<>();
        mutableMsgs.add("m");
        Write write2 = new Write("file", mutableMsgs);
        mutableMsgs.add("m2");
        assertEquals(1, write2.messages().size());
    }
}
