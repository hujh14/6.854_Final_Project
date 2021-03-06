from node import *
from edge import *
from graph import *

import numpy as np

class ImageGraph:
    def __init__(self, pixels, afn_func):
        self.pixels = pixels
        self.height, self.width,self.colors = pixels.shape

        self.locToNodes = {}
        self.graph = Graph()
        
        self.buildGraph(afn_func)

    def buildGraph(self, afn_func):
        print "Building graph..."
        num_of_nodes = 0
        for i in xrange(self.height):
            for j in xrange(self.width):
                color = self.pixels[i][j]
                loc = (i,j)
                node = Node(loc, color)
                self.locToNodes[loc] = node
                self.graph.addNode(node)
                num_of_nodes += 1
        print "Added nodes: ", num_of_nodes

        num_of_edges = 0
        for i in xrange(self.height):
            for j in xrange(self.width):
                loc = (i,j)
                node = self.locToNodes[loc]
                neighborCoords = self.getNeighborCoords(loc)
                for coord in neighborCoords:
                    edge = self.buildEdge(node, self.locToNodes[coord], afn_func)
                    self.graph.addEdge(edge)
                    num_of_edges += 1
        print "Added edges: ", num_of_edges 

    def buildEdge(self, n1, n2, afn_func):
        (c1, c2, c3) = n1.color
        (d1, d2, d3) = n2.color
        if afn_func == 'squared_distance':
            weight = 10 - ((c1-d1)**2 + (c2-d2)**2 + (c3-d3)**2)/(255**2*3.) * 10
            return Edge(n1,n2,weight)
        if afn_func == 'average_distance':
            average_distance = (np.abs(c1-d1) + np.abs(c2-d2) + np.abs(c3-d3))/3.
            weight = 10 - (average_distance)/255. * 10
            return Edge(n1,n2,weight)
        if afn_func == 'binary':
            test = 10 - ((c1-d1)**2 + (c2-d2)**2 + (c3-d3)**2)/(255**2*3.) * 10
            w = 1000
            if test > 2.5:
                w = 1000
            else: 
                w = 1
            return Edge(n1, n2, w)
            

    def getNeighborCoords(self, loc):
        neighborCoords = []
        i,j = loc
        # coords = [(i-1,j-1),(i,j-1),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
        coords = [(i+1,j), (i-1,j),(i,j+1),(i,j-1)]
        for coord in coords:
            if not (coord[0] < 0 or coord[0] >= self.width or coord[1] < 0 or coord[1] >= self.height):
                neighborCoords.append(coord)
        return neighborCoords

    def randomNodes(self, n):
        return self.graph.randomNodes(n)