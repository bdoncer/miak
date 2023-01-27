# Generated from D:/Programming/PycharmProjects/miak\pseudoPython.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pseudoPythonParser import pseudoPythonParser
else:
    from pseudoPythonParser import pseudoPythonParser

# This class defines a complete listener for a parse tree produced by pseudoPythonParser.
class pseudoPythonListener(ParseTreeListener):

    # Enter a parse tree produced by pseudoPythonParser#program.
    def enterProgram(self, ctx:pseudoPythonParser.ProgramContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#program.
    def exitProgram(self, ctx:pseudoPythonParser.ProgramContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#start.
    def enterStart(self, ctx:pseudoPythonParser.StartContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#start.
    def exitStart(self, ctx:pseudoPythonParser.StartContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#for_statement.
    def enterFor_statement(self, ctx:pseudoPythonParser.For_statementContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#for_statement.
    def exitFor_statement(self, ctx:pseudoPythonParser.For_statementContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#while_statement.
    def enterWhile_statement(self, ctx:pseudoPythonParser.While_statementContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#while_statement.
    def exitWhile_statement(self, ctx:pseudoPythonParser.While_statementContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#if_statement.
    def enterIf_statement(self, ctx:pseudoPythonParser.If_statementContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#if_statement.
    def exitIf_statement(self, ctx:pseudoPythonParser.If_statementContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#return_statement.
    def enterReturn_statement(self, ctx:pseudoPythonParser.Return_statementContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#return_statement.
    def exitReturn_statement(self, ctx:pseudoPythonParser.Return_statementContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#function_definition.
    def enterFunction_definition(self, ctx:pseudoPythonParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#function_definition.
    def exitFunction_definition(self, ctx:pseudoPythonParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#array.
    def enterArray(self, ctx:pseudoPythonParser.ArrayContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#array.
    def exitArray(self, ctx:pseudoPythonParser.ArrayContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#expression.
    def enterExpression(self, ctx:pseudoPythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#expression.
    def exitExpression(self, ctx:pseudoPythonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#statement.
    def enterStatement(self, ctx:pseudoPythonParser.StatementContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#statement.
    def exitStatement(self, ctx:pseudoPythonParser.StatementContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#declaration.
    def enterDeclaration(self, ctx:pseudoPythonParser.DeclarationContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#declaration.
    def exitDeclaration(self, ctx:pseudoPythonParser.DeclarationContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#function_call.
    def enterFunction_call(self, ctx:pseudoPythonParser.Function_callContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#function_call.
    def exitFunction_call(self, ctx:pseudoPythonParser.Function_callContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#variable_type.
    def enterVariable_type(self, ctx:pseudoPythonParser.Variable_typeContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#variable_type.
    def exitVariable_type(self, ctx:pseudoPythonParser.Variable_typeContext):
        pass


    # Enter a parse tree produced by pseudoPythonParser#array_element.
    def enterArray_element(self, ctx:pseudoPythonParser.Array_elementContext):
        pass

    # Exit a parse tree produced by pseudoPythonParser#array_element.
    def exitArray_element(self, ctx:pseudoPythonParser.Array_elementContext):
        pass



del pseudoPythonParser