# Generated from /Users/krishna/CIDAR/reggie/reggie.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("j\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\7\16I\n\16\f\16\16")
        buf.write("\16L\13\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\6\24Y\n\24\r\24\16\24Z\3\24\3\24\3\25\6\25")
        buf.write("`\n\25\r\25\16\25a\3\25\3\25\3\26\6\26g\n\26\r\26\16\26")
        buf.write("h\2\2\27\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\2\37\2!\20#\21%\22\'\23)\24+\25\3")
        buf.write("\2\7\5\2C\\aac|\6\2\62;C\\aac|\4\2\13\13\"\"\4\2\f\f\17")
        buf.write("\17\3\2\62;\2k\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2\5/\3\2\2\2\7")
        buf.write("\61\3\2\2\2\t\63\3\2\2\2\13\65\3\2\2\2\r\67\3\2\2\2\17")
        buf.write("9\3\2\2\2\21;\3\2\2\2\23=\3\2\2\2\25?\3\2\2\2\27B\3\2")
        buf.write("\2\2\31D\3\2\2\2\33F\3\2\2\2\35M\3\2\2\2\37O\3\2\2\2!")
        buf.write("Q\3\2\2\2#S\3\2\2\2%U\3\2\2\2\'X\3\2\2\2)_\3\2\2\2+f\3")
        buf.write("\2\2\2-.\7}\2\2.\4\3\2\2\2/\60\7.\2\2\60\6\3\2\2\2\61")
        buf.write("\62\7\177\2\2\62\b\3\2\2\2\63\64\7<\2\2\64\n\3\2\2\2\65")
        buf.write("\66\7]\2\2\66\f\3\2\2\2\678\7_\2\28\16\3\2\2\29:\7~\2")
        buf.write("\2:\20\3\2\2\2;<\7*\2\2<\22\3\2\2\2=>\7+\2\2>\24\3\2\2")
        buf.write("\2?@\7/\2\2@A\7@\2\2A\26\3\2\2\2BC\7/\2\2C\30\3\2\2\2")
        buf.write("DE\7@\2\2E\32\3\2\2\2FJ\t\2\2\2GI\t\3\2\2HG\3\2\2\2IL")
        buf.write("\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\34\3\2\2\2LJ\3\2\2\2MN\7")
        buf.write("/\2\2N\36\3\2\2\2OP\7@\2\2P \3\2\2\2QR\7,\2\2R\"\3\2\2")
        buf.write("\2ST\7-\2\2T$\3\2\2\2UV\7A\2\2V&\3\2\2\2WY\t\4\2\2XW\3")
        buf.write("\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\b\24")
        buf.write("\2\2](\3\2\2\2^`\t\5\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2")
        buf.write("ab\3\2\2\2bc\3\2\2\2cd\b\25\2\2d*\3\2\2\2eg\t\6\2\2fe")
        buf.write("\3\2\2\2gh\3\2\2\2hf\3\2\2\2hi\3\2\2\2i,\3\2\2\2\7\2J")
        buf.write("Zah\3\b\2\2")
        return buf.getvalue()


class reggieLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    ID = 13
    STAR_WILDCARD = 14
    PLUS_WILDCARD = 15
    QUESTIONMARK_WILDCARD = 16
    WS = 17
    NL = 18
    INT = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "','", "'}'", "':'", "'['", "']'", "'|'", "'('", "')'", 
            "'->'", "'-'", "'>'", "'*'", "'+'", "'?'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "STAR_WILDCARD", "PLUS_WILDCARD", "QUESTIONMARK_WILDCARD", 
            "WS", "NL", "INT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "ID", "ARROW_BASE", 
                  "ARROW_HEAD", "STAR_WILDCARD", "PLUS_WILDCARD", "QUESTIONMARK_WILDCARD", 
                  "WS", "NL", "INT" ]

    grammarFileName = "reggie.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


