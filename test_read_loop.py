from wf_parser import WebFocusParser
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from ssa_transformer import SSATransformer
from optimizer import ConstantPropagator

fex = """
-SET &I = 1;
-REPEAT LBL WHILE &I LE 10;
-READ MYFILE &VAR
-SET &I = &I + 1;
-LBL
"""

parser = WebFocusParser()
asg_builder = ReportASGBuilder()
ir_builder = IRBuilder()
ssa_transformer = SSATransformer()

tree = parser.parse(fex)
asg_nodes = asg_builder.visit(tree)
cfg = ir_builder.build(asg_nodes)
ssa_transformer.transform(cfg)

for block_name, block in cfg.blocks.items():
    print(f"Block: {block_name}")
    for instr in block.instructions:
        print(f"  {instr}")
    print(f"  Successors: {[b.name for b in block.successors]}")
