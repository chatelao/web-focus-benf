package com.transpiler.ir;

import com.transpiler.asg.Expression;
import com.transpiler.asg.Literal;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

class ProcedureInstructionTest {

    @Test
    void testType() {
        List<Expression> messages = List.of(new Literal("Hello"), new Literal("World"));
        Type type = new Type(messages);
        assertEquals(messages, type.messages());

        // Verify immutability
        List<Expression> mutableMessages = new ArrayList<>();
        mutableMessages.add(new Literal("Test"));
        Type type2 = new Type(mutableMessages);
        mutableMessages.add(new Literal("Changed"));
        assertEquals(1, type2.messages().size());
        assertEquals(new Literal("Test"), type2.messages().get(0));
        assertThrows(UnsupportedOperationException.class, () -> type2.messages().add(new Literal("New")));
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
        List<Expression> msgs = List.of(new Literal("Line 1"), new Literal("Line 2"));
        Write write = new Write("output.txt", msgs);
        assertEquals("output.txt", write.filename());
        assertEquals(msgs, write.messages());

        // Verify immutability
        List<Expression> mutableMsgs = new ArrayList<>();
        mutableMsgs.add(new Literal("m"));
        Write write2 = new Write("file", mutableMsgs);
        mutableMsgs.add(new Literal("m2"));
        assertEquals(1, write2.messages().size());
    }
}
