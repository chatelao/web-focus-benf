# Generated from src/MasterFile.g4 by ANTLR 4.13.2
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
        4,1,15,186,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,3,1,43,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,3,1,3,3,
        3,56,8,3,1,3,1,3,1,3,5,3,61,8,3,10,3,12,3,64,9,3,1,3,3,3,67,8,3,
        1,3,1,3,1,4,1,4,3,4,73,8,4,1,4,1,4,1,4,5,4,78,8,4,10,4,12,4,81,9,
        4,1,4,3,4,84,8,4,1,4,1,4,1,5,1,5,3,5,90,8,5,1,5,1,5,1,5,5,5,95,8,
        5,10,5,12,5,98,9,5,1,5,3,5,101,8,5,1,5,1,5,1,6,1,6,1,6,5,6,108,8,
        6,10,6,12,6,111,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,122,
        8,7,10,7,12,7,125,9,7,1,7,3,7,128,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,5,8,139,8,8,10,8,12,8,142,9,8,1,8,3,8,145,8,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,9,5,9,154,8,9,10,9,12,9,157,9,9,1,9,3,9,160,8,
        9,1,9,1,9,1,10,1,10,3,10,166,8,10,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,3,12,175,8,12,1,13,1,13,1,14,4,14,180,8,14,11,14,12,14,181,
        1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        0,3,1,0,8,9,1,0,12,14,3,0,1,6,8,10,12,14,197,0,35,1,0,0,0,2,42,1,
        0,0,0,4,51,1,0,0,0,6,53,1,0,0,0,8,70,1,0,0,0,10,87,1,0,0,0,12,104,
        1,0,0,0,14,114,1,0,0,0,16,131,1,0,0,0,18,148,1,0,0,0,20,165,1,0,
        0,0,22,167,1,0,0,0,24,171,1,0,0,0,26,176,1,0,0,0,28,179,1,0,0,0,
        30,183,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,
        0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,0,0,1,39,
        1,1,0,0,0,40,43,3,4,2,0,41,43,5,7,0,0,42,40,1,0,0,0,42,41,1,0,0,
        0,43,3,1,0,0,0,44,52,3,6,3,0,45,52,3,8,4,0,46,52,3,10,5,0,47,52,
        3,14,7,0,48,52,3,16,8,0,49,52,3,12,6,0,50,52,3,18,9,0,51,44,1,0,
        0,0,51,45,1,0,0,0,51,46,1,0,0,0,51,47,1,0,0,0,51,48,1,0,0,0,51,49,
        1,0,0,0,51,50,1,0,0,0,52,5,1,0,0,0,53,55,5,1,0,0,54,56,7,0,0,0,55,
        54,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,62,3,26,13,0,58,59,5,8,
        0,0,59,61,3,20,10,0,60,58,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,
        63,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,65,67,5,8,0,0,66,65,1,0,0,
        0,66,67,1,0,0,0,67,68,1,0,0,0,68,69,5,7,0,0,69,7,1,0,0,0,70,72,5,
        2,0,0,71,73,7,0,0,0,72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,
        79,3,26,13,0,75,76,5,8,0,0,76,78,3,20,10,0,77,75,1,0,0,0,78,81,1,
        0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,82,
        84,5,8,0,0,83,82,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,0,85,86,5,7,0,
        0,86,9,1,0,0,0,87,89,5,3,0,0,88,90,7,0,0,0,89,88,1,0,0,0,89,90,1,
        0,0,0,90,91,1,0,0,0,91,96,3,26,13,0,92,93,5,8,0,0,93,95,3,20,10,
        0,94,92,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,100,
        1,0,0,0,98,96,1,0,0,0,99,101,5,8,0,0,100,99,1,0,0,0,100,101,1,0,
        0,0,101,102,1,0,0,0,102,103,5,7,0,0,103,11,1,0,0,0,104,109,5,4,0,
        0,105,108,3,20,10,0,106,108,5,8,0,0,107,105,1,0,0,0,107,106,1,0,
        0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,112,1,0,
        0,0,111,109,1,0,0,0,112,113,5,7,0,0,113,13,1,0,0,0,114,115,5,5,0,
        0,115,116,3,24,12,0,116,117,5,9,0,0,117,118,3,28,14,0,118,123,5,
        11,0,0,119,120,5,8,0,0,120,122,3,20,10,0,121,119,1,0,0,0,122,125,
        1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,127,1,0,0,0,125,123,
        1,0,0,0,126,128,5,8,0,0,127,126,1,0,0,0,127,128,1,0,0,0,128,129,
        1,0,0,0,129,130,5,7,0,0,130,15,1,0,0,0,131,132,5,6,0,0,132,133,3,
        24,12,0,133,134,5,9,0,0,134,135,3,28,14,0,135,140,5,11,0,0,136,137,
        5,8,0,0,137,139,3,20,10,0,138,136,1,0,0,0,139,142,1,0,0,0,140,138,
        1,0,0,0,140,141,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,143,145,
        5,8,0,0,144,143,1,0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,147,
        5,7,0,0,147,17,1,0,0,0,148,149,5,12,0,0,149,150,5,9,0,0,150,155,
        3,26,13,0,151,152,5,8,0,0,152,154,3,20,10,0,153,151,1,0,0,0,154,
        157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,159,1,0,0,0,157,
        155,1,0,0,0,158,160,5,8,0,0,159,158,1,0,0,0,159,160,1,0,0,0,160,
        161,1,0,0,0,161,162,5,7,0,0,162,19,1,0,0,0,163,166,3,22,11,0,164,
        166,3,26,13,0,165,163,1,0,0,0,165,164,1,0,0,0,166,21,1,0,0,0,167,
        168,5,12,0,0,168,169,5,9,0,0,169,170,3,26,13,0,170,23,1,0,0,0,171,
        174,3,26,13,0,172,173,5,10,0,0,173,175,3,26,13,0,174,172,1,0,0,0,
        174,175,1,0,0,0,175,25,1,0,0,0,176,177,7,1,0,0,177,27,1,0,0,0,178,
        180,3,30,15,0,179,178,1,0,0,0,180,181,1,0,0,0,181,179,1,0,0,0,181,
        182,1,0,0,0,182,29,1,0,0,0,183,184,7,2,0,0,184,31,1,0,0,0,23,35,
        42,51,55,62,66,72,79,83,89,96,100,107,109,123,127,140,144,155,159,
        165,174,181
    ]

class MasterFileParser ( Parser ):

    grammarFileName = "MasterFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "','", "'='", "'/'", "';'" ]

    symbolicNames = [ "<INVALID>", "FILENAME_KW", "SEGNAME_KW", "FIELDNAME_KW",
                      "VARIABLE_KW", "DEFINE_KW", "COMPUTE_KW", "TERMINATOR",
                      "COMMA", "EQUALS", "SLASH", "SEMICOLON", "ATTR", "UNQUOTED_VALUE",
                      "STRING", "WS" ]

    RULE_start = 0
    RULE_item = 1
    RULE_declaration = 2
    RULE_file_decl = 3
    RULE_segment_decl = 4
    RULE_field_decl = 5
    RULE_variable_decl = 6
    RULE_define_decl = 7
    RULE_compute_decl = 8
    RULE_other_decl = 9
    RULE_attr_val = 10
    RULE_assignment = 11
    RULE_name_format = 12
    RULE_value = 13
    RULE_expression = 14
    RULE_expression_part = 15

    ruleNames =  [ "start", "item", "declaration", "file_decl", "segment_decl",
                   "field_decl", "variable_decl", "define_decl", "compute_decl",
                   "other_decl", "attr_val", "assignment", "name_format",
                   "value", "expression", "expression_part" ]

    EOF = Token.EOF
    FILENAME_KW=1
    SEGNAME_KW=2
    FIELDNAME_KW=3
    VARIABLE_KW=4
    DEFINE_KW=5
    COMPUTE_KW=6
    TERMINATOR=7
    COMMA=8
    EQUALS=9
    SLASH=10
    SEMICOLON=11
    ATTR=12
    UNQUOTED_VALUE=13
    STRING=14
    WS=15

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

        def EOF(self):
            return self.getToken(MasterFileParser.EOF, 0)

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasterFileParser.ItemContext)
            else:
                return self.getTypedRuleContext(MasterFileParser.ItemContext,i)


        def getRuleIndex(self):
            return MasterFileParser.RULE_start

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

        localctx = MasterFileParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4350) != 0):
                self.state = 32
                self.item()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(MasterFileParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MasterFileParser.DeclarationContext,0)


        def TERMINATOR(self):
            return self.getToken(MasterFileParser.TERMINATOR, 0)

        def getRuleIndex(self):
            return MasterFileParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = MasterFileParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_item)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.declaration()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(MasterFileParser.TERMINATOR)
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


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def file_decl(self):
            return self.getTypedRuleContext(MasterFileParser.File_declContext,0)


        def segment_decl(self):
            return self.getTypedRuleContext(MasterFileParser.Segment_declContext,0)


        def field_decl(self):
            return self.getTypedRuleContext(MasterFileParser.Field_declContext,0)


        def define_decl(self):
            return self.getTypedRuleContext(MasterFileParser.Define_declContext,0)


        def compute_decl(self):
            return self.getTypedRuleContext(MasterFileParser.Compute_declContext,0)


        def variable_decl(self):
            return self.getTypedRuleContext(MasterFileParser.Variable_declContext,0)


        def other_decl(self):
            return self.getTypedRuleContext(MasterFileParser.Other_declContext,0)


        def getRuleIndex(self):
            return MasterFileParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MasterFileParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.file_decl()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.segment_decl()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.field_decl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.define_decl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.compute_decl()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.variable_decl()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 7)
                self.state = 50
                self.other_decl()
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


    class File_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILENAME_KW(self):
            return self.getToken(MasterFileParser.FILENAME_KW, 0)

        def value(self):
            return self.getTypedRuleContext(MasterFileParser.ValueContext,0)


        def TERMINATOR(self):
            return self.getToken(MasterFileParser.TERMINATOR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MasterFileParser.COMMA)
            else:
                return self.getToken(MasterFileParser.COMMA, i)

        def attr_val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasterFileParser.Attr_valContext)
            else:
                return self.getTypedRuleContext(MasterFileParser.Attr_valContext,i)


        def EQUALS(self):
            return self.getToken(MasterFileParser.EQUALS, 0)

        def getRuleIndex(self):
            return MasterFileParser.RULE_file_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_decl" ):
                listener.enterFile_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_decl" ):
                listener.exitFile_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_decl" ):
                return visitor.visitFile_decl(self)
            else:
                return visitor.visitChildren(self)




    def file_decl(self):

        localctx = MasterFileParser.File_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_file_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(MasterFileParser.FILENAME_KW)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==9:
                self.state = 54
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 57
            self.value()
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 58
                    self.match(MasterFileParser.COMMA)
                    self.state = 59
                    self.attr_val()
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 65
                self.match(MasterFileParser.COMMA)


            self.state = 68
            self.match(MasterFileParser.TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Segment_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEGNAME_KW(self):
            return self.getToken(MasterFileParser.SEGNAME_KW, 0)

        def value(self):
            return self.getTypedRuleContext(MasterFileParser.ValueContext,0)


        def TERMINATOR(self):
            return self.getToken(MasterFileParser.TERMINATOR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MasterFileParser.COMMA)
            else:
                return self.getToken(MasterFileParser.COMMA, i)

        def attr_val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasterFileParser.Attr_valContext)
            else:
                return self.getTypedRuleContext(MasterFileParser.Attr_valContext,i)


        def EQUALS(self):
            return self.getToken(MasterFileParser.EQUALS, 0)

        def getRuleIndex(self):
            return MasterFileParser.RULE_segment_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSegment_decl" ):
                listener.enterSegment_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSegment_decl" ):
                listener.exitSegment_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSegment_decl" ):
                return visitor.visitSegment_decl(self)
            else:
                return visitor.visitChildren(self)




    def segment_decl(self):

        localctx = MasterFileParser.Segment_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_segment_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(MasterFileParser.SEGNAME_KW)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==9:
                self.state = 71
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 74
            self.value()
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 75
                    self.match(MasterFileParser.COMMA)
                    self.state = 76
                    self.attr_val()
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 82
                self.match(MasterFileParser.COMMA)


            self.state = 85
            self.match(MasterFileParser.TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIELDNAME_KW(self):
            return self.getToken(MasterFileParser.FIELDNAME_KW, 0)

        def value(self):
            return self.getTypedRuleContext(MasterFileParser.ValueContext,0)


        def TERMINATOR(self):
            return self.getToken(MasterFileParser.TERMINATOR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MasterFileParser.COMMA)
            else:
                return self.getToken(MasterFileParser.COMMA, i)

        def attr_val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasterFileParser.Attr_valContext)
            else:
                return self.getTypedRuleContext(MasterFileParser.Attr_valContext,i)


        def EQUALS(self):
            return self.getToken(MasterFileParser.EQUALS, 0)

        def getRuleIndex(self):
            return MasterFileParser.RULE_field_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_decl" ):
                listener.enterField_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_decl" ):
                listener.exitField_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_decl" ):
                return visitor.visitField_decl(self)
            else:
                return visitor.visitChildren(self)




    def field_decl(self):

        localctx = MasterFileParser.Field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_field_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(MasterFileParser.FIELDNAME_KW)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==9:
                self.state = 88
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 91
            self.value()
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 92
                    self.match(MasterFileParser.COMMA)
                    self.state = 93
                    self.attr_val()
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 99
                self.match(MasterFileParser.COMMA)


            self.state = 102
            self.match(MasterFileParser.TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_KW(self):
            return self.getToken(MasterFileParser.VARIABLE_KW, 0)

        def TERMINATOR(self):
            return self.getToken(MasterFileParser.TERMINATOR, 0)

        def attr_val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasterFileParser.Attr_valContext)
            else:
                return self.getTypedRuleContext(MasterFileParser.Attr_valContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MasterFileParser.COMMA)
            else:
                return self.getToken(MasterFileParser.COMMA, i)

        def getRuleIndex(self):
            return MasterFileParser.RULE_variable_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_decl" ):
                listener.enterVariable_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_decl" ):
                listener.exitVariable_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = MasterFileParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MasterFileParser.VARIABLE_KW)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28928) != 0):
                self.state = 107
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 13, 14]:
                    self.state = 105
                    self.attr_val()
                    pass
                elif token in [8]:
                    self.state = 106
                    self.match(MasterFileParser.COMMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self.match(MasterFileParser.TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE_KW(self):
            return self.getToken(MasterFileParser.DEFINE_KW, 0)

        def name_format(self):
            return self.getTypedRuleContext(MasterFileParser.Name_formatContext,0)


        def EQUALS(self):
            return self.getToken(MasterFileParser.EQUALS, 0)

        def expression(self):
            return self.getTypedRuleContext(MasterFileParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MasterFileParser.SEMICOLON, 0)

        def TERMINATOR(self):
            return self.getToken(MasterFileParser.TERMINATOR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MasterFileParser.COMMA)
            else:
                return self.getToken(MasterFileParser.COMMA, i)

        def attr_val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasterFileParser.Attr_valContext)
            else:
                return self.getTypedRuleContext(MasterFileParser.Attr_valContext,i)


        def getRuleIndex(self):
            return MasterFileParser.RULE_define_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_decl" ):
                listener.enterDefine_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_decl" ):
                listener.exitDefine_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_decl" ):
                return visitor.visitDefine_decl(self)
            else:
                return visitor.visitChildren(self)




    def define_decl(self):

        localctx = MasterFileParser.Define_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_define_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MasterFileParser.DEFINE_KW)
            self.state = 115
            self.name_format()
            self.state = 116
            self.match(MasterFileParser.EQUALS)
            self.state = 117
            self.expression()
            self.state = 118
            self.match(MasterFileParser.SEMICOLON)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 119
                    self.match(MasterFileParser.COMMA)
                    self.state = 120
                    self.attr_val()
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 126
                self.match(MasterFileParser.COMMA)


            self.state = 129
            self.match(MasterFileParser.TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPUTE_KW(self):
            return self.getToken(MasterFileParser.COMPUTE_KW, 0)

        def name_format(self):
            return self.getTypedRuleContext(MasterFileParser.Name_formatContext,0)


        def EQUALS(self):
            return self.getToken(MasterFileParser.EQUALS, 0)

        def expression(self):
            return self.getTypedRuleContext(MasterFileParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MasterFileParser.SEMICOLON, 0)

        def TERMINATOR(self):
            return self.getToken(MasterFileParser.TERMINATOR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MasterFileParser.COMMA)
            else:
                return self.getToken(MasterFileParser.COMMA, i)

        def attr_val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasterFileParser.Attr_valContext)
            else:
                return self.getTypedRuleContext(MasterFileParser.Attr_valContext,i)


        def getRuleIndex(self):
            return MasterFileParser.RULE_compute_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompute_decl" ):
                listener.enterCompute_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompute_decl" ):
                listener.exitCompute_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompute_decl" ):
                return visitor.visitCompute_decl(self)
            else:
                return visitor.visitChildren(self)




    def compute_decl(self):

        localctx = MasterFileParser.Compute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_compute_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(MasterFileParser.COMPUTE_KW)
            self.state = 132
            self.name_format()
            self.state = 133
            self.match(MasterFileParser.EQUALS)
            self.state = 134
            self.expression()
            self.state = 135
            self.match(MasterFileParser.SEMICOLON)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 136
                    self.match(MasterFileParser.COMMA)
                    self.state = 137
                    self.attr_val()
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 143
                self.match(MasterFileParser.COMMA)


            self.state = 146
            self.match(MasterFileParser.TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Other_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTR(self):
            return self.getToken(MasterFileParser.ATTR, 0)

        def EQUALS(self):
            return self.getToken(MasterFileParser.EQUALS, 0)

        def value(self):
            return self.getTypedRuleContext(MasterFileParser.ValueContext,0)


        def TERMINATOR(self):
            return self.getToken(MasterFileParser.TERMINATOR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MasterFileParser.COMMA)
            else:
                return self.getToken(MasterFileParser.COMMA, i)

        def attr_val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasterFileParser.Attr_valContext)
            else:
                return self.getTypedRuleContext(MasterFileParser.Attr_valContext,i)


        def getRuleIndex(self):
            return MasterFileParser.RULE_other_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOther_decl" ):
                listener.enterOther_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOther_decl" ):
                listener.exitOther_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther_decl" ):
                return visitor.visitOther_decl(self)
            else:
                return visitor.visitChildren(self)




    def other_decl(self):

        localctx = MasterFileParser.Other_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_other_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(MasterFileParser.ATTR)
            self.state = 149
            self.match(MasterFileParser.EQUALS)
            self.state = 150
            self.value()
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 151
                    self.match(MasterFileParser.COMMA)
                    self.state = 152
                    self.attr_val()
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 158
                self.match(MasterFileParser.COMMA)


            self.state = 161
            self.match(MasterFileParser.TERMINATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MasterFileParser.AssignmentContext,0)


        def value(self):
            return self.getTypedRuleContext(MasterFileParser.ValueContext,0)


        def getRuleIndex(self):
            return MasterFileParser.RULE_attr_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr_val" ):
                listener.enterAttr_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr_val" ):
                listener.exitAttr_val(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_val" ):
                return visitor.visitAttr_val(self)
            else:
                return visitor.visitChildren(self)




    def attr_val(self):

        localctx = MasterFileParser.Attr_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attr_val)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTR(self):
            return self.getToken(MasterFileParser.ATTR, 0)

        def EQUALS(self):
            return self.getToken(MasterFileParser.EQUALS, 0)

        def value(self):
            return self.getTypedRuleContext(MasterFileParser.ValueContext,0)


        def getRuleIndex(self):
            return MasterFileParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MasterFileParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(MasterFileParser.ATTR)
            self.state = 168
            self.match(MasterFileParser.EQUALS)
            self.state = 169
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_formatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasterFileParser.ValueContext)
            else:
                return self.getTypedRuleContext(MasterFileParser.ValueContext,i)


        def SLASH(self):
            return self.getToken(MasterFileParser.SLASH, 0)

        def getRuleIndex(self):
            return MasterFileParser.RULE_name_format

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_format" ):
                listener.enterName_format(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_format" ):
                listener.exitName_format(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_format" ):
                return visitor.visitName_format(self)
            else:
                return visitor.visitChildren(self)




    def name_format(self):

        localctx = MasterFileParser.Name_formatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_name_format)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.value()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 172
                self.match(MasterFileParser.SLASH)
                self.state = 173
                self.value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MasterFileParser.STRING, 0)

        def ATTR(self):
            return self.getToken(MasterFileParser.ATTR, 0)

        def UNQUOTED_VALUE(self):
            return self.getToken(MasterFileParser.UNQUOTED_VALUE, 0)

        def getRuleIndex(self):
            return MasterFileParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MasterFileParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MasterFileParser.Expression_partContext)
            else:
                return self.getTypedRuleContext(MasterFileParser.Expression_partContext,i)


        def getRuleIndex(self):
            return MasterFileParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MasterFileParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 178
                self.expression_part()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 30590) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTR(self):
            return self.getToken(MasterFileParser.ATTR, 0)

        def UNQUOTED_VALUE(self):
            return self.getToken(MasterFileParser.UNQUOTED_VALUE, 0)

        def STRING(self):
            return self.getToken(MasterFileParser.STRING, 0)

        def COMMA(self):
            return self.getToken(MasterFileParser.COMMA, 0)

        def EQUALS(self):
            return self.getToken(MasterFileParser.EQUALS, 0)

        def SLASH(self):
            return self.getToken(MasterFileParser.SLASH, 0)

        def FILENAME_KW(self):
            return self.getToken(MasterFileParser.FILENAME_KW, 0)

        def SEGNAME_KW(self):
            return self.getToken(MasterFileParser.SEGNAME_KW, 0)

        def FIELDNAME_KW(self):
            return self.getToken(MasterFileParser.FIELDNAME_KW, 0)

        def VARIABLE_KW(self):
            return self.getToken(MasterFileParser.VARIABLE_KW, 0)

        def DEFINE_KW(self):
            return self.getToken(MasterFileParser.DEFINE_KW, 0)

        def COMPUTE_KW(self):
            return self.getToken(MasterFileParser.COMPUTE_KW, 0)

        def getRuleIndex(self):
            return MasterFileParser.RULE_expression_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_part" ):
                listener.enterExpression_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_part" ):
                listener.exitExpression_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_part" ):
                return visitor.visitExpression_part(self)
            else:
                return visitor.visitChildren(self)




    def expression_part(self):

        localctx = MasterFileParser.Expression_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30590) != 0)):
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
