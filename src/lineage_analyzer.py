import ir
from ir_utils import collect_fields_from_expression

class LineageAnalyzer:
    """
    Analyzes the Control Flow Graph to track field usage and data lineage.
    """
    def __init__(self):
        pass

    def analyze(self, cfg):
        """
        Traverses the CFG and collects field usage from report and match instructions.
        Returns a dictionary of usage information.
        """
        lineage = {
            'fields': {
                'select': set(),
                'sort': set(),
                'filter': set()
            },
            'sources': set(),
            'targets': set()
        }

        if not cfg:
            return lineage

        for block in cfg.blocks.values():
            for instr in block.instructions:
                if isinstance(instr, ir.Report):
                    lineage['sources'].add(instr.filename)
                    self._analyze_report(instr, lineage)
                elif isinstance(instr, ir.Match):
                    lineage['sources'].add(instr.filename)
                    self._analyze_match(instr, lineage)
                elif isinstance(instr, ir.Join):
                    lineage['sources'].add(instr.right_file)
                elif isinstance(instr, ir.Define):
                    lineage['sources'].add(instr.filename)

        # Convert sets to sorted lists for stable output
        lineage['fields']['select'] = sorted(list(lineage['fields']['select']))
        lineage['fields']['sort'] = sorted(list(lineage['fields']['sort']))
        lineage['fields']['filter'] = sorted(list(lineage['fields']['filter']))
        lineage['sources'] = sorted(list(lineage['sources']))
        lineage['targets'] = sorted(list(lineage['targets']))

        return lineage

    def _analyze_report(self, instr, lineage):
        """Analyzes an ir.Report instruction for field usage."""
        for comp in instr.components:
            self._analyze_component(comp, lineage)

    def _analyze_match(self, instr, lineage):
        """Analyzes an ir.Match instruction for field usage."""
        # Main file components
        for comp in instr.components:
            self._analyze_component(comp, lineage)

        # Sub-matches
        for sub in instr.sub_matches:
            lineage['sources'].add(sub.filename)
            for comp in sub.components:
                self._analyze_component(comp, lineage)
            if sub.after_match and sub.after_match.output_command:
                self._analyze_component(sub.after_match.output_command, lineage)

    def _analyze_component(self, comp, lineage):
        """Analyzes a report component and categorizes field usage."""
        class_name = comp.__class__.__name__

        def mark_select(name, source_fn=None):
            lineage['fields']['select'].add(name)

        def mark_sort(name, source_fn=None):
            lineage['fields']['sort'].add(name)

        def mark_filter(name, source_fn=None):
            lineage['fields']['filter'].add(name)

        if class_name == 'VerbCommand':
            for f in comp.fields:
                if f.name != '*':
                    lineage['fields']['select'].add(f.name)
        elif class_name == 'SortCommand':
            lineage['fields']['sort'].add(comp.field.name)
        elif class_name == 'ComputeCommand':
            collect_fields_from_expression(comp.expression, mark_select)
        elif class_name == 'WhereClause':
            collect_fields_from_expression(comp.condition, mark_filter)
        elif class_name == 'WhenCommand':
            collect_fields_from_expression(comp.condition, mark_filter)
        elif class_name == 'OnCommand':
            for action in comp.actions:
                self._analyze_component(action, lineage)
        elif class_name == 'OutputCommand':
            if comp.filename:
                lineage['targets'].add(comp.filename)
