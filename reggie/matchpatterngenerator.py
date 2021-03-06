from reggie.nodefilter import NodeFilter
from reggie.antlrgen.reggieParser import reggieParser
from reggie.antlrgen.reggieListener import reggieListener
import networkx as nx


class MatchPatternGenerator(reggieListener):
    def __init__(self) -> None:
        super(MatchPatternGenerator, self).__init__()

        self.structural_template = nx.DiGraph()
        self.semantic_template = dict()
        self._vertices_stack = []

    def enterVertex(self, ctx: reggieParser.VertexContext):
        vertex_id = ctx.structuralid().getText()

        self._vertices_stack.append(vertex_id)

        label_filters = []
        if ctx.labelfilter() is not None:
            label_filters = [label.getText() for label in ctx.labelfilter().label()]

        # TODO - Get the coloring filter
        coloring_labels = []
        if ctx.coloringfilter() is not None:
            coloring_labels = [s.getText() for s in ctx.coloringfilter().STRING()]
        constraints_tuples = []
        for i in range(0, len(coloring_labels), 2):
            constraints_tuples.append((coloring_labels[i], coloring_labels[i + 1]))

        # TODO - Put in the filter type information here
        semanitc_info = NodeFilter()

        if vertex_id == "?":
            raise NotImplementedError()

        else:
            self.structural_template.add_node(vertex_id)
            self.semantic_template[vertex_id] = NodeFilter(
                node_attributes_filter=label_filters,
                node_constraints=constraints_tuples,
            )

    def enterVertex2vertex(self, ctx: reggieParser.Vertex2vertexContext):
        # Clear out the recent vertex memory
        self._vertices_stack.clear()

    def exitVertex2vertex(self, ctx: reggieParser.Vertex2vertexContext):
        # TODO - Check to see if the vertex is present in the structural template first

        # Since the vertex is in the structural template
        for i in range(1, len(self._vertices_stack)):
            start = self._vertices_stack[i - 1]
            end = self._vertices_stack[i]
            # Generate the graph
            self.structural_template.add_edge(start, end)
