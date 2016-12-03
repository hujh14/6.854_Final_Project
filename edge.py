from node import *

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def computeWeight(self):
        #computes weight of neighbor link for pixels
        self.w = 1
        return self.w
    
    def getSource(self):
        return self.u
        
    def getSink(self):
        return self.v
    
    def getCapacity(self):
        return self.w