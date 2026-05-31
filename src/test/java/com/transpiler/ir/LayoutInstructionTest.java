package com.transpiler.ir;

import com.transpiler.asg.OutputCommand;
import com.transpiler.asg.ReportRequest;
import org.junit.jupiter.api.Test;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

class LayoutInstructionTest {

    @Test
    void testCompoundLayoutInstructions() {
        OutputCommand hold = new OutputCommand("PCHOLD", "REPORT1", "PDF", null);
        ReportRequest report = new ReportRequest("EMPLOYEE");

        CompoundLayout layout = new CompoundLayout(hold, List.of(report));
        assertEquals(hold, layout.outputCommand());
        assertEquals(1, layout.statements().size());
        assertEquals(report, layout.statements().get(0));

        CompoundEnd end = new CompoundEnd();
        assertNotNull(end);
        assertTrue(end instanceof Instruction);
    }
}
