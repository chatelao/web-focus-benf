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


    # Visit a parse tree produced by WebFocusReportParser#define_file.
    def visitDefine_file(self, ctx:WebFocusReportParser.Define_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#define_assignment.
    def visitDefine_assignment(self, ctx:WebFocusReportParser.Define_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#compute_command.
    def visitCompute_command(self, ctx:WebFocusReportParser.Compute_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#format_name.
    def visitFormat_name(self, ctx:WebFocusReportParser.Format_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#join_command.
    def visitJoin_command(self, ctx:WebFocusReportParser.Join_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#set_command.
    def visitSet_command(self, ctx:WebFocusReportParser.Set_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_command.
    def visitDm_command(self, ctx:WebFocusReportParser.Dm_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_set.
    def visitDm_set(self, ctx:WebFocusReportParser.Dm_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_goto.
    def visitDm_goto(self, ctx:WebFocusReportParser.Dm_gotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_repeat.
    def visitDm_repeat(self, ctx:WebFocusReportParser.Dm_repeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_label.
    def visitDm_label(self, ctx:WebFocusReportParser.Dm_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_if.
    def visitDm_if(self, ctx:WebFocusReportParser.Dm_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_type.
    def visitDm_type(self, ctx:WebFocusReportParser.Dm_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_include.
    def visitDm_include(self, ctx:WebFocusReportParser.Dm_includeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_run.
    def visitDm_run(self, ctx:WebFocusReportParser.Dm_runContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_exit.
    def visitDm_exit(self, ctx:WebFocusReportParser.Dm_exitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_expression.
    def visitDm_expression(self, ctx:WebFocusReportParser.Dm_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_if_expression.
    def visitDm_if_expression(self, ctx:WebFocusReportParser.Dm_if_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_logical_expression.
    def visitDm_logical_expression(self, ctx:WebFocusReportParser.Dm_logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_relational_expression.
    def visitDm_relational_expression(self, ctx:WebFocusReportParser.Dm_relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_relational_op.
    def visitDm_relational_op(self, ctx:WebFocusReportParser.Dm_relational_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#is_not_op.
    def visitIs_not_op(self, ctx:WebFocusReportParser.Is_not_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#is_from_op.
    def visitIs_from_op(self, ctx:WebFocusReportParser.Is_from_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#not_from_op.
    def visitNot_from_op(self, ctx:WebFocusReportParser.Not_from_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#is_less_op.
    def visitIs_less_op(self, ctx:WebFocusReportParser.Is_less_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#is_more_op.
    def visitIs_more_op(self, ctx:WebFocusReportParser.Is_more_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#is_greater_op.
    def visitIs_greater_op(self, ctx:WebFocusReportParser.Is_greater_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_concat_expression.
    def visitDm_concat_expression(self, ctx:WebFocusReportParser.Dm_concat_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_additive_expression.
    def visitDm_additive_expression(self, ctx:WebFocusReportParser.Dm_additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_multiplicative_expression.
    def visitDm_multiplicative_expression(self, ctx:WebFocusReportParser.Dm_multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_primary.
    def visitDm_primary(self, ctx:WebFocusReportParser.Dm_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#dm_float.
    def visitDm_float(self, ctx:WebFocusReportParser.Dm_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#amper_var.
    def visitAmper_var(self, ctx:WebFocusReportParser.Amper_varContext):
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


    # Visit a parse tree produced by WebFocusReportParser#where_command.
    def visitWhere_command(self, ctx:WebFocusReportParser.Where_commandContext):
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


    # Visit a parse tree produced by WebFocusReportParser#identifier.
    def visitIdentifier(self, ctx:WebFocusReportParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WebFocusReportParser#prefix_operator.
    def visitPrefix_operator(self, ctx:WebFocusReportParser.Prefix_operatorContext):
        return self.visitChildren(ctx)



del WebFocusReportParser