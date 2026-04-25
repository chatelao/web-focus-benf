# Generated from src/WebFocusReport.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WebFocusReportParser import WebFocusReportParser
else:
    from WebFocusReportParser import WebFocusReportParser

# This class defines a complete generic visitor for a parse tree produced by WebFocusReportParser.

class WebFocusReportVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WebFocusReportParser#start.
    def visitStart(self, ctx:WebFocusReportParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#request.
    def visitRequest(self, ctx:WebFocusReportParser.RequestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#table_file.
    def visitTable_file(self, ctx:WebFocusReportParser.Table_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#verb_command.
    def visitVerb_command(self, ctx:WebFocusReportParser.Verb_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#verb.
    def visitVerb(self, ctx:WebFocusReportParser.VerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#field_list.
    def visitField_list(self, ctx:WebFocusReportParser.Field_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#field_separator.
    def visitField_separator(self, ctx:WebFocusReportParser.Field_separatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#field_or_prefixed.
    def visitField_or_prefixed(self, ctx:WebFocusReportParser.Field_or_prefixedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#field.
    def visitField(self, ctx:WebFocusReportParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#as_phrase.
    def visitAs_phrase(self, ctx:WebFocusReportParser.As_phraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#asterisk.
    def visitAsterisk(self, ctx:WebFocusReportParser.AsteriskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#by_command.
    def visitBy_command(self, ctx:WebFocusReportParser.By_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#across_command.
    def visitAcross_command(self, ctx:WebFocusReportParser.Across_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#sort_options.
    def visitSort_options(self, ctx:WebFocusReportParser.Sort_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#heading_command.
    def visitHeading_command(self, ctx:WebFocusReportParser.Heading_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#footing_command.
    def visitFooting_command(self, ctx:WebFocusReportParser.Footing_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#on_command.
    def visitOn_command(self, ctx:WebFocusReportParser.On_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#on_table_options.
    def visitOn_table_options(self, ctx:WebFocusReportParser.On_table_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#on_field_options.
    def visitOn_field_options(self, ctx:WebFocusReportParser.On_field_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#summarize_command.
    def visitSummarize_command(self, ctx:WebFocusReportParser.Summarize_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#summarize_options.
    def visitSummarize_options(self, ctx:WebFocusReportParser.Summarize_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#output_command.
    def visitOutput_command(self, ctx:WebFocusReportParser.Output_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#end_command.
    def visitEnd_command(self, ctx:WebFocusReportParser.End_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#qualified_name.
    def visitQualified_name(self, ctx:WebFocusReportParser.Qualified_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#prefix_operator.
    def visitPrefix_operator(self, ctx:WebFocusReportParser.Prefix_operatorContext):
        return self.visitChildren(ctx)



del WebFocusReportParser