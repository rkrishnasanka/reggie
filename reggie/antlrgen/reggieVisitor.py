# Generated from /Users/krishna/CIDAR/reggie/reggie.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .reggieParser import reggieParser
else:
    from reggieParser import reggieParser

# This class defines a complete generic visitor for a parse tree produced by reggieParser.

class reggieVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by reggieParser#reggie.
    def visitReggie(self, ctx:reggieParser.ReggieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reggieParser#vertex.
    def visitVertex(self, ctx:reggieParser.VertexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reggieParser#structuralvertexpattern.
    def visitStructuralvertexpattern(self, ctx:reggieParser.StructuralvertexpatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reggieParser#structuraledgepatther.
    def visitStructuraledgepatther(self, ctx:reggieParser.StructuraledgepattherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reggieParser#structuralid.
    def visitStructuralid(self, ctx:reggieParser.StructuralidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reggieParser#labelfilter.
    def visitLabelfilter(self, ctx:reggieParser.LabelfilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reggieParser#vertex2vertex.
    def visitVertex2vertex(self, ctx:reggieParser.Vertex2vertexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reggieParser#edge.
    def visitEdge(self, ctx:reggieParser.EdgeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reggieParser#labelledarraw.
    def visitLabelledarraw(self, ctx:reggieParser.LabelledarrawContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by reggieParser#edgelabel.
    def visitEdgelabel(self, ctx:reggieParser.EdgelabelContext):
        return self.visitChildren(ctx)



del reggieParser