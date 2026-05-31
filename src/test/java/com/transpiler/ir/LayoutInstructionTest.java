package com.transpiler.ir;

import com.transpiler.asg.OutputCommand;
import org.junit.jupiter.api.Test;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

class LayoutInstructionTest {

    @Test
    void testCompoundLayoutInstruction() {
        OutputCommand output = new OutputCommand("HOLD", "MYFILE", "FORMAT", null);
        CompoundLayout layout = new CompoundLayout(output, List.of());
        assertEquals(output, layout.outputCommand());
        assertTrue(layout.statements().isEmpty());
    }

    @Test
    void testCompoundEndInstruction() {
        CompoundEnd end = new CompoundEnd();
        assertNotNull(end);
        assertTrue(end instanceof Instruction);
    }
}
