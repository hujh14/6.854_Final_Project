from node import *

class Edge:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        # self.weight = self.computeWeight(n1,n2)
        self.cap = self.computeCapacity(n1,n2)

    def computeCapacity(self,n1,n2):
        return 1