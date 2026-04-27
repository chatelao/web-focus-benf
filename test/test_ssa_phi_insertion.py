import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import ir
from ssa_transformer import SSATransformer
import asg

def test_phi_insertion_diamond():
    # Diamond: B0 -> B1, B0 -> B2, B1 -> B3, B2 -> B3
    # X defined in B1 and B2. Phi(X) should be in B3.
    cfg = ir.ControlFlowGraph()
    b0 = ir.BasicBlock("B0")
    b1 = ir.BasicBlock("B1")
    b2 = ir.BasicBlock("B2")
    b3 = ir.BasicBlock("B3")

    cfg.add_block(b0)
    cfg.add_block(b1)
    cfg.add_block(b2)
    cfg.add_block(b3)

    cfg.add_edge("B0", "B1")
    cfg.add_edge("B0", "B2")
    cfg.add_edge("B1", "B3")
    cfg.add_edge("B2", "B3")

    b1.add_instruction(ir.Assign(target="X", source=asg.Literal(1)))
    b2.add_instruction(ir.Assign(target="X", source=asg.Literal(2)))

    transformer = SSATransformer()
    transformer.place_phi_nodes(cfg)

    # Check B3 has a Phi node for X
    phi_instrs = [i for i in b3.instructions if i.__class__.__name__ == 'Phi']
    assert len(phi_instrs) == 1
    assert phi_instrs[0].target == "X"
    assert len(phi_instrs[0].sources) == 2

def test_phi_insertion_loop():
    # Loop: ENTRY -> HEADER, HEADER -> BODY, BODY -> HEADER, HEADER -> EXIT
    # X defined in ENTRY and BODY. Phi(X) should be in HEADER.
    cfg = ir.ControlFlowGraph()
    entry = ir.BasicBlock("ENTRY")
    header = ir.BasicBlock("HEADER")
    body = ir.BasicBlock("BODY")
    exit_b = ir.BasicBlock("EXIT")

    cfg.add_block(entry)
    cfg.add_block(header)
    cfg.add_block(body)
    cfg.add_block(exit_b)

    cfg.add_edge("ENTRY", "HEADER")
    cfg.add_edge("HEADER", "BODY")
    cfg.add_edge("BODY", "HEADER")
    cfg.add_edge("HEADER", "EXIT")

    entry.add_instruction(ir.Assign(target="X", source=asg.Literal(0)))
    body.add_instruction(ir.Assign(target="X", source=asg.BinaryOperation(asg.AmperVar("X"), "+", asg.Literal(1))))

    transformer = SSATransformer()
    transformer.place_phi_nodes(cfg)

    # Check HEADER has a Phi node for X
    phi_instrs = [i for i in header.instructions if i.__class__.__name__ == 'Phi']
    assert len(phi_instrs) == 1
    assert phi_instrs[0].target == "X"
    assert len(phi_instrs[0].sources) == 2 # Predecessors: ENTRY and BODY

def test_phi_insertion_no_phi_needed():
    # Linear: B0 -> B1 -> B2
    # X defined in B0. No Phi needed.
    cfg = ir.ControlFlowGraph()
    b0 = ir.BasicBlock("B0")
    b1 = ir.BasicBlock("B1")
    b2 = ir.BasicBlock("B2")

    cfg.add_block(b0)
    cfg.add_block(b1)
    cfg.add_block(b2)

    cfg.add_edge("B0", "B1")
    cfg.add_edge("B1", "B2")

    b0.add_instruction(ir.Assign(target="X", source=asg.Literal(1)))

    transformer = SSATransformer()
    transformer.place_phi_nodes(cfg)

    for block in cfg.blocks.values():
        phi_instrs = [i for i in block.instructions if i.__class__.__name__ == 'Phi']
        assert len(phi_instrs) == 0

if __name__ == "__main__":
    test_phi_insertion_diamond()
    test_phi_insertion_loop()
    test_phi_insertion_no_phi_needed()
    print("All tests passed!")
