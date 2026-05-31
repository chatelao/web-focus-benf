package com.transpiler.ir;

import com.transpiler.asg.FieldSelection;
import com.transpiler.asg.MoreClause;
import com.transpiler.asg.MoreSubRequest;
import com.transpiler.asg.VerbCommand;
import com.transpiler.asg.WhereClause;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

class RelationalInstructionTest {

    @Test
    void testReportInstruction() {
        Join join = new Join("EMP", "ID", "SAL", "ID", "EMPSAL", true, true);
        VerbCommand verb = new VerbCommand("PRINT", List.of(new FieldSelection("LASTNAME")));
        MoreClause more = new MoreClause(List.of(new MoreSubRequest("FILE2", List.of())));

        Report report = new Report("EMPLOYEE", List.of(verb), List.of(join), more);

        assertEquals("EMPLOYEE", report.filename());
        assertEquals(1, report.components().size());
        assertEquals(1, report.joins().size());
        assertEquals(more, report.moreClause());
    }

    @Test
    void testMatchInstruction() {
        FieldSelection field = new FieldSelection("ID");
        Match match = new Match("MAINFILE", List.of(field), List.of(), null);

        assertEquals("MAINFILE", match.filename());
        assertEquals(1, match.components().size());
        assertTrue(match.subMatches().isEmpty());
        assertNull(match.moreClause());
    }

    @Test
    void testDefineInstruction() {
        Define define = new Define("EMPLOYEE", List.of(Map.of("name", "FULLNAME", "expression", "FIRSTNAME || LASTNAME")));
        assertEquals("EMPLOYEE", define.filename());
        assertEquals(1, define.assignments().size());
        assertEquals("FULLNAME", define.assignments().get(0).get("name"));
    }

    @Test
    void testJoinInstruction() {
        Join join = new Join("EMP", "ID", "SAL", "ID", "EMPSAL", true, true);
        assertEquals("EMP", join.leftFile());
        assertEquals("ID", join.leftField());
        assertEquals("SAL", join.rightFile());
        assertEquals("ID", join.rightField());
        assertEquals("EMPSAL", join.joinAs());
        assertTrue(join.outer());
        assertTrue(join.isAll());
    }

    @Test
    void testJoinClearInstruction() {
        JoinClear joinClear = new JoinClear();
        assertNotNull(joinClear);
        assertTrue(joinClear instanceof Instruction);
    }
}
