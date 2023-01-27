# Generated from /home/bdoncer/PycharmProjects/miak/pseudoPython.g4 by ANTLR 4.11.1
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
        4,1,27,188,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,50,8,2,11,2,12,2,51,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,4,3,63,8,3,11,3,12,3,64,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,4,4,76,8,4,11,4,12,4,77,1,4,1,4,1,4,1,4,1,4,
        4,4,85,8,4,11,4,12,4,86,1,4,3,4,90,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,5,6,102,8,6,10,6,12,6,105,9,6,3,6,107,8,6,1,6,1,6,
        1,6,4,6,112,8,6,11,6,12,6,113,1,6,3,6,117,8,6,1,6,1,6,1,7,1,7,1,
        7,1,7,5,7,125,8,7,10,7,12,7,128,9,7,1,7,1,7,1,8,3,8,133,8,8,1,8,
        1,8,1,8,1,8,3,8,139,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,148,8,9,
        1,10,1,10,1,10,1,10,3,10,154,8,10,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,5,11,165,8,11,10,11,12,11,168,9,11,3,11,170,8,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,181,8,12,1,13,
        1,13,1,13,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,0,2,1,0,24,25,2,0,7,8,18,19,205,0,31,1,0,0,0,2,36,1,0,0,0,4,38,
        1,0,0,0,6,55,1,0,0,0,8,68,1,0,0,0,10,91,1,0,0,0,12,95,1,0,0,0,14,
        120,1,0,0,0,16,132,1,0,0,0,18,147,1,0,0,0,20,149,1,0,0,0,22,159,
        1,0,0,0,24,180,1,0,0,0,26,182,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,
        0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,
        1,0,0,0,34,35,5,0,0,1,35,1,1,0,0,0,36,37,3,18,9,0,37,3,1,0,0,0,38,
        39,5,5,0,0,39,40,5,14,0,0,40,41,5,24,0,0,41,42,5,1,0,0,42,43,7,0,
        0,0,43,44,5,21,0,0,44,45,7,0,0,0,45,46,5,15,0,0,46,49,5,12,0,0,47,
        50,3,18,9,0,48,50,5,9,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,51,1,0,
        0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,13,0,0,54,
        5,1,0,0,0,55,56,5,4,0,0,56,57,5,14,0,0,57,58,3,16,8,0,58,59,5,15,
        0,0,59,62,5,12,0,0,60,63,3,18,9,0,61,63,5,9,0,0,62,60,1,0,0,0,62,
        61,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,66,1,0,0,
        0,66,67,5,13,0,0,67,7,1,0,0,0,68,69,5,2,0,0,69,70,5,14,0,0,70,71,
        3,16,8,0,71,72,5,15,0,0,72,75,5,12,0,0,73,76,3,18,9,0,74,76,5,9,
        0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,77,1,0,0,0,77,75,1,0,0,0,77,78,
        1,0,0,0,78,79,1,0,0,0,79,89,5,13,0,0,80,81,5,3,0,0,81,84,5,12,0,
        0,82,85,3,18,9,0,83,85,5,9,0,0,84,82,1,0,0,0,84,83,1,0,0,0,85,86,
        1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,90,5,13,0,0,
        89,80,1,0,0,0,89,90,1,0,0,0,90,9,1,0,0,0,91,92,5,6,0,0,92,93,3,24,
        12,0,93,94,5,26,0,0,94,11,1,0,0,0,95,96,5,11,0,0,96,97,5,24,0,0,
        97,106,5,14,0,0,98,103,5,24,0,0,99,100,5,20,0,0,100,102,5,24,0,0,
        101,99,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,
        107,1,0,0,0,105,103,1,0,0,0,106,98,1,0,0,0,106,107,1,0,0,0,107,108,
        1,0,0,0,108,109,5,15,0,0,109,111,5,12,0,0,110,112,3,18,9,0,111,110,
        1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,116,
        1,0,0,0,115,117,3,10,5,0,116,115,1,0,0,0,116,117,1,0,0,0,117,118,
        1,0,0,0,118,119,5,13,0,0,119,13,1,0,0,0,120,121,5,16,0,0,121,126,
        3,24,12,0,122,123,5,20,0,0,123,125,3,24,12,0,124,122,1,0,0,0,125,
        128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,129,1,0,0,0,128,
        126,1,0,0,0,129,130,5,17,0,0,130,15,1,0,0,0,131,133,5,10,0,0,132,
        131,1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,135,3,24,12,0,135,
        138,7,1,0,0,136,139,3,24,12,0,137,139,3,16,8,0,138,136,1,0,0,0,138,
        137,1,0,0,0,139,17,1,0,0,0,140,148,3,4,2,0,141,148,3,6,3,0,142,148,
        3,8,4,0,143,148,3,10,5,0,144,148,3,20,10,0,145,148,3,22,11,0,146,
        148,3,12,6,0,147,140,1,0,0,0,147,141,1,0,0,0,147,142,1,0,0,0,147,
        143,1,0,0,0,147,144,1,0,0,0,147,145,1,0,0,0,147,146,1,0,0,0,148,
        19,1,0,0,0,149,153,5,24,0,0,150,151,5,16,0,0,151,152,5,25,0,0,152,
        154,5,17,0,0,153,150,1,0,0,0,153,154,1,0,0,0,154,155,1,0,0,0,155,
        156,5,1,0,0,156,157,3,24,12,0,157,158,5,26,0,0,158,21,1,0,0,0,159,
        160,5,24,0,0,160,169,5,14,0,0,161,166,3,24,12,0,162,165,5,20,0,0,
        163,165,3,24,12,0,164,162,1,0,0,0,164,163,1,0,0,0,165,168,1,0,0,
        0,166,164,1,0,0,0,166,167,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,
        0,169,161,1,0,0,0,169,170,1,0,0,0,170,171,1,0,0,0,171,172,5,15,0,
        0,172,173,5,26,0,0,173,23,1,0,0,0,174,181,3,26,13,0,175,181,5,23,
        0,0,176,181,5,24,0,0,177,181,5,25,0,0,178,181,3,14,7,0,179,181,5,
        27,0,0,180,174,1,0,0,0,180,175,1,0,0,0,180,176,1,0,0,0,180,177,1,
        0,0,0,180,178,1,0,0,0,180,179,1,0,0,0,181,25,1,0,0,0,182,183,5,24,
        0,0,183,184,5,16,0,0,184,185,3,24,12,0,185,186,5,17,0,0,186,27,1,
        0,0,0,23,31,49,51,62,64,75,77,84,86,89,103,106,113,116,126,132,138,
        147,153,164,166,169,180
    ]

class pseudoPythonParser ( Parser ):

    grammarFileName = "pseudoPython.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "'if'", "'else'", "'while'", "'for'", 
                     "'return'", "'and'", "'or'", "'skip'", "'not'", "'function'", 
                     "'{'", "'}'", "'('", "')'", "'['", "']'", "<INVALID>", 
                     "<INVALID>", "','", "'...'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "ASSIGN", "IF_TOKEN", "ELSE_TOKEN", "WHILE_TOKEN", 
                      "FOR_TOKEN", "RETURN_TOKEN", "AND_TOKEN", "OR_TOKEN", 
                      "SKIP_TOKEN", "NOT_TOKEN", "FUNCTION_TOKEN", "CURLY_BRACKET_BEGIN", 
                      "CURLY_BRACKET_END", "ROUND_BRACKET_BEGIN", "ROUND_BRACKET_END", 
                      "SQUARE_BRACKET_BEGIN", "SQUARE_BRACKET_END", "COMPARISON_OPERATORS", 
                      "MATH_OPERATORS", "COMMA", "BETWEEN", "WHITESPACE", 
                      "BOOLEAN", "ID", "NUMBER", "SEMICOLON", "STRING" ]

    RULE_program = 0
    RULE_start = 1
    RULE_for_statement = 2
    RULE_while_statement = 3
    RULE_if_statement = 4
    RULE_return_statement = 5
    RULE_function_definition = 6
    RULE_array = 7
    RULE_expression = 8
    RULE_statement = 9
    RULE_declaration = 10
    RULE_function_call = 11
    RULE_variable_type = 12
    RULE_array_element = 13

    ruleNames =  [ "program", "start", "for_statement", "while_statement", 
                   "if_statement", "return_statement", "function_definition", 
                   "array", "expression", "statement", "declaration", "function_call", 
                   "variable_type", "array_element" ]

    EOF = Token.EOF
    ASSIGN=1
    IF_TOKEN=2
    ELSE_TOKEN=3
    WHILE_TOKEN=4
    FOR_TOKEN=5
    RETURN_TOKEN=6
    AND_TOKEN=7
    OR_TOKEN=8
    SKIP_TOKEN=9
    NOT_TOKEN=10
    FUNCTION_TOKEN=11
    CURLY_BRACKET_BEGIN=12
    CURLY_BRACKET_END=13
    ROUND_BRACKET_BEGIN=14
    ROUND_BRACKET_END=15
    SQUARE_BRACKET_BEGIN=16
    SQUARE_BRACKET_END=17
    COMPARISON_OPERATORS=18
    MATH_OPERATORS=19
    COMMA=20
    BETWEEN=21
    WHITESPACE=22
    BOOLEAN=23
    ID=24
    NUMBER=25
    SEMICOLON=26
    STRING=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(pseudoPythonParser.EOF, 0)

        def start(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pseudoPythonParser.StartContext)
            else:
                return self.getTypedRuleContext(pseudoPythonParser.StartContext,i)


        def getRuleIndex(self):
            return pseudoPythonParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = pseudoPythonParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 16779380) != 0:
                self.state = 28
                self.start()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(pseudoPythonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(pseudoPythonParser.StatementContext,0)


        def getRuleIndex(self):
            return pseudoPythonParser.RULE_start

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

        localctx = pseudoPythonParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_TOKEN(self):
            return self.getToken(pseudoPythonParser.FOR_TOKEN, 0)

        def ROUND_BRACKET_BEGIN(self):
            return self.getToken(pseudoPythonParser.ROUND_BRACKET_BEGIN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(pseudoPythonParser.ID)
            else:
                return self.getToken(pseudoPythonParser.ID, i)

        def ASSIGN(self):
            return self.getToken(pseudoPythonParser.ASSIGN, 0)

        def BETWEEN(self):
            return self.getToken(pseudoPythonParser.BETWEEN, 0)

        def ROUND_BRACKET_END(self):
            return self.getToken(pseudoPythonParser.ROUND_BRACKET_END, 0)

        def CURLY_BRACKET_BEGIN(self):
            return self.getToken(pseudoPythonParser.CURLY_BRACKET_BEGIN, 0)

        def CURLY_BRACKET_END(self):
            return self.getToken(pseudoPythonParser.CURLY_BRACKET_END, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(pseudoPythonParser.NUMBER)
            else:
                return self.getToken(pseudoPythonParser.NUMBER, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pseudoPythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(pseudoPythonParser.StatementContext,i)


        def SKIP_TOKEN(self, i:int=None):
            if i is None:
                return self.getTokens(pseudoPythonParser.SKIP_TOKEN)
            else:
                return self.getToken(pseudoPythonParser.SKIP_TOKEN, i)

        def getRuleIndex(self):
            return pseudoPythonParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = pseudoPythonParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(pseudoPythonParser.FOR_TOKEN)
            self.state = 39
            self.match(pseudoPythonParser.ROUND_BRACKET_BEGIN)
            self.state = 40
            self.match(pseudoPythonParser.ID)
            self.state = 41
            self.match(pseudoPythonParser.ASSIGN)
            self.state = 42
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 43
            self.match(pseudoPythonParser.BETWEEN)
            self.state = 44
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 45
            self.match(pseudoPythonParser.ROUND_BRACKET_END)
            self.state = 46
            self.match(pseudoPythonParser.CURLY_BRACKET_BEGIN)
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 4, 5, 6, 11, 24]:
                    self.state = 47
                    self.statement()
                    pass
                elif token in [9]:
                    self.state = 48
                    self.match(pseudoPythonParser.SKIP_TOKEN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 16779892) != 0):
                    break

            self.state = 53
            self.match(pseudoPythonParser.CURLY_BRACKET_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE_TOKEN(self):
            return self.getToken(pseudoPythonParser.WHILE_TOKEN, 0)

        def ROUND_BRACKET_BEGIN(self):
            return self.getToken(pseudoPythonParser.ROUND_BRACKET_BEGIN, 0)

        def expression(self):
            return self.getTypedRuleContext(pseudoPythonParser.ExpressionContext,0)


        def ROUND_BRACKET_END(self):
            return self.getToken(pseudoPythonParser.ROUND_BRACKET_END, 0)

        def CURLY_BRACKET_BEGIN(self):
            return self.getToken(pseudoPythonParser.CURLY_BRACKET_BEGIN, 0)

        def CURLY_BRACKET_END(self):
            return self.getToken(pseudoPythonParser.CURLY_BRACKET_END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pseudoPythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(pseudoPythonParser.StatementContext,i)


        def SKIP_TOKEN(self, i:int=None):
            if i is None:
                return self.getTokens(pseudoPythonParser.SKIP_TOKEN)
            else:
                return self.getToken(pseudoPythonParser.SKIP_TOKEN, i)

        def getRuleIndex(self):
            return pseudoPythonParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = pseudoPythonParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(pseudoPythonParser.WHILE_TOKEN)
            self.state = 56
            self.match(pseudoPythonParser.ROUND_BRACKET_BEGIN)
            self.state = 57
            self.expression()
            self.state = 58
            self.match(pseudoPythonParser.ROUND_BRACKET_END)
            self.state = 59
            self.match(pseudoPythonParser.CURLY_BRACKET_BEGIN)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 4, 5, 6, 11, 24]:
                    self.state = 60
                    self.statement()
                    pass
                elif token in [9]:
                    self.state = 61
                    self.match(pseudoPythonParser.SKIP_TOKEN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 16779892) != 0):
                    break

            self.state = 66
            self.match(pseudoPythonParser.CURLY_BRACKET_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_TOKEN(self):
            return self.getToken(pseudoPythonParser.IF_TOKEN, 0)

        def ROUND_BRACKET_BEGIN(self):
            return self.getToken(pseudoPythonParser.ROUND_BRACKET_BEGIN, 0)

        def expression(self):
            return self.getTypedRuleContext(pseudoPythonParser.ExpressionContext,0)


        def ROUND_BRACKET_END(self):
            return self.getToken(pseudoPythonParser.ROUND_BRACKET_END, 0)

        def CURLY_BRACKET_BEGIN(self, i:int=None):
            if i is None:
                return self.getTokens(pseudoPythonParser.CURLY_BRACKET_BEGIN)
            else:
                return self.getToken(pseudoPythonParser.CURLY_BRACKET_BEGIN, i)

        def CURLY_BRACKET_END(self, i:int=None):
            if i is None:
                return self.getTokens(pseudoPythonParser.CURLY_BRACKET_END)
            else:
                return self.getToken(pseudoPythonParser.CURLY_BRACKET_END, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pseudoPythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(pseudoPythonParser.StatementContext,i)


        def SKIP_TOKEN(self, i:int=None):
            if i is None:
                return self.getTokens(pseudoPythonParser.SKIP_TOKEN)
            else:
                return self.getToken(pseudoPythonParser.SKIP_TOKEN, i)

        def ELSE_TOKEN(self):
            return self.getToken(pseudoPythonParser.ELSE_TOKEN, 0)

        def getRuleIndex(self):
            return pseudoPythonParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = pseudoPythonParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(pseudoPythonParser.IF_TOKEN)
            self.state = 69
            self.match(pseudoPythonParser.ROUND_BRACKET_BEGIN)
            self.state = 70
            self.expression()
            self.state = 71
            self.match(pseudoPythonParser.ROUND_BRACKET_END)
            self.state = 72
            self.match(pseudoPythonParser.CURLY_BRACKET_BEGIN)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 75
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 4, 5, 6, 11, 24]:
                    self.state = 73
                    self.statement()
                    pass
                elif token in [9]:
                    self.state = 74
                    self.match(pseudoPythonParser.SKIP_TOKEN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 16779892) != 0):
                    break

            self.state = 79
            self.match(pseudoPythonParser.CURLY_BRACKET_END)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 80
                self.match(pseudoPythonParser.ELSE_TOKEN)
                self.state = 81
                self.match(pseudoPythonParser.CURLY_BRACKET_BEGIN)
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 84
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [2, 4, 5, 6, 11, 24]:
                        self.state = 82
                        self.statement()
                        pass
                    elif token in [9]:
                        self.state = 83
                        self.match(pseudoPythonParser.SKIP_TOKEN)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 86 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 16779892) != 0):
                        break

                self.state = 88
                self.match(pseudoPythonParser.CURLY_BRACKET_END)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_TOKEN(self):
            return self.getToken(pseudoPythonParser.RETURN_TOKEN, 0)

        def variable_type(self):
            return self.getTypedRuleContext(pseudoPythonParser.Variable_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(pseudoPythonParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return pseudoPythonParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = pseudoPythonParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(pseudoPythonParser.RETURN_TOKEN)
            self.state = 92
            self.variable_type()
            self.state = 93
            self.match(pseudoPythonParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_TOKEN(self):
            return self.getToken(pseudoPythonParser.FUNCTION_TOKEN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(pseudoPythonParser.ID)
            else:
                return self.getToken(pseudoPythonParser.ID, i)

        def ROUND_BRACKET_BEGIN(self):
            return self.getToken(pseudoPythonParser.ROUND_BRACKET_BEGIN, 0)

        def ROUND_BRACKET_END(self):
            return self.getToken(pseudoPythonParser.ROUND_BRACKET_END, 0)

        def CURLY_BRACKET_BEGIN(self):
            return self.getToken(pseudoPythonParser.CURLY_BRACKET_BEGIN, 0)

        def CURLY_BRACKET_END(self):
            return self.getToken(pseudoPythonParser.CURLY_BRACKET_END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pseudoPythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(pseudoPythonParser.StatementContext,i)


        def return_statement(self):
            return self.getTypedRuleContext(pseudoPythonParser.Return_statementContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(pseudoPythonParser.COMMA)
            else:
                return self.getToken(pseudoPythonParser.COMMA, i)

        def getRuleIndex(self):
            return pseudoPythonParser.RULE_function_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition" ):
                listener.enterFunction_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition" ):
                listener.exitFunction_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition" ):
                return visitor.visitFunction_definition(self)
            else:
                return visitor.visitChildren(self)




    def function_definition(self):

        localctx = pseudoPythonParser.Function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(pseudoPythonParser.FUNCTION_TOKEN)
            self.state = 96
            self.match(pseudoPythonParser.ID)
            self.state = 97
            self.match(pseudoPythonParser.ROUND_BRACKET_BEGIN)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 98
                self.match(pseudoPythonParser.ID)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 99
                    self.match(pseudoPythonParser.COMMA)
                    self.state = 100
                    self.match(pseudoPythonParser.ID)
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 108
            self.match(pseudoPythonParser.ROUND_BRACKET_END)
            self.state = 109
            self.match(pseudoPythonParser.CURLY_BRACKET_BEGIN)
            self.state = 111 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 110
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 113 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 115
                self.return_statement()


            self.state = 118
            self.match(pseudoPythonParser.CURLY_BRACKET_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQUARE_BRACKET_BEGIN(self):
            return self.getToken(pseudoPythonParser.SQUARE_BRACKET_BEGIN, 0)

        def variable_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pseudoPythonParser.Variable_typeContext)
            else:
                return self.getTypedRuleContext(pseudoPythonParser.Variable_typeContext,i)


        def SQUARE_BRACKET_END(self):
            return self.getToken(pseudoPythonParser.SQUARE_BRACKET_END, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(pseudoPythonParser.COMMA)
            else:
                return self.getToken(pseudoPythonParser.COMMA, i)

        def getRuleIndex(self):
            return pseudoPythonParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = pseudoPythonParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(pseudoPythonParser.SQUARE_BRACKET_BEGIN)
            self.state = 121
            self.variable_type()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 122
                self.match(pseudoPythonParser.COMMA)
                self.state = 123
                self.variable_type()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self.match(pseudoPythonParser.SQUARE_BRACKET_END)
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

        def variable_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pseudoPythonParser.Variable_typeContext)
            else:
                return self.getTypedRuleContext(pseudoPythonParser.Variable_typeContext,i)


        def AND_TOKEN(self):
            return self.getToken(pseudoPythonParser.AND_TOKEN, 0)

        def OR_TOKEN(self):
            return self.getToken(pseudoPythonParser.OR_TOKEN, 0)

        def COMPARISON_OPERATORS(self):
            return self.getToken(pseudoPythonParser.COMPARISON_OPERATORS, 0)

        def MATH_OPERATORS(self):
            return self.getToken(pseudoPythonParser.MATH_OPERATORS, 0)

        def expression(self):
            return self.getTypedRuleContext(pseudoPythonParser.ExpressionContext,0)


        def NOT_TOKEN(self):
            return self.getToken(pseudoPythonParser.NOT_TOKEN, 0)

        def getRuleIndex(self):
            return pseudoPythonParser.RULE_expression

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

        localctx = pseudoPythonParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 131
                self.match(pseudoPythonParser.NOT_TOKEN)


            self.state = 134
            self.variable_type()
            self.state = 135
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 786816) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 136
                self.variable_type()
                pass

            elif la_ == 2:
                self.state = 137
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_statement(self):
            return self.getTypedRuleContext(pseudoPythonParser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(pseudoPythonParser.While_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(pseudoPythonParser.If_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(pseudoPythonParser.Return_statementContext,0)


        def declaration(self):
            return self.getTypedRuleContext(pseudoPythonParser.DeclarationContext,0)


        def function_call(self):
            return self.getTypedRuleContext(pseudoPythonParser.Function_callContext,0)


        def function_definition(self):
            return self.getTypedRuleContext(pseudoPythonParser.Function_definitionContext,0)


        def getRuleIndex(self):
            return pseudoPythonParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = pseudoPythonParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 140
                self.for_statement()
                pass

            elif la_ == 2:
                self.state = 141
                self.while_statement()
                pass

            elif la_ == 3:
                self.state = 142
                self.if_statement()
                pass

            elif la_ == 4:
                self.state = 143
                self.return_statement()
                pass

            elif la_ == 5:
                self.state = 144
                self.declaration()
                pass

            elif la_ == 6:
                self.state = 145
                self.function_call()
                pass

            elif la_ == 7:
                self.state = 146
                self.function_definition()
                pass


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

        def ID(self):
            return self.getToken(pseudoPythonParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(pseudoPythonParser.ASSIGN, 0)

        def variable_type(self):
            return self.getTypedRuleContext(pseudoPythonParser.Variable_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(pseudoPythonParser.SEMICOLON, 0)

        def SQUARE_BRACKET_BEGIN(self):
            return self.getToken(pseudoPythonParser.SQUARE_BRACKET_BEGIN, 0)

        def NUMBER(self):
            return self.getToken(pseudoPythonParser.NUMBER, 0)

        def SQUARE_BRACKET_END(self):
            return self.getToken(pseudoPythonParser.SQUARE_BRACKET_END, 0)

        def getRuleIndex(self):
            return pseudoPythonParser.RULE_declaration

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

        localctx = pseudoPythonParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(pseudoPythonParser.ID)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 150
                self.match(pseudoPythonParser.SQUARE_BRACKET_BEGIN)
                self.state = 151
                self.match(pseudoPythonParser.NUMBER)
                self.state = 152
                self.match(pseudoPythonParser.SQUARE_BRACKET_END)


            self.state = 155
            self.match(pseudoPythonParser.ASSIGN)
            self.state = 156
            self.variable_type()
            self.state = 157
            self.match(pseudoPythonParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(pseudoPythonParser.ID, 0)

        def ROUND_BRACKET_BEGIN(self):
            return self.getToken(pseudoPythonParser.ROUND_BRACKET_BEGIN, 0)

        def ROUND_BRACKET_END(self):
            return self.getToken(pseudoPythonParser.ROUND_BRACKET_END, 0)

        def SEMICOLON(self):
            return self.getToken(pseudoPythonParser.SEMICOLON, 0)

        def variable_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pseudoPythonParser.Variable_typeContext)
            else:
                return self.getTypedRuleContext(pseudoPythonParser.Variable_typeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(pseudoPythonParser.COMMA)
            else:
                return self.getToken(pseudoPythonParser.COMMA, i)

        def getRuleIndex(self):
            return pseudoPythonParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = pseudoPythonParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(pseudoPythonParser.ID)
            self.state = 160
            self.match(pseudoPythonParser.ROUND_BRACKET_BEGIN)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 193003520) != 0:
                self.state = 161
                self.variable_type()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 194052096) != 0:
                    self.state = 164
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [20]:
                        self.state = 162
                        self.match(pseudoPythonParser.COMMA)
                        pass
                    elif token in [16, 23, 24, 25, 27]:
                        self.state = 163
                        self.variable_type()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 171
            self.match(pseudoPythonParser.ROUND_BRACKET_END)
            self.state = 172
            self.match(pseudoPythonParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(pseudoPythonParser.Array_elementContext,0)


        def BOOLEAN(self):
            return self.getToken(pseudoPythonParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(pseudoPythonParser.ID, 0)

        def NUMBER(self):
            return self.getToken(pseudoPythonParser.NUMBER, 0)

        def array(self):
            return self.getTypedRuleContext(pseudoPythonParser.ArrayContext,0)


        def STRING(self):
            return self.getToken(pseudoPythonParser.STRING, 0)

        def getRuleIndex(self):
            return pseudoPythonParser.RULE_variable_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_type" ):
                listener.enterVariable_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_type" ):
                listener.exitVariable_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_type" ):
                return visitor.visitVariable_type(self)
            else:
                return visitor.visitChildren(self)




    def variable_type(self):

        localctx = pseudoPythonParser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variable_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 174
                self.array_element()
                pass

            elif la_ == 2:
                self.state = 175
                self.match(pseudoPythonParser.BOOLEAN)
                pass

            elif la_ == 3:
                self.state = 176
                self.match(pseudoPythonParser.ID)
                pass

            elif la_ == 4:
                self.state = 177
                self.match(pseudoPythonParser.NUMBER)
                pass

            elif la_ == 5:
                self.state = 178
                self.array()
                pass

            elif la_ == 6:
                self.state = 179
                self.match(pseudoPythonParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(pseudoPythonParser.ID, 0)

        def SQUARE_BRACKET_BEGIN(self):
            return self.getToken(pseudoPythonParser.SQUARE_BRACKET_BEGIN, 0)

        def variable_type(self):
            return self.getTypedRuleContext(pseudoPythonParser.Variable_typeContext,0)


        def SQUARE_BRACKET_END(self):
            return self.getToken(pseudoPythonParser.SQUARE_BRACKET_END, 0)

        def getRuleIndex(self):
            return pseudoPythonParser.RULE_array_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_element" ):
                listener.enterArray_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_element" ):
                listener.exitArray_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = pseudoPythonParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(pseudoPythonParser.ID)
            self.state = 183
            self.match(pseudoPythonParser.SQUARE_BRACKET_BEGIN)
            self.state = 184
            self.variable_type()
            self.state = 185
            self.match(pseudoPythonParser.SQUARE_BRACKET_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





