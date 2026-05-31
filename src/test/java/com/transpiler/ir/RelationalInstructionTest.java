package com.transpiler.ir;

import org.junit.jupiter.api.Test;
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
}
