# Generated from src/MasterFile.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MasterFileParser import MasterFileParser
else:
    from MasterFileParser import MasterFileParser

# This class defines a complete listener for a parse tree produced by MasterFileParser.
class MasterFileListener(ParseTreeListener):

    # Enter a parse tree produced by MasterFileParser#start.
    def enterStart(self, ctx:MasterFileParser.StartContext):
        pass

    # Exit a parse tree produced by MasterFileParser#start.
    def exitStart(self, ctx:MasterFileParser.StartContext):
        pass


    # Enter a parse tree produced by MasterFileParser#item.
    def enterItem(self, ctx:MasterFileParser.ItemContext):
        pass

    # Exit a parse tree produced by MasterFileParser#item.
    def exitItem(self, ctx:MasterFileParser.ItemContext):
        pass


    # Enter a parse tree produced by MasterFileParser#declaration.
    def enterDeclaration(self, ctx:MasterFileParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MasterFileParser#declaration.
    def exitDeclaration(self, ctx:MasterFileParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MasterFileParser#file_decl.
    def enterFile_decl(self, ctx:MasterFileParser.File_declContext):
        pass

    # Exit a parse tree produced by MasterFileParser#file_decl.
    def exitFile_decl(self, ctx:MasterFileParser.File_declContext):
        pass


    # Enter a parse tree produced by MasterFileParser#segment_decl.
    def enterSegment_decl(self, ctx:MasterFileParser.Segment_declContext):
        pass

    # Exit a parse tree produced by MasterFileParser#segment_decl.
    def exitSegment_decl(self, ctx:MasterFileParser.Segment_declContext):
        pass


    # Enter a parse tree produced by MasterFileParser#field_decl.
    def enterField_decl(self, ctx:MasterFileParser.Field_declContext):
        pass

    # Exit a parse tree produced by MasterFileParser#field_decl.
    def exitField_decl(self, ctx:MasterFileParser.Field_declContext):
        pass


    # Enter a parse tree produced by MasterFileParser#variable_decl.
    def enterVariable_decl(self, ctx:MasterFileParser.Variable_declContext):
        pass

    # Exit a parse tree produced by MasterFileParser#variable_decl.
    def exitVariable_decl(self, ctx:MasterFileParser.Variable_declContext):
        pass


    # Enter a parse tree produced by MasterFileParser#define_decl.
    def enterDefine_decl(self, ctx:MasterFileParser.Define_declContext):
        pass

    # Exit a parse tree produced by MasterFileParser#define_decl.
    def exitDefine_decl(self, ctx:MasterFileParser.Define_declContext):
        pass


    # Enter a parse tree produced by MasterFileParser#compute_decl.
    def enterCompute_decl(self, ctx:MasterFileParser.Compute_declContext):
        pass

    # Exit a parse tree produced by MasterFileParser#compute_decl.
    def exitCompute_decl(self, ctx:MasterFileParser.Compute_declContext):
        pass


    # Enter a parse tree produced by MasterFileParser#other_decl.
    def enterOther_decl(self, ctx:MasterFileParser.Other_declContext):
        pass

    # Exit a parse tree produced by MasterFileParser#other_decl.
    def exitOther_decl(self, ctx:MasterFileParser.Other_declContext):
        pass


    # Enter a parse tree produced by MasterFileParser#attr_val.
    def enterAttr_val(self, ctx:MasterFileParser.Attr_valContext):
        pass

    # Exit a parse tree produced by MasterFileParser#attr_val.
    def exitAttr_val(self, ctx:MasterFileParser.Attr_valContext):
        pass


    # Enter a parse tree produced by MasterFileParser#assignment.
    def enterAssignment(self, ctx:MasterFileParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MasterFileParser#assignment.
    def exitAssignment(self, ctx:MasterFileParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MasterFileParser#name_format.
    def enterName_format(self, ctx:MasterFileParser.Name_formatContext):
        pass

    # Exit a parse tree produced by MasterFileParser#name_format.
    def exitName_format(self, ctx:MasterFileParser.Name_formatContext):
        pass


    # Enter a parse tree produced by MasterFileParser#value.
    def enterValue(self, ctx:MasterFileParser.ValueContext):
        pass

    # Exit a parse tree produced by MasterFileParser#value.
    def exitValue(self, ctx:MasterFileParser.ValueContext):
        pass


    # Enter a parse tree produced by MasterFileParser#expression.
    def enterExpression(self, ctx:MasterFileParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MasterFileParser#expression.
    def exitExpression(self, ctx:MasterFileParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MasterFileParser#expression_part.
    def enterExpression_part(self, ctx:MasterFileParser.Expression_partContext):
        pass

    # Exit a parse tree produced by MasterFileParser#expression_part.
    def exitExpression_part(self, ctx:MasterFileParser.Expression_partContext):
        pass



del MasterFileParser