from image_graph import *
from node import *

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
            redge = Edge(edge.getSink(), edge.getSouce(), reverse = True)  
            edge.redge = redge
            redge.redge = edge
            self.adj[edge.getSouce].append(edge)
            self.adj[edge.getSink].append(redge)
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
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_path( edge.sink, sink, path + [edge]) 
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
                residual = e.capacity - self.flow[e]
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
        path = self.find_DFS_path(source, sink, [])
        while path != None:
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))

    def get_min_cut(self):
        #TODO