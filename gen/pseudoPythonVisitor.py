# Generated from D:/Programming/PycharmProjects/miak\pseudoPython.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pseudoPythonParser import pseudoPythonParser
else:
    from pseudoPythonParser import pseudoPythonParser

# This class defines a complete generic visitor for a parse tree produced by pseudoPythonParser.

class pseudoPythonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pseudoPythonParser#program.
    def visitProgram(self, ctx:pseudoPythonParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#start.
    def visitStart(self, ctx:pseudoPythonParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#for_statement.
    def visitFor_statement(self, ctx:pseudoPythonParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#while_statement.
    def visitWhile_statement(self, ctx:pseudoPythonParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#if_statement.
    def visitIf_statement(self, ctx:pseudoPythonParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#return_statement.
    def visitReturn_statement(self, ctx:pseudoPythonParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#function_definition.
    def visitFunction_definition(self, ctx:pseudoPythonParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#array.
    def visitArray(self, ctx:pseudoPythonParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#expression.
    def visitExpression(self, ctx:pseudoPythonParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#statement.
    def visitStatement(self, ctx:pseudoPythonParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#declaration.
    def visitDeclaration(self, ctx:pseudoPythonParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#function_call.
    def visitFunction_call(self, ctx:pseudoPythonParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#variable_type.
    def visitVariable_type(self, ctx:pseudoPythonParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#array_element.
    def visitArray_element(self, ctx:pseudoPythonParser.Array_elementContext):
        return self.visitChildren(ctx)



del pseudoPythonParser