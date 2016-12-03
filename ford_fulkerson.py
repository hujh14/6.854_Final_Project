from image_graph import *
from node import *
from edge import *

class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
        self.nodes = set()
 
    def convertImageGraph(self, imageGraph):
        nodes = imageGraph.getNodes()
        for node in nodes:
            self.add_vertex(node)
            
        
    def add_vertex(self, node):
        for edge in node.getOutgoingEdges():
            redge = Edge(edge.getSink(), edge.getSource(), 0)  
            edge.redge = redge
            redge.redge = edge
            u = edge.getSource()
            v = edge.getSink()
            if not(self.adj.has_key(u)):
                self.adj[u] = []
            if not(self.adj.has_key(v)):
                self.adj[v] = []
            self.adj[u].append(edge)
            self.adj[v].append(redge)
            self.flow[edge] = 0
            self.flow[redge] = 0
        self.nodes.add(node)
        
    def get_edges(self, node):
        return self.adj[node]

### TO ADD EDGES, first use node.addNeighbor() functions then add_vertex to FlowNetwork
### TODO: currently, node neighbors and flownetwork[node] neighbors not synched
#    def add_edge(self, u, v, w):
#        if u == v:
#            raise ValueError("u == v")
#        edge = Edge(u,v,w)
#        redge = Edge(v,u,0)
#        edge.redge = redge
#        redge.redge = edge
#        self.adj[u].append(edge)
#        self.adj[v].append(redge)
#        self.flow[edge] = 0
#        self.flow[redge] = 0
 
 
    def find_DFS_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.getCapacity() - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_DFS_path( edge.getSink(), sink, path + [edge]) 
                if result != None:
                    return result

    def find_BFS_path(self, source, sink): 
    #assumes unit distances, no sorting of queue
        visited = {}
        parent = {}
        for node in self.nodes:
            visited[node] = False
        queue = []
        queue.append(source)
        visited[source] = True
        
        while queue:
            u = queue.pop(0)
            if u == sink:
                return self.make_BFS_Path(parent, source, sink)
            for e in self.get_edges(source):
                residual = e.getCapacity() - self.flow[e]
                if not(visited[e.getSink()]) and  residual > 0:
                    queue.append(e.getSink())
                    visited[e.getSink()] = True
                    parent[e.getSink()] = e.getSource()
        return None
        
    def make_BFS_Path(self, parent, source, sink):
        reversePath = [sink]
        current = sink
        while not(current == source):
            current = parent[current]
            reversePath.append(current)
        path = reversePath.reverse()
        return path
 
    def max_flow(self, source, sink):
        path = self.find_BFS_path(source, sink)
        while path != None:
            residuals = [edge.getCapacity() - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_BFS_path(source, sink)
        return sum(self.flow[edge] for edge in self.get_edges(source))

    def get_min_cut(self):
        #TODO
        return None
    
color = (5,5,5)

s = Node((0,0), color)
n1 = Node((0,1), color)
n2 = Node((0,2), color)
n3 = Node((0,3), color)
n4 = Node((0,4), color)
t = Node((0,100), color)

s.addNeighborWithWeight(n1, 2)
s.addNeighborWithWeight(n2, 3)
n1.addNeighborWithWeight(n3, 1)
n2.addNeighborWithWeight(n3, 4)
n3.addNeighborWithWeight(t, 6)
n4.addNeighborWithWeight(t, 4)

g = FlowNetwork()
g.add_vertex(s)
g.add_vertex(n1)
g.add_vertex(n2)
g.add_vertex(n3)
g.add_vertex(t)

print g.max_flow(s,t)