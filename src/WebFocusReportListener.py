# Generated from src/WebFocusReport.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WebFocusReportParser import WebFocusReportParser
else:
    from WebFocusReportParser import WebFocusReportParser

# This class defines a complete listener for a parse tree produced by WebFocusReportParser.
class WebFocusReportListener(ParseTreeListener):

    # Enter a parse tree produced by WebFocusReportParser#start.
    def enterStart(self, ctx:WebFocusReportParser.StartContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#start.
    def exitStart(self, ctx:WebFocusReportParser.StartContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#request.
    def enterRequest(self, ctx:WebFocusReportParser.RequestContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#request.
    def exitRequest(self, ctx:WebFocusReportParser.RequestContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#define_file.
    def enterDefine_file(self, ctx:WebFocusReportParser.Define_fileContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#define_file.
    def exitDefine_file(self, ctx:WebFocusReportParser.Define_fileContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#define_assignment.
    def enterDefine_assignment(self, ctx:WebFocusReportParser.Define_assignmentContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#define_assignment.
    def exitDefine_assignment(self, ctx:WebFocusReportParser.Define_assignmentContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#compute_command.
    def enterCompute_command(self, ctx:WebFocusReportParser.Compute_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#compute_command.
    def exitCompute_command(self, ctx:WebFocusReportParser.Compute_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#format_name.
    def enterFormat_name(self, ctx:WebFocusReportParser.Format_nameContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#format_name.
    def exitFormat_name(self, ctx:WebFocusReportParser.Format_nameContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#join_command.
    def enterJoin_command(self, ctx:WebFocusReportParser.Join_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#join_command.
    def exitJoin_command(self, ctx:WebFocusReportParser.Join_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#set_command.
    def enterSet_command(self, ctx:WebFocusReportParser.Set_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#set_command.
    def exitSet_command(self, ctx:WebFocusReportParser.Set_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_command.
    def enterDm_command(self, ctx:WebFocusReportParser.Dm_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_command.
    def exitDm_command(self, ctx:WebFocusReportParser.Dm_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_set.
    def enterDm_set(self, ctx:WebFocusReportParser.Dm_setContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_set.
    def exitDm_set(self, ctx:WebFocusReportParser.Dm_setContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_goto.
    def enterDm_goto(self, ctx:WebFocusReportParser.Dm_gotoContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_goto.
    def exitDm_goto(self, ctx:WebFocusReportParser.Dm_gotoContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_repeat.
    def enterDm_repeat(self, ctx:WebFocusReportParser.Dm_repeatContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_repeat.
    def exitDm_repeat(self, ctx:WebFocusReportParser.Dm_repeatContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_label.
    def enterDm_label(self, ctx:WebFocusReportParser.Dm_labelContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_label.
    def exitDm_label(self, ctx:WebFocusReportParser.Dm_labelContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_if.
    def enterDm_if(self, ctx:WebFocusReportParser.Dm_ifContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_if.
    def exitDm_if(self, ctx:WebFocusReportParser.Dm_ifContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_type.
    def enterDm_type(self, ctx:WebFocusReportParser.Dm_typeContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_type.
    def exitDm_type(self, ctx:WebFocusReportParser.Dm_typeContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_include.
    def enterDm_include(self, ctx:WebFocusReportParser.Dm_includeContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_include.
    def exitDm_include(self, ctx:WebFocusReportParser.Dm_includeContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_run.
    def enterDm_run(self, ctx:WebFocusReportParser.Dm_runContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_run.
    def exitDm_run(self, ctx:WebFocusReportParser.Dm_runContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_exit.
    def enterDm_exit(self, ctx:WebFocusReportParser.Dm_exitContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_exit.
    def exitDm_exit(self, ctx:WebFocusReportParser.Dm_exitContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_expression.
    def enterDm_expression(self, ctx:WebFocusReportParser.Dm_expressionContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_expression.
    def exitDm_expression(self, ctx:WebFocusReportParser.Dm_expressionContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_if_expression.
    def enterDm_if_expression(self, ctx:WebFocusReportParser.Dm_if_expressionContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_if_expression.
    def exitDm_if_expression(self, ctx:WebFocusReportParser.Dm_if_expressionContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_concat_expression.
    def enterDm_concat_expression(self, ctx:WebFocusReportParser.Dm_concat_expressionContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_concat_expression.
    def exitDm_concat_expression(self, ctx:WebFocusReportParser.Dm_concat_expressionContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_additive_expression.
    def enterDm_additive_expression(self, ctx:WebFocusReportParser.Dm_additive_expressionContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_additive_expression.
    def exitDm_additive_expression(self, ctx:WebFocusReportParser.Dm_additive_expressionContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_multiplicative_expression.
    def enterDm_multiplicative_expression(self, ctx:WebFocusReportParser.Dm_multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_multiplicative_expression.
    def exitDm_multiplicative_expression(self, ctx:WebFocusReportParser.Dm_multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_primary.
    def enterDm_primary(self, ctx:WebFocusReportParser.Dm_primaryContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_primary.
    def exitDm_primary(self, ctx:WebFocusReportParser.Dm_primaryContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_float.
    def enterDm_float(self, ctx:WebFocusReportParser.Dm_floatContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_float.
    def exitDm_float(self, ctx:WebFocusReportParser.Dm_floatContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#amper_var.
    def enterAmper_var(self, ctx:WebFocusReportParser.Amper_varContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#amper_var.
    def exitAmper_var(self, ctx:WebFocusReportParser.Amper_varContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_logical_expression.
    def enterDm_logical_expression(self, ctx:WebFocusReportParser.Dm_logical_expressionContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_logical_expression.
    def exitDm_logical_expression(self, ctx:WebFocusReportParser.Dm_logical_expressionContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#dm_relational_op.
    def enterDm_relational_op(self, ctx:WebFocusReportParser.Dm_relational_opContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#dm_relational_op.
    def exitDm_relational_op(self, ctx:WebFocusReportParser.Dm_relational_opContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#table_file.
    def enterTable_file(self, ctx:WebFocusReportParser.Table_fileContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#table_file.
    def exitTable_file(self, ctx:WebFocusReportParser.Table_fileContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#verb_command.
    def enterVerb_command(self, ctx:WebFocusReportParser.Verb_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#verb_command.
    def exitVerb_command(self, ctx:WebFocusReportParser.Verb_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#verb.
    def enterVerb(self, ctx:WebFocusReportParser.VerbContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#verb.
    def exitVerb(self, ctx:WebFocusReportParser.VerbContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#field_list.
    def enterField_list(self, ctx:WebFocusReportParser.Field_listContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#field_list.
    def exitField_list(self, ctx:WebFocusReportParser.Field_listContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#field_separator.
    def enterField_separator(self, ctx:WebFocusReportParser.Field_separatorContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#field_separator.
    def exitField_separator(self, ctx:WebFocusReportParser.Field_separatorContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#field_or_prefixed.
    def enterField_or_prefixed(self, ctx:WebFocusReportParser.Field_or_prefixedContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#field_or_prefixed.
    def exitField_or_prefixed(self, ctx:WebFocusReportParser.Field_or_prefixedContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#field.
    def enterField(self, ctx:WebFocusReportParser.FieldContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#field.
    def exitField(self, ctx:WebFocusReportParser.FieldContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#as_phrase.
    def enterAs_phrase(self, ctx:WebFocusReportParser.As_phraseContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#as_phrase.
    def exitAs_phrase(self, ctx:WebFocusReportParser.As_phraseContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#asterisk.
    def enterAsterisk(self, ctx:WebFocusReportParser.AsteriskContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#asterisk.
    def exitAsterisk(self, ctx:WebFocusReportParser.AsteriskContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#by_command.
    def enterBy_command(self, ctx:WebFocusReportParser.By_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#by_command.
    def exitBy_command(self, ctx:WebFocusReportParser.By_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#across_command.
    def enterAcross_command(self, ctx:WebFocusReportParser.Across_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#across_command.
    def exitAcross_command(self, ctx:WebFocusReportParser.Across_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#sort_options.
    def enterSort_options(self, ctx:WebFocusReportParser.Sort_optionsContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#sort_options.
    def exitSort_options(self, ctx:WebFocusReportParser.Sort_optionsContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#where_command.
    def enterWhere_command(self, ctx:WebFocusReportParser.Where_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#where_command.
    def exitWhere_command(self, ctx:WebFocusReportParser.Where_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#heading_command.
    def enterHeading_command(self, ctx:WebFocusReportParser.Heading_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#heading_command.
    def exitHeading_command(self, ctx:WebFocusReportParser.Heading_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#footing_command.
    def enterFooting_command(self, ctx:WebFocusReportParser.Footing_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#footing_command.
    def exitFooting_command(self, ctx:WebFocusReportParser.Footing_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#on_command.
    def enterOn_command(self, ctx:WebFocusReportParser.On_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#on_command.
    def exitOn_command(self, ctx:WebFocusReportParser.On_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#on_table_options.
    def enterOn_table_options(self, ctx:WebFocusReportParser.On_table_optionsContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#on_table_options.
    def exitOn_table_options(self, ctx:WebFocusReportParser.On_table_optionsContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#on_field_options.
    def enterOn_field_options(self, ctx:WebFocusReportParser.On_field_optionsContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#on_field_options.
    def exitOn_field_options(self, ctx:WebFocusReportParser.On_field_optionsContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#summarize_command.
    def enterSummarize_command(self, ctx:WebFocusReportParser.Summarize_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#summarize_command.
    def exitSummarize_command(self, ctx:WebFocusReportParser.Summarize_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#summarize_options.
    def enterSummarize_options(self, ctx:WebFocusReportParser.Summarize_optionsContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#summarize_options.
    def exitSummarize_options(self, ctx:WebFocusReportParser.Summarize_optionsContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#output_command.
    def enterOutput_command(self, ctx:WebFocusReportParser.Output_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#output_command.
    def exitOutput_command(self, ctx:WebFocusReportParser.Output_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#end_command.
    def enterEnd_command(self, ctx:WebFocusReportParser.End_commandContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#end_command.
    def exitEnd_command(self, ctx:WebFocusReportParser.End_commandContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#qualified_name.
    def enterQualified_name(self, ctx:WebFocusReportParser.Qualified_nameContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#qualified_name.
    def exitQualified_name(self, ctx:WebFocusReportParser.Qualified_nameContext):
        pass


    # Enter a parse tree produced by WebFocusReportParser#prefix_operator.
    def enterPrefix_operator(self, ctx:WebFocusReportParser.Prefix_operatorContext):
        pass

    # Exit a parse tree produced by WebFocusReportParser#prefix_operator.
    def exitPrefix_operator(self, ctx:WebFocusReportParser.Prefix_operatorContext):
        pass



del WebFocusReportParser