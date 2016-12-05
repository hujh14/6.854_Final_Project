from edge import *

class Node:
    def __init__(self, loc, color):
        self.x = loc[0]
        self.y = loc[1]
        self.color = color

        self.neighbors = set()
        self.edges = set()

    def addPixelNeighbors(self, nodes):
        # input nodes: list of neighbor nodes directed from self --> nodes
        for node in nodes:
            self.neighbors.add(node)
            edge = Edge(self, node, 0).computeWeight()
            self.edges.add(edge)

    def addNeighborWithWeight(self, node, w):
        self.neighbors.add(node)
        edge = Edge(self, node, w)
        self.edges.add(edge)
    
    # def getChildren(self):
    #     return self.neighbors
        
    # def getOutgoingEdges(self):
    #     return self.edges