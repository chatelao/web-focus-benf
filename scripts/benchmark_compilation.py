import time
import os
import sys
from antlr4 import CommonTokenStream, InputStream

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from ssa_transformer import SSATransformer
from emitter import PostgresEmitter
from metadata_registry import MetadataRegistry

def benchmark_sample(filepath):
    with open(filepath, 'r') as f:
        code = f.read()

    start_time = time.perf_counter()

    # 1. Parsing
    input_stream = InputStream(code)
    lexer = WebFocusReportLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WebFocusReportParser(token_stream)
    tree = parser.start()
    parse_time = time.perf_counter()

    # 2. ASG Construction
    builder = ReportASGBuilder()
    asg_nodes = builder.visit(tree)
    asg_time = time.perf_counter()

    # 3. IR Construction
    ir_builder = IRBuilder()
    cfg = ir_builder.build(asg_nodes)
    ir_time = time.perf_counter()

    # 4. SSA Transformation
    ssa_transformer = SSATransformer()
    ssa_transformer.transform(cfg)
    ssa_time = time.perf_counter()

    # 5. Backend Emission
    metadata = MetadataRegistry()
    emitter = PostgresEmitter(metadata_registry=metadata)
    emitter.emit(cfg)
    emit_time = time.perf_counter()

    total_time = emit_time - start_time

    return {
        'total': total_time,
        'parse': parse_time - start_time,
        'asg': asg_time - parse_time,
        'ir': ir_time - asg_time,
        'ssa': ssa_time - ir_time,
        'emit': emit_time - ssa_time
    }

def main():
    samples_dir = os.path.join(os.path.dirname(__file__), '..', 'test', 'samples')
    doc_examples_dir = os.path.join(os.path.dirname(__file__), '..', 'test', 'documentation_examples')

    all_samples = []
    for d in [samples_dir, doc_examples_dir]:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.endswith('.fex'):
                    all_samples.append(os.path.join(d, f))

    print(f"{'Sample':<40} | {'Total (ms)':>10} | {'Parse':>8} | {'ASG':>8} | {'IR':>8} | {'SSA':>8} | {'Emit':>8}")
    print("-" * 105)

    totals = {'total': 0, 'parse': 0, 'asg': 0, 'ir': 0, 'ssa': 0, 'emit': 0}
    count = 0

    for sample in sorted(all_samples):
        try:
            results = benchmark_sample(sample)
            name = os.path.basename(sample)
            print(f"{name:<40} | {results['total']*1000:>10.2f} | {results['parse']*1000:>8.2f} | {results['asg']*1000:>8.2f} | {results['ir']*1000:>8.2f} | {results['ssa']*1000:>8.2f} | {results['emit']*1000:>8.2f}")

            for k in totals:
                totals[k] += results[k]
            count += 1
        except Exception as e:
            print(f"Error benchmarking {sample}: {e}")

    if count > 0:
        print("-" * 105)
        print(f"{'AVERAGE':<40} | {totals['total']/count*1000:>10.2f} | {totals['parse']/count*1000:>8.2f} | {totals['asg']/count*1000:>8.2f} | {totals['ir']/count*1000:>8.2f} | {totals['ssa']/count*1000:>8.2f} | {totals['emit']/count*1000:>8.2f}")

if __name__ == "__main__":
    main()
