package com.transpiler.ir;

import com.transpiler.asg.DefineAssignment;
import org.junit.jupiter.api.Test;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

class RelationalInstructionTest {

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

    @Test
    void testDefineInstruction() {
        DefineAssignment assignment = new DefineAssignment("VAL", "EXPR", "A10");
        Define define = new Define("EMP", List.of(assignment));
        assertEquals("EMP", define.filename());
        assertEquals(1, define.assignments().size());
        assertEquals("VAL", define.assignments().get(0).name());
    }

    @Test
    void testReportInstruction() {
        Report report = new Report("EMP", java.util.List.of());
        assertEquals("EMP", report.filename());
        assertTrue(report.components().isEmpty());
        assertTrue(report.joins().isEmpty());
        assertNull(report.moreClause());
    }

    @Test
    void testMatchInstruction() {
        Match match = new Match("EMP", java.util.List.of());
        assertEquals("EMP", match.filename());
        assertTrue(match.components().isEmpty());
        assertTrue(match.subMatches().isEmpty());
        assertNull(match.moreClause());
    }
}
