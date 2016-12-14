from node import *

import random

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

        self.outgoingEdges = {}

    def addNode(self, node):
        self.nodes.add(node)

    def addEdge(self, edge):
        self.edges.add(edge)
        if edge.u in self.outgoingEdges.keys():
            self.outgoingEdges[edge.u].append(edge)
        else:
            self.outgoingEdges[edge.u] = [edge]

    def randomNodes(self, n):
        return random.sample(self.nodes, n)

    # def copy(self):
    #     output = Graph()
    #     for node in self.nodes:
    #         output.addNode(node)
    #     for e in self.edges:
    #         output.addEdge(e)
    #     return output