# Generated from src/MasterFile.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MasterFileParser import MasterFileParser
else:
    from MasterFileParser import MasterFileParser

# This class defines a complete generic visitor for a parse tree produced by MasterFileParser.

class MasterFileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MasterFileParser#start.
    def visitStart(self, ctx:MasterFileParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#item.
    def visitItem(self, ctx:MasterFileParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#declaration.
    def visitDeclaration(self, ctx:MasterFileParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#file_decl.
    def visitFile_decl(self, ctx:MasterFileParser.File_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#segment_decl.
    def visitSegment_decl(self, ctx:MasterFileParser.Segment_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#field_decl.
    def visitField_decl(self, ctx:MasterFileParser.Field_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#dimension_decl.
    def visitDimension_decl(self, ctx:MasterFileParser.Dimension_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#hierarchy_decl.
    def visitHierarchy_decl(self, ctx:MasterFileParser.Hierarchy_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#variable_decl.
    def visitVariable_decl(self, ctx:MasterFileParser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#define_decl.
    def visitDefine_decl(self, ctx:MasterFileParser.Define_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#compute_decl.
    def visitCompute_decl(self, ctx:MasterFileParser.Compute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#other_decl.
    def visitOther_decl(self, ctx:MasterFileParser.Other_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#attr_val.
    def visitAttr_val(self, ctx:MasterFileParser.Attr_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#assignment.
    def visitAssignment(self, ctx:MasterFileParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#name_format.
    def visitName_format(self, ctx:MasterFileParser.Name_formatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#value.
    def visitValue(self, ctx:MasterFileParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#expression.
    def visitExpression(self, ctx:MasterFileParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MasterFileParser#expression_part.
    def visitExpression_part(self, ctx:MasterFileParser.Expression_partContext):
        return self.visitChildren(ctx)



del MasterFileParser