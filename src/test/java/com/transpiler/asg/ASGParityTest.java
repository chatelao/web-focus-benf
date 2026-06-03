package com.transpiler.asg;

import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import static org.junit.jupiter.api.Assertions.*;

class ASGParityTest {

    @Test
    void testExpressionInstantiation() {
        // In Java, Expression is an interface, so we test one of its implementations
        Expression expr = new Literal(1);
        assertTrue(expr instanceof Expression);
    }

    @Test
    void testOutputAndMatchNodes() {
        OutputCommand hold = new OutputCommand("HOLD", "MYHOLD", "FOCUS", null);
        assertEquals("HOLD", hold.outputType());
        assertEquals("MYHOLD", hold.filename());

        MoreSubRequest moreSub = new MoreSubRequest("FILE2", List.of(new WhereClause(new BinaryOperation(new Identifier("COUNTRY"), "EQ", new Literal("USA")), false)));
        MoreClause more = new MoreClause(List.of(moreSub));
        assertEquals(1, more.subRequests().size());
        assertEquals("FILE2", more.subRequests().get(0).filename());

        AfterMatchPhrase after = new AfterMatchPhrase("OLD-OR-NEW", hold);
        SubMatch subMatch = new SubMatch("FILE1", List.of(new FieldSelection("ID")), null, after);

        MatchRequest match = new MatchRequest("MAINFILE", List.of(new FieldSelection("ID")), more, List.of(subMatch));
        assertEquals("MAINFILE", match.filename());
        assertEquals(more, match.moreClause());
        assertEquals(1, match.subMatches().size());
        assertEquals(after, match.subMatches().get(0).afterMatch());
    }

    @Test
    void testStatementInstantiation() {
        // In Java, Statement is an interface, so we test one of its implementations
        Statement stmt = new ReportRequest("EMPLOYEE");
        assertTrue(stmt instanceof Statement);
    }

    @Test
    void testCommandInstantiation() {
        // In Java, Command is an interface, so we test one of its implementations
        Command cmd = new RunDM();
        assertTrue(cmd instanceof Command);
    }

    @Test
    void testMasterFileNode() {
        MasterFile mf = new MasterFile("EMPLOYEE", "FOC");
        assertEquals("EMPLOYEE", mf.name());
        assertEquals("FOC", mf.suffix());
        assertTrue(mf.segments().isEmpty());
    }

    @Test
    void testSegmentNode() {
        Segment seg = new Segment("EMPDATA", "S1");
        assertEquals("EMPDATA", seg.name());
        assertEquals("S1", seg.segtype());
        assertTrue(seg.fields().isEmpty());
    }

    @Test
    void testFieldNode() {
        Field fld = new Field("LASTNAME", "LN", "A15");
        assertEquals("LASTNAME", fld.name());
        assertEquals("LN", fld.alias());
        assertEquals("A15", fld.format());
    }

    @Test
    void testNodeNesting() {
        Field fld = new Field("LASTNAME", "LN", "A15");
        Field virtualFld = new Field("FULLNAME", null, "A30");
        Segment seg = new Segment("EMPDATA", "S1", "EMPLOYEE", List.of(fld), List.of(virtualFld));

        Dimension dim = new Dimension("TIME");
        Hierarchy hier = new Hierarchy("YEAR_MONTH");
        MasterFile mf = new MasterFile("EMPLOYEE", "FOC", List.of(seg), List.of(virtualFld), List.of(dim), List.of(hier));

        assertEquals(1, mf.segments().size());
        assertEquals("EMPDATA", mf.segments().get(0).name());
        assertEquals(1, mf.segments().get(0).fields().size());
        assertEquals("LASTNAME", mf.segments().get(0).fields().get(0).name());
        assertEquals(1, mf.segments().get(0).virtualFields().size());
        assertEquals("FULLNAME", mf.segments().get(0).virtualFields().get(0).name());

        assertEquals(1, mf.virtualFields().size());
        assertEquals("FULLNAME", mf.virtualFields().get(0).name());
        assertEquals(1, mf.dimensions().size());
        assertEquals("TIME", mf.dimensions().get(0).name());
        assertEquals(1, mf.hierarchies().size());
        assertEquals("YEAR_MONTH", mf.hierarchies().get(0).name());
    }

    @Test
    void testDmControlFlowNodes() {
        Goto gotoNode = new Goto("EXIT_REPORT");
        assertEquals("EXIT_REPORT", gotoNode.target());

        Label labelNode = new Label("EXIT_REPORT");
        assertEquals("EXIT_REPORT", labelNode.name());

        Expression condition = new BinaryOperation(new AmperVar("&VAR"), "EQ", new Literal(1));
        IfDM ifNode = new IfDM(condition, "LABEL1", "LABEL2");
        assertEquals(condition, ifNode.condition());
        assertEquals("LABEL1", ifNode.thenTarget());
        assertEquals("LABEL2", ifNode.elseTarget());

        Repeat repeatNode = new Repeat("LOOP_START");
        assertEquals("LOOP_START", repeatNode.label());
    }

    @Test
    void testDmActionNodes() {
        SetDM setNode = new SetDM("&VAR", new Literal("100"));
        assertEquals("&VAR", setNode.variable());
        assertEquals(new Literal("100"), setNode.expression());

        TypeDM typeNode = new TypeDM(List.of(new Literal("Hello"), new Literal("World")));
        assertEquals(List.of(new Literal("Hello"), new Literal("World")), typeNode.messages());

        IncludeDM includeNode = new IncludeDM("MYFEX.FEX");
        assertEquals("MYFEX.FEX", includeNode.filename());

        RunDM runNode = new RunDM();
        assertNotNull(runNode);

        ExitDM exitNode = new ExitDM();
        assertNotNull(exitNode);
    }

    @Test
    void testReportRequestNodes() {
        ReportRequest report = new ReportRequest("EMPLOYEE");
        assertEquals("EMPLOYEE", report.filename());
        assertTrue(report.components().isEmpty());

        VerbCommand verb = new VerbCommand("PRINT", List.of(new FieldSelection("LASTNAME")));
        assertEquals("PRINT", verb.verb());
        assertEquals("LASTNAME", verb.fields().get(0).name());

        SortCommand sort = new SortCommand("BY", new FieldSelection("DEPARTMENT"));
        assertEquals("BY", sort.sortType());
        assertEquals("DEPARTMENT", sort.field().name());

        Expression whereCond = new BinaryOperation(new Identifier("SALARY"), "GT", new Literal(50000));
        WhereClause where = new WhereClause(whereCond, false);
        assertEquals(whereCond, where.condition());
        assertFalse(where.isTotal());

        Heading heading = new Heading("Employee Report", true);
        assertEquals("Employee Report", heading.text());
        assertTrue(heading.centered());

        Footing footing = new Footing("End of Report");
        assertEquals("End of Report", footing.text());
        assertFalse(footing.centered());

        OnCommand onTable = new OnCommand("TABLE", List.of(new SetCommand("COLUMN-TOTAL", "ON")));
        assertEquals("TABLE", onTable.target());
        assertEquals("COLUMN-TOTAL", ((SetCommand)onTable.actions().get(0)).parameter());

        ComputeCommand compute = new ComputeCommand("BONUS", new BinaryOperation(new Identifier("SALARY"), "*", new Literal(0.1)), "D12.2");
        assertEquals("BONUS", compute.name());
        assertTrue(compute.expression() instanceof BinaryOperation);
        assertEquals("D12.2", compute.format());
    }

    @Test
    void testEnvironmentAndVirtualFieldNodes() {
        Join join = new Join("EMP", "ID", "SAL", "ID", "EMPSAL", true, false);
        assertEquals("EMP", join.leftFile());
        assertEquals("EMPSAL", join.joinAs());
        assertTrue(join.outer());
        assertFalse(join.isAll());

        Join joinAll = new Join("EMP", "ID", "SAL", "ID", "EMPSAL", false, true);
        assertTrue(joinAll.isAll());

        JoinClear joinClear = new JoinClear();
        assertNotNull(joinClear);

        SetCommand setCmd = new SetCommand("NODATA", "MISSING");
        assertEquals("NODATA", setCmd.parameter());
        assertEquals("MISSING", setCmd.value());

        DefineFile define = new DefineFile("EMPLOYEE", List.of(Map.of("name", "FULLNAME", "expression", "FIRSTNAME || LASTNAME")));
        assertEquals("EMPLOYEE", define.filename());
        assertEquals(1, define.assignments().size());
    }

    @Test
    void testExpressionNodes() {
        Literal lit = new Literal(100);
        assertEquals(100, lit.value());

        Identifier ident = new Identifier("SALARY");
        assertEquals("SALARY", ident.name());

        AmperVar amper = new AmperVar("&DATE");
        assertEquals("&DATE", amper.name());

        BinaryOperation binOp = new BinaryOperation(ident, "+", lit);
        assertEquals(ident, binOp.left());
        assertEquals("+", binOp.operator());
        assertEquals(lit, binOp.right());

        UnaryOperation unOp = new UnaryOperation("NOT", binOp);
        assertEquals("NOT", unOp.operator());
        assertEquals(binOp, unOp.operand());

        FunctionCall func = new FunctionCall("ABS", List.of(lit));
        assertEquals("ABS", func.functionName());
        assertEquals(lit, func.arguments().get(0));

        IfExpression ifExpr = new IfExpression(ident, lit, new Literal(0));
        assertEquals(ident, ifExpr.condition());
        assertEquals(lit, ifExpr.thenExpression());
        assertEquals(0, ((Literal)ifExpr.elseExpression()).value());

        BetweenExpression between = new BetweenExpression(ident, new Literal(10), new Literal(20));
        assertEquals(ident, between.expression());
        assertEquals(10, ((Literal)between.lower()).value());
        assertEquals(20, ((Literal)between.upper()).value());

        InExpression inExpr = new InExpression(ident, List.of(new Literal(1), new Literal(2)));
        assertEquals(ident, inExpr.expression());
        assertEquals(2, inExpr.values().size());
    }
}
