# Generated from /Users/krishna/CIDAR/reggie/reggie.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\7\2\33")
        buf.write("\n\2\f\2\16\2\36\13\2\3\2\3\2\3\3\3\3\3\3\5\3%\n\3\3\3")
        buf.write("\5\3(\n\3\3\4\3\4\3\4\3\4\3\4\5\4/\n\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\5\5\66\n\5\3\6\3\6\3\7\3\7\3\7\7\7=\n\7\f\7\16\7")
        buf.write("@\13\7\3\7\3\7\3\7\3\7\7\7F\n\7\f\7\16\7I\13\7\3\7\5\7")
        buf.write("L\n\7\3\b\3\b\3\b\3\b\7\bR\n\b\f\b\16\bU\13\b\3\t\3\t")
        buf.write("\5\tY\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\2\2\f")
        buf.write("\2\4\6\b\n\f\16\20\22\24\2\3\4\2\17\17\22\22\2d\2\26\3")
        buf.write("\2\2\2\4!\3\2\2\2\6.\3\2\2\2\b\65\3\2\2\2\n\67\3\2\2\2")
        buf.write("\fK\3\2\2\2\16M\3\2\2\2\20X\3\2\2\2\22Z\3\2\2\2\24`\3")
        buf.write("\2\2\2\26\27\7\3\2\2\27\34\5\16\b\2\30\31\7\4\2\2\31\33")
        buf.write("\5\16\b\2\32\30\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2\34")
        buf.write("\35\3\2\2\2\35\37\3\2\2\2\36\34\3\2\2\2\37 \7\5\2\2 \3")
        buf.write("\3\2\2\2!$\5\n\6\2\"#\7\6\2\2#%\5\f\7\2$\"\3\2\2\2$%\3")
        buf.write("\2\2\2%\'\3\2\2\2&(\5\6\4\2\'&\3\2\2\2\'(\3\2\2\2(\5\3")
        buf.write("\2\2\2)*\7\7\2\2*/\7\25\2\2+/\7\21\2\2,-\7\20\2\2-/\7")
        buf.write("\b\2\2.)\3\2\2\2.+\3\2\2\2.,\3\2\2\2/\7\3\2\2\2\60\61")
        buf.write("\7\7\2\2\61\66\7\25\2\2\62\66\7\21\2\2\63\64\7\20\2\2")
        buf.write("\64\66\7\b\2\2\65\60\3\2\2\2\65\62\3\2\2\2\65\63\3\2\2")
        buf.write("\2\66\t\3\2\2\2\678\t\2\2\28\13\3\2\2\29>\7\17\2\2:;\7")
        buf.write("\t\2\2;=\7\17\2\2<:\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2")
        buf.write("\2\2?L\3\2\2\2@>\3\2\2\2AB\7\n\2\2BG\7\17\2\2CD\7\t\2")
        buf.write("\2DF\7\17\2\2EC\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2")
        buf.write("HJ\3\2\2\2IG\3\2\2\2JL\7\13\2\2K9\3\2\2\2KA\3\2\2\2L\r")
        buf.write("\3\2\2\2MS\5\4\3\2NO\5\20\t\2OP\5\4\3\2PR\3\2\2\2QN\3")
        buf.write("\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\17\3\2\2\2US\3\2")
        buf.write("\2\2VY\7\f\2\2WY\5\22\n\2XV\3\2\2\2XW\3\2\2\2Y\21\3\2")
        buf.write("\2\2Z[\7\r\2\2[\\\7\n\2\2\\]\5\24\13\2]^\7\13\2\2^_\7")
        buf.write("\16\2\2_\23\3\2\2\2`a\7\17\2\2a\25\3\2\2\2\f\34$\'.\65")
        buf.write(">GKSX")
        return buf.getvalue()


class reggieParser ( Parser ):

    grammarFileName = "reggie.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "':'", "'['", "']'", 
                     "'|'", "'('", "')'", "'->'", "'-'", "'>'", "<INVALID>", 
                     "'*'", "'+'", "'?'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "STAR_WILDCARD", "PLUS_WILDCARD", 
                      "QUESTIONMARK_WILDCARD", "WS", "NL", "INT" ]

    RULE_reggie = 0
    RULE_vertex = 1
    RULE_structuralvertexpattern = 2
    RULE_structuraledgepatther = 3
    RULE_structuralid = 4
    RULE_labelfilter = 5
    RULE_vertex2vertex = 6
    RULE_edge = 7
    RULE_labelledarraw = 8
    RULE_edgelabel = 9

    ruleNames =  [ "reggie", "vertex", "structuralvertexpattern", "structuraledgepatther", 
                   "structuralid", "labelfilter", "vertex2vertex", "edge", 
                   "labelledarraw", "edgelabel" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    ID=13
    STAR_WILDCARD=14
    PLUS_WILDCARD=15
    QUESTIONMARK_WILDCARD=16
    WS=17
    NL=18
    INT=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ReggieContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertex2vertex(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reggieParser.Vertex2vertexContext)
            else:
                return self.getTypedRuleContext(reggieParser.Vertex2vertexContext,i)


        def getRuleIndex(self):
            return reggieParser.RULE_reggie

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReggie" ):
                listener.enterReggie(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReggie" ):
                listener.exitReggie(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReggie" ):
                return visitor.visitReggie(self)
            else:
                return visitor.visitChildren(self)




    def reggie(self):

        localctx = reggieParser.ReggieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_reggie)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(reggieParser.T__0)
            self.state = 21
            self.vertex2vertex()
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==reggieParser.T__1:
                self.state = 22
                self.match(reggieParser.T__1)
                self.state = 23
                self.vertex2vertex()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(reggieParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VertexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structuralid(self):
            return self.getTypedRuleContext(reggieParser.StructuralidContext,0)


        def labelfilter(self):
            return self.getTypedRuleContext(reggieParser.LabelfilterContext,0)


        def structuralvertexpattern(self):
            return self.getTypedRuleContext(reggieParser.StructuralvertexpatternContext,0)


        def getRuleIndex(self):
            return reggieParser.RULE_vertex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertex" ):
                listener.enterVertex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertex" ):
                listener.exitVertex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVertex" ):
                return visitor.visitVertex(self)
            else:
                return visitor.visitChildren(self)




    def vertex(self):

        localctx = reggieParser.VertexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vertex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.structuralid()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==reggieParser.T__3:
                self.state = 32
                self.match(reggieParser.T__3)
                self.state = 33
                self.labelfilter()


            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << reggieParser.T__4) | (1 << reggieParser.STAR_WILDCARD) | (1 << reggieParser.PLUS_WILDCARD))) != 0):
                self.state = 36
                self.structuralvertexpattern()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructuralvertexpatternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(reggieParser.INT, 0)

        def PLUS_WILDCARD(self):
            return self.getToken(reggieParser.PLUS_WILDCARD, 0)

        def STAR_WILDCARD(self):
            return self.getToken(reggieParser.STAR_WILDCARD, 0)

        def getRuleIndex(self):
            return reggieParser.RULE_structuralvertexpattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructuralvertexpattern" ):
                listener.enterStructuralvertexpattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructuralvertexpattern" ):
                listener.exitStructuralvertexpattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructuralvertexpattern" ):
                return visitor.visitStructuralvertexpattern(self)
            else:
                return visitor.visitChildren(self)




    def structuralvertexpattern(self):

        localctx = reggieParser.StructuralvertexpatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_structuralvertexpattern)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [reggieParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(reggieParser.T__4)
                self.state = 40
                self.match(reggieParser.INT)
                pass
            elif token in [reggieParser.PLUS_WILDCARD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(reggieParser.PLUS_WILDCARD)
                pass
            elif token in [reggieParser.STAR_WILDCARD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(reggieParser.STAR_WILDCARD)
                self.state = 43
                self.match(reggieParser.T__5)
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


    class StructuraledgepattherContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(reggieParser.INT, 0)

        def PLUS_WILDCARD(self):
            return self.getToken(reggieParser.PLUS_WILDCARD, 0)

        def STAR_WILDCARD(self):
            return self.getToken(reggieParser.STAR_WILDCARD, 0)

        def getRuleIndex(self):
            return reggieParser.RULE_structuraledgepatther

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructuraledgepatther" ):
                listener.enterStructuraledgepatther(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructuraledgepatther" ):
                listener.exitStructuraledgepatther(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructuraledgepatther" ):
                return visitor.visitStructuraledgepatther(self)
            else:
                return visitor.visitChildren(self)




    def structuraledgepatther(self):

        localctx = reggieParser.StructuraledgepattherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_structuraledgepatther)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [reggieParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(reggieParser.T__4)
                self.state = 47
                self.match(reggieParser.INT)
                pass
            elif token in [reggieParser.PLUS_WILDCARD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(reggieParser.PLUS_WILDCARD)
                pass
            elif token in [reggieParser.STAR_WILDCARD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(reggieParser.STAR_WILDCARD)
                self.state = 50
                self.match(reggieParser.T__5)
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


    class StructuralidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(reggieParser.ID, 0)

        def QUESTIONMARK_WILDCARD(self):
            return self.getToken(reggieParser.QUESTIONMARK_WILDCARD, 0)

        def getRuleIndex(self):
            return reggieParser.RULE_structuralid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructuralid" ):
                listener.enterStructuralid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructuralid" ):
                listener.exitStructuralid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructuralid" ):
                return visitor.visitStructuralid(self)
            else:
                return visitor.visitChildren(self)




    def structuralid(self):

        localctx = reggieParser.StructuralidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_structuralid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            _la = self._input.LA(1)
            if not(_la==reggieParser.ID or _la==reggieParser.QUESTIONMARK_WILDCARD):
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


    class LabelfilterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(reggieParser.ID)
            else:
                return self.getToken(reggieParser.ID, i)

        def getRuleIndex(self):
            return reggieParser.RULE_labelfilter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelfilter" ):
                listener.enterLabelfilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelfilter" ):
                listener.exitLabelfilter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelfilter" ):
                return visitor.visitLabelfilter(self)
            else:
                return visitor.visitChildren(self)




    def labelfilter(self):

        localctx = reggieParser.LabelfilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_labelfilter)
        self._la = 0 # Token type
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [reggieParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(reggieParser.ID)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==reggieParser.T__6:
                    self.state = 56
                    self.match(reggieParser.T__6)
                    self.state = 57
                    self.match(reggieParser.ID)
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [reggieParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(reggieParser.T__7)
                self.state = 64
                self.match(reggieParser.ID)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==reggieParser.T__6:
                    self.state = 65
                    self.match(reggieParser.T__6)
                    self.state = 66
                    self.match(reggieParser.ID)
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72
                self.match(reggieParser.T__8)
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


    class Vertex2vertexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertex(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reggieParser.VertexContext)
            else:
                return self.getTypedRuleContext(reggieParser.VertexContext,i)


        def edge(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(reggieParser.EdgeContext)
            else:
                return self.getTypedRuleContext(reggieParser.EdgeContext,i)


        def getRuleIndex(self):
            return reggieParser.RULE_vertex2vertex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertex2vertex" ):
                listener.enterVertex2vertex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertex2vertex" ):
                listener.exitVertex2vertex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVertex2vertex" ):
                return visitor.visitVertex2vertex(self)
            else:
                return visitor.visitChildren(self)




    def vertex2vertex(self):

        localctx = reggieParser.Vertex2vertexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vertex2vertex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.vertex()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==reggieParser.T__9 or _la==reggieParser.T__10:
                self.state = 76
                self.edge()
                self.state = 77
                self.vertex()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labelledarraw(self):
            return self.getTypedRuleContext(reggieParser.LabelledarrawContext,0)


        def getRuleIndex(self):
            return reggieParser.RULE_edge

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge" ):
                listener.enterEdge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge" ):
                listener.exitEdge(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdge" ):
                return visitor.visitEdge(self)
            else:
                return visitor.visitChildren(self)




    def edge(self):

        localctx = reggieParser.EdgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_edge)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [reggieParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(reggieParser.T__9)
                pass
            elif token in [reggieParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.labelledarraw()
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


    class LabelledarrawContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edgelabel(self):
            return self.getTypedRuleContext(reggieParser.EdgelabelContext,0)


        def getRuleIndex(self):
            return reggieParser.RULE_labelledarraw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelledarraw" ):
                listener.enterLabelledarraw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelledarraw" ):
                listener.exitLabelledarraw(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelledarraw" ):
                return visitor.visitLabelledarraw(self)
            else:
                return visitor.visitChildren(self)




    def labelledarraw(self):

        localctx = reggieParser.LabelledarrawContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_labelledarraw)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(reggieParser.T__10)
            self.state = 89
            self.match(reggieParser.T__7)
            self.state = 90
            self.edgelabel()
            self.state = 91
            self.match(reggieParser.T__8)
            self.state = 92
            self.match(reggieParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgelabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(reggieParser.ID, 0)

        def getRuleIndex(self):
            return reggieParser.RULE_edgelabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdgelabel" ):
                listener.enterEdgelabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdgelabel" ):
                listener.exitEdgelabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdgelabel" ):
                return visitor.visitEdgelabel(self)
            else:
                return visitor.visitChildren(self)




    def edgelabel(self):

        localctx = reggieParser.EdgelabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_edgelabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(reggieParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





