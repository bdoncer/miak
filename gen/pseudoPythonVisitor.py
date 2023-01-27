# Generated from /home/bdoncer/PycharmProjects/miak/pseudoPython.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pseudoPythonParser import pseudoPythonParser
else:
    from pseudoPythonParser import pseudoPythonParser

# This class defines a complete generic visitor for a parse tree produced by pseudoPythonParser.

class pseudoPythonVisitor(ParseTreeVisitor):

    def __init__(self):
        self.code = ""
        self.indent_ctr = 0

    def _add_to_code(self, token, communicat):
        communicat = str(communicat)

        if token == "ASSIGN":
            self.code += "="

        elif token in ("COMPARISON_OPERATORS", "MATH_OPERATORS"):
            if communicat == "=":
                communicat += "="
            self.code += communicat

        elif token == "CURLY_BRACKET_BEGIN":
            self.code += ":\n"
            self.indent_ctr += 1
            self.code += " " * 4 * self.indent_ctr

        elif token == "CURLY_BRACKET_END":
            self.code = self.code[:-4]
            self.indent_ctr -= 1

        elif token == "SEMICOLON":
            self.code += "\n"
            self.code += " " * 4 * self.indent_ctr

        elif token == "FUNCTION":
            self.code += "def "

        elif token == "BOOLEAN":
            self.code += communicat.capitalize()

        elif token in ["IF_TOKEN", "FOR_TOKEN", "OR_TOKEN", "AND_TOKEN", "NOT_TOKEN",
                       "RETURN_TOKEN", "FUNCTION"]:
            self.code += communicat + " "

        else:
            self.code += communicat

    # Visit a parse tree produced by pseudoPythonParser#program.
    def visitProgram(self, ctx:pseudoPythonParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#start.
    def visitStart(self, ctx:pseudoPythonParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#for_statement.
    def visitFor_statement(self, ctx:pseudoPythonParser.For_statementContext):
        token = ctx.getToken(pseudoPythonParser.FOR_TOKEN, 0)
        if token != None:
            self._add_to_code("FOR_TOKEN", token)

        token = ctx.getToken(pseudoPythonParser.ROUND_BRACKET_BEGIN, 0)
        if token != None:
            # self._add_to_code("ROUND_BRACKET_BEGIN", token)
            pass

        token = ctx.getToken(pseudoPythonParser.ID, 0)
        if token != None:
            self._add_to_code("ID", token)

        self.code += " in range("

        id_ctr = 1
        token = ctx.getToken(pseudoPythonParser.ID, id_ctr)
        if token != None:
            id_ctr += 1
            self._add_to_code("ID", token)

        nr_ctr = 0
        token = ctx.getToken(pseudoPythonParser.NUMBER, nr_ctr)
        if token != None:
            nr_ctr += 1
            self._add_to_code("NUMBER", token)

        self.code += ","


        token = ctx.getToken(pseudoPythonParser.ID, id_ctr)
        if token != None:
            self._add_to_code("ID", token)

        token = ctx.getToken(pseudoPythonParser.NUMBER, nr_ctr)
        if token != None:
            self._add_to_code("NUMBER", token)

        token = ctx.getToken(pseudoPythonParser.ROUND_BRACKET_END, 0)
        if token != None:
            self._add_to_code("ROUND_BRACKET_END", token)

        token = ctx.getToken(pseudoPythonParser.CURLY_BRACKET_BEGIN, 0)
        if token != None:
            self._add_to_code("CURLY_BRACKET_BEGIN", token)

        res = self.visitChildren(ctx)

        token = ctx.getToken(pseudoPythonParser.CURLY_BRACKET_END, 0)
        if token != None:
            self._add_to_code("CURLY_BRACKET_END", token)

    # Visit a parse tree produced by pseudoPythonParser#while_statement.
    def visitWhile_statement(self, ctx:pseudoPythonParser.While_statementContext):
        token = ctx.getToken(pseudoPythonParser.WHILE_TOKEN, 0)
        if token != None:
            self._add_to_code("WHILE_TOKEN", token)

        token = ctx.getToken(pseudoPythonParser.ROUND_BRACKET_BEGIN, 0)
        if token != None:
            # self._add_to_code("ROUND_BRACKET_BEGIN", token)
            pass
        c = ctx.getChild(2)
        c.accept(self)

        token = ctx.getToken(pseudoPythonParser.ROUND_BRACKET_END, 0)
        if token != None:
            # self._add_to_code("ROUND_BRACKET_END", token)
            pass
        token = ctx.getToken(pseudoPythonParser.CURLY_BRACKET_BEGIN, 0)
        if token != None:
            self._add_to_code("CURLY_BRACKET_BEGIN", token)

        c = ctx.getChild(5)
        c.accept(self)

        token = ctx.getToken(pseudoPythonParser.CURLY_BRACKET_END, 0)
        if token != None:
            self._add_to_code("CURLY_BRACKET_END", token)


    # Visit a parse tree produced by pseudoPythonParser#if_statement.
    def visitIf_statement(self, ctx:pseudoPythonParser.If_statementContext):
        token = ctx.getToken(pseudoPythonParser.IF_TOKEN, 0)
        if token != None:
            self._add_to_code("IF_TOKEN", token)

        token = ctx.getToken(pseudoPythonParser.ROUND_BRACKET_BEGIN, 0)
        if token != None:
            # self._add_to_code("ROUND_BRACKET_BEGIN", token)
            pass
        c = ctx.getChild(2)
        c.accept(self)

        token = ctx.getToken(pseudoPythonParser.ROUND_BRACKET_END, 0)
        if token != None:
            # self._add_to_code("ROUND_BRACKET_END", token)
            pass
        token = ctx.getToken(pseudoPythonParser.CURLY_BRACKET_BEGIN, 0)
        if token != None:
            self._add_to_code("CURLY_BRACKET_BEGIN", token)

        c = ctx.getChild(5)
        c.accept(self)

        token = ctx.getToken(pseudoPythonParser.CURLY_BRACKET_END, 0)
        if token != None:
            self._add_to_code("CURLY_BRACKET_END", token)

        token = ctx.getToken(pseudoPythonParser.ELSE_TOKEN, 0)
        if token != None:
            self._add_to_code("ELSE_TOKEN", token)

            token = ctx.getToken(pseudoPythonParser.CURLY_BRACKET_BEGIN, 1)
            if token != None:
                self._add_to_code("CURLY_BRACKET_BEGIN", token)

            c = ctx.getChild(9)
            c.accept(self)

            token = ctx.getToken(pseudoPythonParser.CURLY_BRACKET_END, 1)
            if token != None:
                self._add_to_code("CURLY_BRACKET_END", token)



    # Visit a parse tree produced by pseudoPythonParser#return_statement.
    def visitReturn_statement(self, ctx:pseudoPythonParser.Return_statementContext):
        token = ctx.getToken(pseudoPythonParser.RETURN_TOKEN, 0)
        if token != None:
            self._add_to_code("RETURN_TOKEN", token)

        res = self.visitChildren(ctx)

        token = ctx.getToken(pseudoPythonParser.SEMICOLON, 0)
        if token != None:
            self._add_to_code("SEMICOLON", token)


    # Visit a parse tree produced by pseudoPythonParser#function_definition.
    def visitFunction_definition(self, ctx:pseudoPythonParser.Function_definitionContext):
        token = ctx.getToken(pseudoPythonParser.FUNCTION_TOKEN, 0)
        if token != None:
            self._add_to_code('FUNCTION', token)

        token = ctx.getToken(pseudoPythonParser.ID, 0)
        if token != None:
            self._add_to_code('ID', token)

        token = ctx.getToken(pseudoPythonParser.ROUND_BRACKET_BEGIN, 0)
        if token != None:
            self._add_to_code('ROUND_BRACKET_BEGIN', token)

        token = ctx.getToken(pseudoPythonParser.ID, 1)
        if token != None:
            self._add_to_code('ID', token)


        id_ctr = 2
        comma_ctr = 0
        while token != None:
            token = ctx.getToken(pseudoPythonParser.COMMA, comma_ctr)
            comma_ctr += 1
            if token == None:
                break
            self._add_to_code('COMMA', token)
            token = ctx.getToken(pseudoPythonParser.ID, id_ctr)
            id_ctr += 1
            self._add_to_code('ID', token)

        token = ctx.getToken(pseudoPythonParser.ROUND_BRACKET_END, 0)
        if token != None:
            self._add_to_code('ROUND_BRACKET_END', token)

        token = ctx.getToken(pseudoPythonParser.CURLY_BRACKET_BEGIN, 0)
        if token != None:
            self._add_to_code('CURLY_BRACKET_BEGIN', token)

        res = self.visitChildren(ctx)

        token = ctx.getToken(pseudoPythonParser.CURLY_BRACKET_END, 0)
        if token != None:
            self._add_to_code('CURLY_BRACKET_END', token)
        return res


    # Visit a parse tree produced by pseudoPythonParser#array.
    def visitArray(self, ctx:pseudoPythonParser.ArrayContext):
        token = ctx.getToken(pseudoPythonParser.SQUARE_BRACKET_BEGIN, 0)
        if token != None:
            self._add_to_code('SQUARE_BRACKET_BEGIN', token)

        node = ctx
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            c = node.getChild(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)
            if i == 0 or i ==n-1 or i %2 != 0:
                continue
            self._add_to_code('COMMA', ',')

        token = ctx.getToken(pseudoPythonParser.SQUARE_BRACKET_END, 0)
        if token != None:
            self._add_to_code('SQUARE_BRACKET_END', token)


    # Visit a parse tree produced by pseudoPythonParser#expression.
    def visitExpression(self, ctx:pseudoPythonParser.ExpressionContext):
        flag = 0
        token = ctx.getToken(pseudoPythonParser.NOT_TOKEN, 0)
        if token != None:
            self._add_to_code('NOT_TOKEN', token)
            flag += 1

        c = ctx.getChild(flag)
        c.accept(self)

        token = ctx.getToken(pseudoPythonParser.AND_TOKEN, 0)
        if token != None:
            self._add_to_code('AND_TOKEN', token)

        token = ctx.getToken(pseudoPythonParser.OR_TOKEN, 0)
        if token != None:
            self._add_to_code('OR_TOKEN', token)

        token = ctx.getToken(pseudoPythonParser.COMPARISON_OPERATORS, 0)
        if token != None:
            self._add_to_code('COMPARISON_OPERATORS', token)

        token = ctx.getToken(pseudoPythonParser.MATH_OPERATORS, 0)
        if token != None:
            self._add_to_code('MATH_OPERATORS', token)

        c = ctx.getChild(2+flag)
        c.accept(self)

    # Visit a parse tree produced by pseudoPythonParser#statement.
    def visitStatement(self, ctx:pseudoPythonParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pseudoPythonParser#declaration.
    def visitDeclaration(self, ctx:pseudoPythonParser.DeclarationContext):
        token = ctx.getToken(pseudoPythonParser.ID, 0)
        if token != None:
            self._add_to_code('ID', token)


        token = ctx.getToken(pseudoPythonParser.SQUARE_BRACKET_BEGIN, 0)
        if token != None:
            self._add_to_code('SQUARE_BRACKET_BEGIN', token)

        token = ctx.getToken(pseudoPythonParser.NUMBER, 0)
        if token != None:
            self._add_to_code('NUMBER', token)

        token = ctx.getToken(pseudoPythonParser.SQUARE_BRACKET_END, 0)
        if token != None:
            self._add_to_code('SQUARE_BRACKET_END', token)

        token = ctx.getToken(pseudoPythonParser.ASSIGN, 0)
        if token != None:
            self._add_to_code('ASSIGN', token)

        res = self.visitChildren(ctx)

        token = ctx.getToken(pseudoPythonParser.SEMICOLON, 0)
        if token != None:
            self._add_to_code('SEMICOLON', token)

        return res




    # Visit a parse tree produced by pseudoPythonParser#function_call.
    def visitFunction_call(self, ctx:pseudoPythonParser.Function_callContext):
        token = ctx.getToken(pseudoPythonParser.ID, 0)
        if token != None:
            self._add_to_code('ID', token)

        token = ctx.getToken(pseudoPythonParser.ROUND_BRACKET_BEGIN, 0)
        if token != None:
            self._add_to_code('ROUND_BRACKET_BEGIN', token)

        node = ctx
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            c = node.getChild(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)
            if i == 0 or i == n - 1 or  i== n-3 or i % 2 != 0:
                continue
            self._add_to_code('COMMA', ',')

        token = ctx.getToken(pseudoPythonParser.ROUND_BRACKET_END, 0)
        if token != None:
            self._add_to_code('ROUND_BRACKET_END', token)

        token = ctx.getToken(pseudoPythonParser.SEMICOLON, 0)
        if token != None:
            self._add_to_code('SEMICOLON', token)

    # Visit a parse tree produced by pseudoPythonParser#variable_type.
    def visitVariable_type(self, ctx: pseudoPythonParser.Variable_typeContext):

        token = ctx.getToken(pseudoPythonParser.BOOLEAN, 0)
        if token != None:
            self._add_to_code('BOOLEAN', token)

        token = ctx.getToken(pseudoPythonParser.ID, 0)
        if token != None:
            self._add_to_code('ID', token)

        token = ctx.getToken(pseudoPythonParser.NUMBER, 0)
        if token != None:
            self._add_to_code('NUMBER', token)

        token = ctx.getToken(pseudoPythonParser.STRING, 0)
        if token != None:
            self._add_to_code('STRING', token)

        res = self.visitChildren(ctx)

        return res

    # Visit a parse tree produced by pseudoPythonParser#array_element.
    def visitArray_element(self, ctx:pseudoPythonParser.Array_elementContext):
        token = ctx.getToken(pseudoPythonParser.ID, 0)
        if token != None:
            self._add_to_code('ID', token)

        token = ctx.getToken(pseudoPythonParser.SQUARE_BRACKET_BEGIN, 0)
        if token != None:
            self._add_to_code('SQUARE_BRACKET_BEGIN', token)
        res = self.visitChildren(ctx)

        token = ctx.getToken(pseudoPythonParser.SQUARE_BRACKET_END, 0)
        if token != None:
            self._add_to_code('SQUARE_BRACKET_END', token)

        return res



#del pseudoPythonParser