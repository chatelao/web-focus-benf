# Generated from src/WebFocusReport.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,60,257,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,5,1,61,8,1,10,1,12,1,64,9,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,3,3,75,8,3,1,4,1,4,1,5,3,5,80,8,5,1,5,1,5,3,
        5,84,8,5,1,5,5,5,87,8,5,10,5,12,5,90,9,5,1,6,1,6,1,6,1,6,1,6,3,6,
        97,8,6,1,7,1,7,1,7,5,7,102,8,7,10,7,12,7,105,9,7,1,7,1,7,1,8,1,8,
        3,8,111,8,8,1,9,1,9,1,9,1,10,1,10,1,11,3,11,119,8,11,1,11,1,11,3,
        11,123,8,11,1,11,1,11,3,11,127,8,11,1,11,3,11,130,8,11,1,12,1,12,
        3,12,134,8,12,1,12,1,12,3,12,138,8,12,1,13,1,13,3,13,142,8,13,1,
        13,3,13,145,8,13,1,14,1,14,3,14,149,8,14,1,14,4,14,152,8,14,11,14,
        12,14,153,1,15,1,15,3,15,158,8,15,1,15,4,15,161,8,15,11,15,12,15,
        162,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,172,8,16,1,17,1,17,3,
        17,176,8,17,1,17,4,17,179,8,17,11,17,12,17,180,1,17,1,17,1,17,1,
        17,3,17,187,8,17,1,18,1,18,3,18,191,8,18,1,18,4,18,194,8,18,11,18,
        12,18,195,1,18,3,18,199,8,18,1,19,1,19,3,19,203,8,19,1,19,1,19,3,
        19,207,8,19,1,19,3,19,210,8,19,1,19,3,19,213,8,19,1,20,1,20,1,20,
        1,20,5,20,219,8,20,10,20,12,20,222,9,20,1,20,1,20,1,20,4,20,227,
        8,20,11,20,12,20,228,3,20,231,8,20,1,21,1,21,1,21,3,21,236,8,21,
        1,21,1,21,1,21,3,21,241,8,21,3,21,243,8,21,1,22,1,22,1,23,1,23,1,
        23,5,23,250,8,23,10,23,12,23,253,9,23,1,24,1,24,1,24,0,0,25,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        0,6,1,0,5,10,1,0,14,17,1,0,25,26,1,0,28,31,1,0,34,37,2,0,6,6,40,
        54,280,0,50,1,0,0,0,2,53,1,0,0,0,4,67,1,0,0,0,6,71,1,0,0,0,8,76,
        1,0,0,0,10,79,1,0,0,0,12,96,1,0,0,0,14,103,1,0,0,0,16,108,1,0,0,
        0,18,112,1,0,0,0,20,115,1,0,0,0,22,118,1,0,0,0,24,131,1,0,0,0,26,
        144,1,0,0,0,28,146,1,0,0,0,30,155,1,0,0,0,32,171,1,0,0,0,34,186,
        1,0,0,0,36,198,1,0,0,0,38,200,1,0,0,0,40,230,1,0,0,0,42,232,1,0,
        0,0,44,244,1,0,0,0,46,246,1,0,0,0,48,254,1,0,0,0,50,51,3,2,1,0,51,
        52,5,0,0,1,52,1,1,0,0,0,53,62,3,4,2,0,54,61,3,6,3,0,55,61,3,22,11,
        0,56,61,3,24,12,0,57,61,3,28,14,0,58,61,3,30,15,0,59,61,3,32,16,
        0,60,54,1,0,0,0,60,55,1,0,0,0,60,56,1,0,0,0,60,57,1,0,0,0,60,58,
        1,0,0,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,
        63,65,1,0,0,0,64,62,1,0,0,0,65,66,3,44,22,0,66,3,1,0,0,0,67,68,5,
        2,0,0,68,69,5,3,0,0,69,70,3,46,23,0,70,5,1,0,0,0,71,74,3,8,4,0,72,
        75,3,10,5,0,73,75,3,20,10,0,74,72,1,0,0,0,74,73,1,0,0,0,75,7,1,0,
        0,0,76,77,7,0,0,0,77,9,1,0,0,0,78,80,5,20,0,0,79,78,1,0,0,0,79,80,
        1,0,0,0,80,81,1,0,0,0,81,88,3,14,7,0,82,84,3,12,6,0,83,82,1,0,0,
        0,83,84,1,0,0,0,84,85,1,0,0,0,85,87,3,14,7,0,86,83,1,0,0,0,87,90,
        1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,11,1,0,0,0,90,88,1,0,0,0,
        91,97,5,56,0,0,92,93,5,21,0,0,93,97,5,20,0,0,94,97,5,21,0,0,95,97,
        5,20,0,0,96,91,1,0,0,0,96,92,1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,0,
        97,13,1,0,0,0,98,99,3,48,24,0,99,100,5,55,0,0,100,102,1,0,0,0,101,
        98,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,106,
        1,0,0,0,105,103,1,0,0,0,106,107,3,16,8,0,107,15,1,0,0,0,108,110,
        3,46,23,0,109,111,3,18,9,0,110,109,1,0,0,0,110,111,1,0,0,0,111,17,
        1,0,0,0,112,113,5,19,0,0,113,114,5,58,0,0,114,19,1,0,0,0,115,116,
        5,1,0,0,116,21,1,0,0,0,117,119,5,13,0,0,118,117,1,0,0,0,118,119,
        1,0,0,0,119,120,1,0,0,0,120,122,5,11,0,0,121,123,3,26,13,0,122,121,
        1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,126,3,16,8,0,125,127,
        3,38,19,0,126,125,1,0,0,0,126,127,1,0,0,0,127,129,1,0,0,0,128,130,
        5,18,0,0,129,128,1,0,0,0,129,130,1,0,0,0,130,23,1,0,0,0,131,133,
        5,12,0,0,132,134,3,26,13,0,133,132,1,0,0,0,133,134,1,0,0,0,134,135,
        1,0,0,0,135,137,3,16,8,0,136,138,5,18,0,0,137,136,1,0,0,0,137,138,
        1,0,0,0,138,25,1,0,0,0,139,141,7,1,0,0,140,142,5,57,0,0,141,140,
        1,0,0,0,141,142,1,0,0,0,142,145,1,0,0,0,143,145,5,57,0,0,144,139,
        1,0,0,0,144,143,1,0,0,0,145,27,1,0,0,0,146,148,5,22,0,0,147,149,
        5,27,0,0,148,147,1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,152,
        5,58,0,0,151,150,1,0,0,0,152,153,1,0,0,0,153,151,1,0,0,0,153,154,
        1,0,0,0,154,29,1,0,0,0,155,157,5,23,0,0,156,158,5,27,0,0,157,156,
        1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,161,5,58,0,0,160,159,
        1,0,0,0,161,162,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,31,1,
        0,0,0,164,165,5,24,0,0,165,166,5,2,0,0,166,172,3,34,17,0,167,168,
        5,24,0,0,168,169,3,46,23,0,169,170,3,36,18,0,170,172,1,0,0,0,171,
        164,1,0,0,0,171,167,1,0,0,0,172,33,1,0,0,0,173,175,7,2,0,0,174,176,
        5,27,0,0,175,174,1,0,0,0,175,176,1,0,0,0,176,178,1,0,0,0,177,179,
        5,58,0,0,178,177,1,0,0,0,179,180,1,0,0,0,180,178,1,0,0,0,180,181,
        1,0,0,0,181,187,1,0,0,0,182,187,5,32,0,0,183,187,5,33,0,0,184,187,
        3,42,21,0,185,187,3,38,19,0,186,173,1,0,0,0,186,182,1,0,0,0,186,
        183,1,0,0,0,186,184,1,0,0,0,186,185,1,0,0,0,187,35,1,0,0,0,188,190,
        7,2,0,0,189,191,5,27,0,0,190,189,1,0,0,0,190,191,1,0,0,0,191,193,
        1,0,0,0,192,194,5,58,0,0,193,192,1,0,0,0,194,195,1,0,0,0,195,193,
        1,0,0,0,195,196,1,0,0,0,196,199,1,0,0,0,197,199,3,38,19,0,198,188,
        1,0,0,0,198,197,1,0,0,0,199,37,1,0,0,0,200,212,7,3,0,0,201,203,3,
        40,20,0,202,201,1,0,0,0,202,203,1,0,0,0,203,209,1,0,0,0,204,206,
        3,16,8,0,205,207,3,18,9,0,206,205,1,0,0,0,206,207,1,0,0,0,207,210,
        1,0,0,0,208,210,3,18,9,0,209,204,1,0,0,0,209,208,1,0,0,0,210,213,
        1,0,0,0,211,213,3,40,20,0,212,202,1,0,0,0,212,211,1,0,0,0,212,213,
        1,0,0,0,213,39,1,0,0,0,214,220,5,39,0,0,215,216,3,48,24,0,216,217,
        5,55,0,0,217,219,1,0,0,0,218,215,1,0,0,0,219,222,1,0,0,0,220,218,
        1,0,0,0,220,221,1,0,0,0,221,231,1,0,0,0,222,220,1,0,0,0,223,224,
        3,48,24,0,224,225,5,55,0,0,225,227,1,0,0,0,226,223,1,0,0,0,227,228,
        1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,231,1,0,0,0,230,214,
        1,0,0,0,230,226,1,0,0,0,231,41,1,0,0,0,232,235,7,4,0,0,233,234,5,
        19,0,0,234,236,3,46,23,0,235,233,1,0,0,0,235,236,1,0,0,0,236,242,
        1,0,0,0,237,240,5,38,0,0,238,241,5,59,0,0,239,241,3,8,4,0,240,238,
        1,0,0,0,240,239,1,0,0,0,241,243,1,0,0,0,242,237,1,0,0,0,242,243,
        1,0,0,0,243,43,1,0,0,0,244,245,5,4,0,0,245,45,1,0,0,0,246,251,5,
        59,0,0,247,248,5,55,0,0,248,250,5,59,0,0,249,247,1,0,0,0,250,253,
        1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,47,1,0,0,0,253,251,1,
        0,0,0,254,255,7,5,0,0,255,49,1,0,0,0,39,60,62,74,79,83,88,96,103,
        110,118,122,126,129,133,137,141,144,148,153,157,162,171,175,180,
        186,190,195,198,202,206,209,212,220,228,230,235,240,242,251
    ]

class WebFocusReportParser ( Parser ):

    grammarFileName = "WebFocusReport.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "TABLE", "FILE", "END",
                      "PRINT", "SUM", "LIST", "COUNT", "WRITE", "ADD", "BY",
                      "ACROSS", "RANKED", "HIGHEST", "LOWEST", "TOP", "BOTTOM",
                      "NOPRINT", "AS", "THE", "AND", "HEADING", "FOOTING",
                      "ON", "SUBHEAD", "SUBFOOT", "CENTER", "SUBTOTAL",
                      "SUB_TOTAL", "SUMMARIZE", "RECOMPUTE", "COLUMN_TOTAL",
                      "ROW_TOTAL", "HOLD", "PCHOLD", "SAVE", "SAVB", "FORMAT",
                      "ROLL_DOT", "AVE", "MIN", "MAX", "CNT", "FST", "LST",
                      "ASQ", "MDN", "MDE", "PCT", "RPCT", "RNK", "DST",
                      "TOT", "CT", "DOT", "COMMA", "NUMBER", "STRING", "NAME",
                      "WS" ]

    RULE_start = 0
    RULE_request = 1
    RULE_table_file = 2
    RULE_verb_command = 3
    RULE_verb = 4
    RULE_field_list = 5
    RULE_field_separator = 6
    RULE_field_or_prefixed = 7
    RULE_field = 8
    RULE_as_phrase = 9
    RULE_asterisk = 10
    RULE_by_command = 11
    RULE_across_command = 12
    RULE_sort_options = 13
    RULE_heading_command = 14
    RULE_footing_command = 15
    RULE_on_command = 16
    RULE_on_table_options = 17
    RULE_on_field_options = 18
    RULE_summarize_command = 19
    RULE_summarize_options = 20
    RULE_output_command = 21
    RULE_end_command = 22
    RULE_qualified_name = 23
    RULE_prefix_operator = 24

    ruleNames =  [ "start", "request", "table_file", "verb_command", "verb",
                   "field_list", "field_separator", "field_or_prefixed",
                   "field", "as_phrase", "asterisk", "by_command", "across_command",
                   "sort_options", "heading_command", "footing_command",
                   "on_command", "on_table_options", "on_field_options",
                   "summarize_command", "summarize_options", "output_command",
                   "end_command", "qualified_name", "prefix_operator" ]

    EOF = Token.EOF
    T__0=1
    TABLE=2
    FILE=3
    END=4
    PRINT=5
    SUM=6
    LIST=7
    COUNT=8
    WRITE=9
    ADD=10
    BY=11
    ACROSS=12
    RANKED=13
    HIGHEST=14
    LOWEST=15
    TOP=16
    BOTTOM=17
    NOPRINT=18
    AS=19
    THE=20
    AND=21
    HEADING=22
    FOOTING=23
    ON=24
    SUBHEAD=25
    SUBFOOT=26
    CENTER=27
    SUBTOTAL=28
    SUB_TOTAL=29
    SUMMARIZE=30
    RECOMPUTE=31
    COLUMN_TOTAL=32
    ROW_TOTAL=33
    HOLD=34
    PCHOLD=35
    SAVE=36
    SAVB=37
    FORMAT=38
    ROLL_DOT=39
    AVE=40
    MIN=41
    MAX=42
    CNT=43
    FST=44
    LST=45
    ASQ=46
    MDN=47
    MDE=48
    PCT=49
    RPCT=50
    RNK=51
    DST=52
    TOT=53
    CT=54
    DOT=55
    COMMA=56
    NUMBER=57
    STRING=58
    NAME=59
    WS=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def request(self):
            return self.getTypedRuleContext(WebFocusReportParser.RequestContext,0)


        def EOF(self):
            return self.getToken(WebFocusReportParser.EOF, 0)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = WebFocusReportParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.request()
            self.state = 51
            self.match(WebFocusReportParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_file(self):
            return self.getTypedRuleContext(WebFocusReportParser.Table_fileContext,0)


        def end_command(self):
            return self.getTypedRuleContext(WebFocusReportParser.End_commandContext,0)


        def verb_command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WebFocusReportParser.Verb_commandContext)
            else:
                return self.getTypedRuleContext(WebFocusReportParser.Verb_commandContext,i)


        def by_command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WebFocusReportParser.By_commandContext)
            else:
                return self.getTypedRuleContext(WebFocusReportParser.By_commandContext,i)


        def across_command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WebFocusReportParser.Across_commandContext)
            else:
                return self.getTypedRuleContext(WebFocusReportParser.Across_commandContext,i)


        def heading_command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WebFocusReportParser.Heading_commandContext)
            else:
                return self.getTypedRuleContext(WebFocusReportParser.Heading_commandContext,i)


        def footing_command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WebFocusReportParser.Footing_commandContext)
            else:
                return self.getTypedRuleContext(WebFocusReportParser.Footing_commandContext,i)


        def on_command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WebFocusReportParser.On_commandContext)
            else:
                return self.getTypedRuleContext(WebFocusReportParser.On_commandContext,i)


        def getRuleIndex(self):
            return WebFocusReportParser.RULE_request

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequest" ):
                listener.enterRequest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequest" ):
                listener.exitRequest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequest" ):
                return visitor.visitRequest(self)
            else:
                return visitor.visitChildren(self)




    def request(self):

        localctx = WebFocusReportParser.RequestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_request)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.table_file()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 29376480) != 0):
                self.state = 60
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 6, 7, 8, 9, 10]:
                    self.state = 54
                    self.verb_command()
                    pass
                elif token in [11, 13]:
                    self.state = 55
                    self.by_command()
                    pass
                elif token in [12]:
                    self.state = 56
                    self.across_command()
                    pass
                elif token in [22]:
                    self.state = 57
                    self.heading_command()
                    pass
                elif token in [23]:
                    self.state = 58
                    self.footing_command()
                    pass
                elif token in [24]:
                    self.state = 59
                    self.on_command()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.end_command()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TABLE(self):
            return self.getToken(WebFocusReportParser.TABLE, 0)

        def FILE(self):
            return self.getToken(WebFocusReportParser.FILE, 0)

        def qualified_name(self):
            return self.getTypedRuleContext(WebFocusReportParser.Qualified_nameContext,0)


        def getRuleIndex(self):
            return WebFocusReportParser.RULE_table_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_file" ):
                listener.enterTable_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_file" ):
                listener.exitTable_file(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_file" ):
                return visitor.visitTable_file(self)
            else:
                return visitor.visitChildren(self)




    def table_file(self):

        localctx = WebFocusReportParser.Table_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_table_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(WebFocusReportParser.TABLE)
            self.state = 68
            self.match(WebFocusReportParser.FILE)
            self.state = 69
            self.qualified_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Verb_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def verb(self):
            return self.getTypedRuleContext(WebFocusReportParser.VerbContext,0)


        def field_list(self):
            return self.getTypedRuleContext(WebFocusReportParser.Field_listContext,0)


        def asterisk(self):
            return self.getTypedRuleContext(WebFocusReportParser.AsteriskContext,0)


        def getRuleIndex(self):
            return WebFocusReportParser.RULE_verb_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerb_command" ):
                listener.enterVerb_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerb_command" ):
                listener.exitVerb_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerb_command" ):
                return visitor.visitVerb_command(self)
            else:
                return visitor.visitChildren(self)




    def verb_command(self):

        localctx = WebFocusReportParser.Verb_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_verb_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.verb()
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 20, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 59]:
                self.state = 72
                self.field_list()
                pass
            elif token in [1]:
                self.state = 73
                self.asterisk()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(WebFocusReportParser.PRINT, 0)

        def SUM(self):
            return self.getToken(WebFocusReportParser.SUM, 0)

        def LIST(self):
            return self.getToken(WebFocusReportParser.LIST, 0)

        def COUNT(self):
            return self.getToken(WebFocusReportParser.COUNT, 0)

        def WRITE(self):
            return self.getToken(WebFocusReportParser.WRITE, 0)

        def ADD(self):
            return self.getToken(WebFocusReportParser.ADD, 0)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_verb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerb" ):
                listener.enterVerb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerb" ):
                listener.exitVerb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerb" ):
                return visitor.visitVerb(self)
            else:
                return visitor.visitChildren(self)




    def verb(self):

        localctx = WebFocusReportParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_verb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_or_prefixed(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WebFocusReportParser.Field_or_prefixedContext)
            else:
                return self.getTypedRuleContext(WebFocusReportParser.Field_or_prefixedContext,i)


        def THE(self):
            return self.getToken(WebFocusReportParser.THE, 0)

        def field_separator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WebFocusReportParser.Field_separatorContext)
            else:
                return self.getTypedRuleContext(WebFocusReportParser.Field_separatorContext,i)


        def getRuleIndex(self):
            return WebFocusReportParser.RULE_field_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_list" ):
                listener.enterField_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_list" ):
                listener.exitField_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_list" ):
                return visitor.visitField_list(self)
            else:
                return visitor.visitChildren(self)




    def field_list(self):

        localctx = WebFocusReportParser.Field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_field_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 78
                self.match(WebFocusReportParser.THE)


            self.state = 81
            self.field_or_prefixed()
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594041073664) != 0):
                        self.state = 82
                        self.field_separator()


                    self.state = 85
                    self.field_or_prefixed()
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_separatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(WebFocusReportParser.COMMA, 0)

        def AND(self):
            return self.getToken(WebFocusReportParser.AND, 0)

        def THE(self):
            return self.getToken(WebFocusReportParser.THE, 0)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_field_separator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_separator" ):
                listener.enterField_separator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_separator" ):
                listener.exitField_separator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_separator" ):
                return visitor.visitField_separator(self)
            else:
                return visitor.visitChildren(self)




    def field_separator(self):

        localctx = WebFocusReportParser.Field_separatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_field_separator)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(WebFocusReportParser.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(WebFocusReportParser.AND)
                self.state = 93
                self.match(WebFocusReportParser.THE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(WebFocusReportParser.AND)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.match(WebFocusReportParser.THE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_or_prefixedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(WebFocusReportParser.FieldContext,0)


        def prefix_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WebFocusReportParser.Prefix_operatorContext)
            else:
                return self.getTypedRuleContext(WebFocusReportParser.Prefix_operatorContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(WebFocusReportParser.DOT)
            else:
                return self.getToken(WebFocusReportParser.DOT, i)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_field_or_prefixed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_or_prefixed" ):
                listener.enterField_or_prefixed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_or_prefixed" ):
                listener.exitField_or_prefixed(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_or_prefixed" ):
                return visitor.visitField_or_prefixed(self)
            else:
                return visitor.visitChildren(self)




    def field_or_prefixed(self):

        localctx = WebFocusReportParser.Field_or_prefixedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_field_or_prefixed)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 36027697507336256) != 0):
                self.state = 98
                self.prefix_operator()
                self.state = 99
                self.match(WebFocusReportParser.DOT)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.field()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualified_name(self):
            return self.getTypedRuleContext(WebFocusReportParser.Qualified_nameContext,0)


        def as_phrase(self):
            return self.getTypedRuleContext(WebFocusReportParser.As_phraseContext,0)


        def getRuleIndex(self):
            return WebFocusReportParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = WebFocusReportParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.qualified_name()
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 109
                self.as_phrase()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class As_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AS(self):
            return self.getToken(WebFocusReportParser.AS, 0)

        def STRING(self):
            return self.getToken(WebFocusReportParser.STRING, 0)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_as_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAs_phrase" ):
                listener.enterAs_phrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAs_phrase" ):
                listener.exitAs_phrase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAs_phrase" ):
                return visitor.visitAs_phrase(self)
            else:
                return visitor.visitChildren(self)




    def as_phrase(self):

        localctx = WebFocusReportParser.As_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_as_phrase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(WebFocusReportParser.AS)
            self.state = 113
            self.match(WebFocusReportParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsteriskContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WebFocusReportParser.RULE_asterisk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsterisk" ):
                listener.enterAsterisk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsterisk" ):
                listener.exitAsterisk(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsterisk" ):
                return visitor.visitAsterisk(self)
            else:
                return visitor.visitChildren(self)




    def asterisk(self):

        localctx = WebFocusReportParser.AsteriskContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_asterisk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(WebFocusReportParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class By_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(WebFocusReportParser.BY, 0)

        def field(self):
            return self.getTypedRuleContext(WebFocusReportParser.FieldContext,0)


        def RANKED(self):
            return self.getToken(WebFocusReportParser.RANKED, 0)

        def sort_options(self):
            return self.getTypedRuleContext(WebFocusReportParser.Sort_optionsContext,0)


        def summarize_command(self):
            return self.getTypedRuleContext(WebFocusReportParser.Summarize_commandContext,0)


        def NOPRINT(self):
            return self.getToken(WebFocusReportParser.NOPRINT, 0)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_by_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBy_command" ):
                listener.enterBy_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBy_command" ):
                listener.exitBy_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBy_command" ):
                return visitor.visitBy_command(self)
            else:
                return visitor.visitChildren(self)




    def by_command(self):

        localctx = WebFocusReportParser.By_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_by_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 117
                self.match(WebFocusReportParser.RANKED)


            self.state = 120
            self.match(WebFocusReportParser.BY)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188076101632) != 0):
                self.state = 121
                self.sort_options()


            self.state = 124
            self.field()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0):
                self.state = 125
                self.summarize_command()


            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 128
                self.match(WebFocusReportParser.NOPRINT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Across_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACROSS(self):
            return self.getToken(WebFocusReportParser.ACROSS, 0)

        def field(self):
            return self.getTypedRuleContext(WebFocusReportParser.FieldContext,0)


        def sort_options(self):
            return self.getTypedRuleContext(WebFocusReportParser.Sort_optionsContext,0)


        def NOPRINT(self):
            return self.getToken(WebFocusReportParser.NOPRINT, 0)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_across_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcross_command" ):
                listener.enterAcross_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcross_command" ):
                listener.exitAcross_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcross_command" ):
                return visitor.visitAcross_command(self)
            else:
                return visitor.visitChildren(self)




    def across_command(self):

        localctx = WebFocusReportParser.Across_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_across_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(WebFocusReportParser.ACROSS)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 144115188076101632) != 0):
                self.state = 132
                self.sort_options()


            self.state = 135
            self.field()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 136
                self.match(WebFocusReportParser.NOPRINT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sort_optionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HIGHEST(self):
            return self.getToken(WebFocusReportParser.HIGHEST, 0)

        def LOWEST(self):
            return self.getToken(WebFocusReportParser.LOWEST, 0)

        def TOP(self):
            return self.getToken(WebFocusReportParser.TOP, 0)

        def BOTTOM(self):
            return self.getToken(WebFocusReportParser.BOTTOM, 0)

        def NUMBER(self):
            return self.getToken(WebFocusReportParser.NUMBER, 0)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_sort_options

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSort_options" ):
                listener.enterSort_options(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSort_options" ):
                listener.exitSort_options(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSort_options" ):
                return visitor.visitSort_options(self)
            else:
                return visitor.visitChildren(self)




    def sort_options(self):

        localctx = WebFocusReportParser.Sort_optionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_sort_options)
        self._la = 0 # Token type
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==57:
                    self.state = 140
                    self.match(WebFocusReportParser.NUMBER)


                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(WebFocusReportParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Heading_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEADING(self):
            return self.getToken(WebFocusReportParser.HEADING, 0)

        def CENTER(self):
            return self.getToken(WebFocusReportParser.CENTER, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(WebFocusReportParser.STRING)
            else:
                return self.getToken(WebFocusReportParser.STRING, i)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_heading_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeading_command" ):
                listener.enterHeading_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeading_command" ):
                listener.exitHeading_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeading_command" ):
                return visitor.visitHeading_command(self)
            else:
                return visitor.visitChildren(self)




    def heading_command(self):

        localctx = WebFocusReportParser.Heading_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_heading_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(WebFocusReportParser.HEADING)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 147
                self.match(WebFocusReportParser.CENTER)


            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 150
                self.match(WebFocusReportParser.STRING)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==58):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Footing_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOOTING(self):
            return self.getToken(WebFocusReportParser.FOOTING, 0)

        def CENTER(self):
            return self.getToken(WebFocusReportParser.CENTER, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(WebFocusReportParser.STRING)
            else:
                return self.getToken(WebFocusReportParser.STRING, i)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_footing_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFooting_command" ):
                listener.enterFooting_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFooting_command" ):
                listener.exitFooting_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFooting_command" ):
                return visitor.visitFooting_command(self)
            else:
                return visitor.visitChildren(self)




    def footing_command(self):

        localctx = WebFocusReportParser.Footing_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_footing_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(WebFocusReportParser.FOOTING)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 156
                self.match(WebFocusReportParser.CENTER)


            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 159
                self.match(WebFocusReportParser.STRING)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==58):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class On_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(WebFocusReportParser.ON, 0)

        def TABLE(self):
            return self.getToken(WebFocusReportParser.TABLE, 0)

        def on_table_options(self):
            return self.getTypedRuleContext(WebFocusReportParser.On_table_optionsContext,0)


        def qualified_name(self):
            return self.getTypedRuleContext(WebFocusReportParser.Qualified_nameContext,0)


        def on_field_options(self):
            return self.getTypedRuleContext(WebFocusReportParser.On_field_optionsContext,0)


        def getRuleIndex(self):
            return WebFocusReportParser.RULE_on_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOn_command" ):
                listener.enterOn_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOn_command" ):
                listener.exitOn_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOn_command" ):
                return visitor.visitOn_command(self)
            else:
                return visitor.visitChildren(self)




    def on_command(self):

        localctx = WebFocusReportParser.On_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_on_command)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(WebFocusReportParser.ON)
                self.state = 165
                self.match(WebFocusReportParser.TABLE)
                self.state = 166
                self.on_table_options()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(WebFocusReportParser.ON)
                self.state = 168
                self.qualified_name()
                self.state = 169
                self.on_field_options()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class On_table_optionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBHEAD(self):
            return self.getToken(WebFocusReportParser.SUBHEAD, 0)

        def SUBFOOT(self):
            return self.getToken(WebFocusReportParser.SUBFOOT, 0)

        def CENTER(self):
            return self.getToken(WebFocusReportParser.CENTER, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(WebFocusReportParser.STRING)
            else:
                return self.getToken(WebFocusReportParser.STRING, i)

        def COLUMN_TOTAL(self):
            return self.getToken(WebFocusReportParser.COLUMN_TOTAL, 0)

        def ROW_TOTAL(self):
            return self.getToken(WebFocusReportParser.ROW_TOTAL, 0)

        def output_command(self):
            return self.getTypedRuleContext(WebFocusReportParser.Output_commandContext,0)


        def summarize_command(self):
            return self.getTypedRuleContext(WebFocusReportParser.Summarize_commandContext,0)


        def getRuleIndex(self):
            return WebFocusReportParser.RULE_on_table_options

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOn_table_options" ):
                listener.enterOn_table_options(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOn_table_options" ):
                listener.exitOn_table_options(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOn_table_options" ):
                return visitor.visitOn_table_options(self)
            else:
                return visitor.visitChildren(self)




    def on_table_options(self):

        localctx = WebFocusReportParser.On_table_optionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_on_table_options)
        self._la = 0 # Token type
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 174
                    self.match(WebFocusReportParser.CENTER)


                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 177
                    self.match(WebFocusReportParser.STRING)
                    self.state = 180
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==58):
                        break

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(WebFocusReportParser.COLUMN_TOTAL)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(WebFocusReportParser.ROW_TOTAL)
                pass
            elif token in [34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.output_command()
                pass
            elif token in [28, 29, 30, 31]:
                self.enterOuterAlt(localctx, 5)
                self.state = 185
                self.summarize_command()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class On_field_optionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBHEAD(self):
            return self.getToken(WebFocusReportParser.SUBHEAD, 0)

        def SUBFOOT(self):
            return self.getToken(WebFocusReportParser.SUBFOOT, 0)

        def CENTER(self):
            return self.getToken(WebFocusReportParser.CENTER, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(WebFocusReportParser.STRING)
            else:
                return self.getToken(WebFocusReportParser.STRING, i)

        def summarize_command(self):
            return self.getTypedRuleContext(WebFocusReportParser.Summarize_commandContext,0)


        def getRuleIndex(self):
            return WebFocusReportParser.RULE_on_field_options

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOn_field_options" ):
                listener.enterOn_field_options(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOn_field_options" ):
                listener.exitOn_field_options(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOn_field_options" ):
                return visitor.visitOn_field_options(self)
            else:
                return visitor.visitChildren(self)




    def on_field_options(self):

        localctx = WebFocusReportParser.On_field_optionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_on_field_options)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 189
                    self.match(WebFocusReportParser.CENTER)


                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 192
                    self.match(WebFocusReportParser.STRING)
                    self.state = 195
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==58):
                        break

                pass
            elif token in [28, 29, 30, 31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.summarize_command()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Summarize_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBTOTAL(self):
            return self.getToken(WebFocusReportParser.SUBTOTAL, 0)

        def SUB_TOTAL(self):
            return self.getToken(WebFocusReportParser.SUB_TOTAL, 0)

        def SUMMARIZE(self):
            return self.getToken(WebFocusReportParser.SUMMARIZE, 0)

        def RECOMPUTE(self):
            return self.getToken(WebFocusReportParser.RECOMPUTE, 0)

        def summarize_options(self):
            return self.getTypedRuleContext(WebFocusReportParser.Summarize_optionsContext,0)


        def field(self):
            return self.getTypedRuleContext(WebFocusReportParser.FieldContext,0)


        def as_phrase(self):
            return self.getTypedRuleContext(WebFocusReportParser.As_phraseContext,0)


        def getRuleIndex(self):
            return WebFocusReportParser.RULE_summarize_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummarize_command" ):
                listener.enterSummarize_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummarize_command" ):
                listener.exitSummarize_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSummarize_command" ):
                return visitor.visitSummarize_command(self)
            else:
                return visitor.visitChildren(self)




    def summarize_command(self):

        localctx = WebFocusReportParser.Summarize_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_summarize_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028247263150144) != 0):
                    self.state = 201
                    self.summarize_options()


                self.state = 209
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [59]:
                    self.state = 204
                    self.field()
                    self.state = 206
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==19:
                        self.state = 205
                        self.as_phrase()


                    pass
                elif token in [19]:
                    self.state = 208
                    self.as_phrase()
                    pass
                else:
                    raise NoViableAltException(self)


            elif la_ == 2:
                self.state = 211
                self.summarize_options()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Summarize_optionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROLL_DOT(self):
            return self.getToken(WebFocusReportParser.ROLL_DOT, 0)

        def prefix_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WebFocusReportParser.Prefix_operatorContext)
            else:
                return self.getTypedRuleContext(WebFocusReportParser.Prefix_operatorContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(WebFocusReportParser.DOT)
            else:
                return self.getToken(WebFocusReportParser.DOT, i)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_summarize_options

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummarize_options" ):
                listener.enterSummarize_options(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummarize_options" ):
                listener.exitSummarize_options(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSummarize_options" ):
                return visitor.visitSummarize_options(self)
            else:
                return visitor.visitChildren(self)




    def summarize_options(self):

        localctx = WebFocusReportParser.Summarize_optionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_summarize_options)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(WebFocusReportParser.ROLL_DOT)
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 215
                        self.prefix_operator()
                        self.state = 216
                        self.match(WebFocusReportParser.DOT)
                    self.state = 222
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                pass
            elif token in [6, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 223
                        self.prefix_operator()
                        self.state = 224
                        self.match(WebFocusReportParser.DOT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 228
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Output_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HOLD(self):
            return self.getToken(WebFocusReportParser.HOLD, 0)

        def PCHOLD(self):
            return self.getToken(WebFocusReportParser.PCHOLD, 0)

        def SAVE(self):
            return self.getToken(WebFocusReportParser.SAVE, 0)

        def SAVB(self):
            return self.getToken(WebFocusReportParser.SAVB, 0)

        def AS(self):
            return self.getToken(WebFocusReportParser.AS, 0)

        def qualified_name(self):
            return self.getTypedRuleContext(WebFocusReportParser.Qualified_nameContext,0)


        def FORMAT(self):
            return self.getToken(WebFocusReportParser.FORMAT, 0)

        def NAME(self):
            return self.getToken(WebFocusReportParser.NAME, 0)

        def verb(self):
            return self.getTypedRuleContext(WebFocusReportParser.VerbContext,0)


        def getRuleIndex(self):
            return WebFocusReportParser.RULE_output_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput_command" ):
                listener.enterOutput_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput_command" ):
                listener.exitOutput_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput_command" ):
                return visitor.visitOutput_command(self)
            else:
                return visitor.visitChildren(self)




    def output_command(self):

        localctx = WebFocusReportParser.Output_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_output_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 257698037760) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 233
                self.match(WebFocusReportParser.AS)
                self.state = 234
                self.qualified_name()


            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 237
                self.match(WebFocusReportParser.FORMAT)
                self.state = 240
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [59]:
                    self.state = 238
                    self.match(WebFocusReportParser.NAME)
                    pass
                elif token in [5, 6, 7, 8, 9, 10]:
                    self.state = 239
                    self.verb()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(WebFocusReportParser.END, 0)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_end_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd_command" ):
                listener.enterEnd_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd_command" ):
                listener.exitEnd_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_command" ):
                return visitor.visitEnd_command(self)
            else:
                return visitor.visitChildren(self)




    def end_command(self):

        localctx = WebFocusReportParser.End_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_end_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(WebFocusReportParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Qualified_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(WebFocusReportParser.NAME)
            else:
                return self.getToken(WebFocusReportParser.NAME, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(WebFocusReportParser.DOT)
            else:
                return self.getToken(WebFocusReportParser.DOT, i)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_qualified_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualified_name" ):
                listener.enterQualified_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualified_name" ):
                listener.exitQualified_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualified_name" ):
                return visitor.visitQualified_name(self)
            else:
                return visitor.visitChildren(self)




    def qualified_name(self):

        localctx = WebFocusReportParser.Qualified_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_qualified_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(WebFocusReportParser.NAME)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 247
                self.match(WebFocusReportParser.DOT)
                self.state = 248
                self.match(WebFocusReportParser.NAME)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AVE(self):
            return self.getToken(WebFocusReportParser.AVE, 0)

        def MIN(self):
            return self.getToken(WebFocusReportParser.MIN, 0)

        def MAX(self):
            return self.getToken(WebFocusReportParser.MAX, 0)

        def CNT(self):
            return self.getToken(WebFocusReportParser.CNT, 0)

        def FST(self):
            return self.getToken(WebFocusReportParser.FST, 0)

        def LST(self):
            return self.getToken(WebFocusReportParser.LST, 0)

        def ASQ(self):
            return self.getToken(WebFocusReportParser.ASQ, 0)

        def MDN(self):
            return self.getToken(WebFocusReportParser.MDN, 0)

        def MDE(self):
            return self.getToken(WebFocusReportParser.MDE, 0)

        def PCT(self):
            return self.getToken(WebFocusReportParser.PCT, 0)

        def RPCT(self):
            return self.getToken(WebFocusReportParser.RPCT, 0)

        def RNK(self):
            return self.getToken(WebFocusReportParser.RNK, 0)

        def DST(self):
            return self.getToken(WebFocusReportParser.DST, 0)

        def TOT(self):
            return self.getToken(WebFocusReportParser.TOT, 0)

        def SUM(self):
            return self.getToken(WebFocusReportParser.SUM, 0)

        def CT(self):
            return self.getToken(WebFocusReportParser.CT, 0)

        def getRuleIndex(self):
            return WebFocusReportParser.RULE_prefix_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix_operator" ):
                listener.enterPrefix_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix_operator" ):
                listener.exitPrefix_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix_operator" ):
                return visitor.visitPrefix_operator(self)
            else:
                return visitor.visitChildren(self)




    def prefix_operator(self):

        localctx = WebFocusReportParser.Prefix_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_prefix_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 36027697507336256) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
