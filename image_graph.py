from node import *
from edge import *
from graph import *

class ImageGraph:
    def __init__(self, pixels):
        self.pixels = pixels
        self.height, self.width,self.colors = pixels.shape

        self.locToNodes = {}
        self.graph = Graph()
        
        self.buildGraph()

    def buildGraph(self):
        print "Building graph..."
        for i in xrange(self.height):
            for j in xrange(self.width):
                color = self.pixels[i][j]
                loc = (i,j)
                node = Node(loc, color)
                self.locToNodes[loc] = node
                self.graph.addNode(node)
        print "Added nodes."

        for i in xrange(self.height):
            for j in xrange(self.width):
                loc = (i,j)
                print loc
                node = self.locToNodes[loc]
                neighborCoords = self.getNeighborCoords(loc)
                for coord in neighborCoords:
                    edge = self.buildEdge(node, self.locToNodes[coord])
                    self.graph.addEdge(edge)

    def buildEdge(self, n1, n2):
        weight = 1 # affinity function
        return Edge(n1,n2,weight)

    def getNeighborCoords(self, loc):
        neighborCoords = []
        i,j = loc
        coords = [(i-1,j-1),(i,j-1),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
        for coord in coords:
            if not (coord[0] < 0 or coord[0] >= self.width or coord[1] < 0 or coord[1] >= self.height):
                neighborCoords.append(coord)
        return neighborCoords

    def randomNodes(self, n):
        return self.graph.randomNodes(n)