from edge import *

class Node:
    def __init__(self, loc, color):
        self.x = loc[0]
        self.y = loc[1]
        self.color = color

        self.neighbors = set()
        self.edges = set()

    def addNeighbors(self, nodes):
        for node in nodes:
            self.neighbors.add(node)
            edge = Edge(self, node)
            self.edges.add(edge)