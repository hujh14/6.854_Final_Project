from node import *

class Graph:
    def __init__(self, pixels):
        self.pixels = pixels
        self.height, self.width,self.colors = pixels.shape

        self.nodes = {}
        self.createNodes()

    def createNodes(self):
        for i in xrange(self.height):
            for j in xrange(self.width):
                color = self.pixels[i][j]
                loc = (i,j)
                node = Node(loc, color)
                self.nodes[loc] = node

        for i in xrange(self.height):
            for j in xrange(self.width):
                loc = (i,j)
                node = self.nodes[loc]
                neighbors = self.findNeighbors(loc)
                node.addNeighbors(neighbors)

    def findNeighbors(self, loc):
        neighbors = []
        i,j = loc
        coords = [(i-1,j-1),(i,j-1),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
        for coord in coords:
            if not (coord[0] < 0 or coord[0] >= self.width or coord[1] < 0 or coord[1] >= self.height):
                neighbors.append(self.nodes[coord])
        return neighbors

