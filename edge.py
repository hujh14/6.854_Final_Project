from node import *

class Edge:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.w = self.computeWeight(n1,n2)

    def computeWeight(self,n1,n2):
        return 1