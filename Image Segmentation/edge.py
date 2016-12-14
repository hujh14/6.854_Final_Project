from node import *

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

        self.redge = None
    
    def getSource(self):
        return self.u
        
    def getSink(self):
        return self.v
    
    def getCapacity(self):
        return self.w

    def __str__(self):
        u = str(self.u)
        v = str(self.v)
        return str((u,v, self.w))
