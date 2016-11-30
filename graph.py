from node import *

class Graph:
    def __init__(self, source, sink, nodes, edges):
        self.source = source
        self.sink = sink

        # nodes is a list of Nodes
        # edges is a list of Edges
        self.nodes = set(nodes)
        self.edges = set(edges)

    def


