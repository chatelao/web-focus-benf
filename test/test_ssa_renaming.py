import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import ir
from ssa_transformer import SSATransformer
import asg

def test_rename_linear():
    # ENTRY: X = 1; Y = X + 1; X = 2; Z = X + Y
    cfg = ir.ControlFlowGraph()
    entry = ir.BasicBlock("ENTRY")
    cfg.add_block(entry)
    cfg.entry_block = entry

    entry.add_instruction(ir.Assign(target="X", source=asg.Literal(1)))
    entry.add_instruction(ir.Assign(target="Y", source=asg.BinaryOperation(asg.AmperVar("X"), "+", asg.Literal(1))))
    entry.add_instruction(ir.Assign(target="X", source=asg.Literal(2)))
    entry.add_instruction(ir.Assign(target="Z", source=asg.BinaryOperation(asg.AmperVar("X"), "+", asg.AmperVar("Y"))))

    transformer = SSATransformer()
    transformer.place_phi_nodes(cfg)
    transformer.rename_variables(cfg)

    instrs = entry.instructions
    assert instrs[0].target == "X_0"

    assert instrs[1].target == "Y_0"
    assert instrs[1].source.left.name == "X_0"

    assert instrs[2].target == "X_1"

    assert instrs[3].target == "Z_0"
    assert instrs[3].source.left.name == "X_1"
    assert instrs[3].source.right.name == "Y_0"

def test_rename_diamond():
    # ENTRY -> B1, ENTRY -> B2, B1 -> B3, B2 -> B3
    # ENTRY: X = 0
    # B1: X = 1
    # B2: X = 2
    # B3: Y = X
    cfg = ir.ControlFlowGraph()
    entry = ir.BasicBlock("ENTRY")
    b1 = ir.BasicBlock("B1")
    b2 = ir.BasicBlock("B2")
    b3 = ir.BasicBlock("B3")

    cfg.add_block(entry)
    cfg.add_block(b1)
    cfg.add_block(b2)
    cfg.add_block(b3)
    cfg.entry_block = entry

    cfg.add_edge("ENTRY", "B1")
    cfg.add_edge("ENTRY", "B2")
    cfg.add_edge("B1", "B3")
    cfg.add_edge("B2", "B3")

    entry.add_instruction(ir.Assign(target="X", source=asg.Literal(0)))
    b1.add_instruction(ir.Assign(target="X", source=asg.Literal(1)))
    b2.add_instruction(ir.Assign(target="X", source=asg.Literal(2)))
    b3.add_instruction(ir.Assign(target="Y", source=asg.AmperVar("X")))

    transformer = SSATransformer()
    transformer.place_phi_nodes(cfg)
    transformer.rename_variables(cfg)

    # Check Phi in B3
    phi = [i for i in b3.instructions if isinstance(i, ir.Phi)][0]
    assert phi.target == "X_3"
    assert "X_1" in phi.sources # from B1
    assert "X_2" in phi.sources # from B2

    # Check use of X in B3
    use_instr = [i for i in b3.instructions if isinstance(i, ir.Assign)][0]
    assert use_instr.target == "Y_0"
    assert use_instr.source.name == "X_3"

def test_rename_loop():
    # ENTRY: X = 0
    # HEADER: Phi(X)
    # BODY: X = X + 1
    # HEADER -> BODY, BODY -> HEADER, HEADER -> EXIT
    cfg = ir.ControlFlowGraph()
    entry = ir.BasicBlock("ENTRY")
    header = ir.BasicBlock("HEADER")
    body = ir.BasicBlock("BODY")
    exit_b = ir.BasicBlock("EXIT")

    cfg.add_block(entry)
    cfg.add_block(header)
    cfg.add_block(body)
    cfg.add_block(exit_b)
    cfg.entry_block = entry

    cfg.add_edge("ENTRY", "HEADER")
    cfg.add_edge("HEADER", "BODY")
    cfg.add_edge("BODY", "HEADER")
    cfg.add_edge("HEADER", "EXIT")

    entry.add_instruction(ir.Assign(target="X", source=asg.Literal(0)))
    body.add_instruction(ir.Assign(target="X", source=asg.BinaryOperation(asg.AmperVar("X"), "+", asg.Literal(1))))

    transformer = SSATransformer()
    transformer.place_phi_nodes(cfg)
    transformer.rename_variables(cfg)

    # Header Phi
    phi = [i for i in header.instructions if isinstance(i, ir.Phi)][0]
    # entry defines X_0
    # body defines X_1
    # Phi defines X_2 (since it's processed in HEADER)
    print(f"Phi target: {phi.target}")
    print(f"Phi sources: {phi.sources}")

    # Body assignment
    assign = body.instructions[0]
    print(f"Body assign target: {assign.target}")
    print(f"Body assign source: {assign.source.left.name}")

    assert phi.target == "X_1"
    assert "X_0" in phi.sources
    assert "X_2" in phi.sources

    assert assign.target == "X_2"
    assert assign.source.left.name == "X_1"

def test_rename_complex_instrs():
    # ENTRY: &VAR = 10; DEFINE FILE X: F = &VAR; TABLE FILE X: WHERE G EQ &VAR; COMPUTE H = &VAR; END
    cfg = ir.ControlFlowGraph()
    entry = ir.BasicBlock("ENTRY")
    cfg.add_block(entry)
    cfg.entry_block = entry

    # &VAR = 10
    entry.add_instruction(ir.Assign(target="&VAR", source=asg.Literal(10)))

    # DEFINE FILE X: F = &VAR;
    define_instr = ir.Define(filename="X", assignments=[
        asg.DefineAssignment(name="F", expression=asg.AmperVar("&VAR"))
    ])
    entry.add_instruction(define_instr)

    # TABLE FILE X: WHERE G EQ &VAR; COMPUTE H = &VAR; END
    report_instr = ir.Report(filename="X", components=[
        asg.WhereClause(condition=asg.BinaryOperation(asg.Identifier("G"), "EQ", asg.AmperVar("&VAR"))),
        asg.ComputeCommand(name="H", expression=asg.AmperVar("&VAR"))
    ])
    entry.add_instruction(report_instr)

    transformer = SSATransformer()
    transformer.place_phi_nodes(cfg)
    transformer.rename_variables(cfg)

    # Check definitions
    assert entry.instructions[0].target == "&VAR_0"

    # Check DEFINE use
    assert define_instr.assignments[0].expression.name == "&VAR_0"

    # Check Report uses
    where_clause = report_instr.components[0]
    compute_cmd = report_instr.components[1]

    assert where_clause.condition.right.name == "&VAR_0"
    assert compute_cmd.expression.name == "&VAR_0"

if __name__ == "__main__":
    test_rename_linear()
    test_rename_diamond()
    test_rename_loop()
    test_rename_complex_instrs()
    print("All tests passed!")
