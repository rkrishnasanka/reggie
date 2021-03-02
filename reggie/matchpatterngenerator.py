from reggie.nodefilter import NodeFilter
from reggie.antlrgen.reggieParser import reggieParser
from reggie.antlrgen.reggieListener import reggieListener
import networkx as nx


class MatchPatternGenerator(reggieListener):
    def __init__(self) -> None:
        super(MatchPatternGenerator, self).__init__()

        self.structural_template = nx.DiGraph()
        self.semantic_template = dict()

    def enterVertex(self, ctx: reggieParser.VertexContext):
        vertex_id = ctx.structuralid

        label_filters = []
        if ctx.labelfilter is not None:
            for filter in ctx.labelfilter.label:
                label_filters.append(filter)
        # TODO - Put in the filter type information here
        semanitc_info = NodeFilter()
        if vertex_id == "?":
            raise NotImplementedError()

        else:
            self.structural_template.add_node(vertex_id)
            self.semantic_template[vertex_id] = NodeFilter()
