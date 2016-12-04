from image_graph import *
from node import *
from edge import *

class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
        self.nodes = set()

        # for node in self.g.outgoingEdges.keys():
        #     for edge in self.g.outgoingEdges[node]:
        #         u = edge.u
        #         v = edge.v

        #         redge = Edge(u, v, 0)  
        #         edge.redge = redge
        #         redge.redge = edge

        #         if not(self.g.outgoingEdges.has_key(u)):
        #             self.adj[u] = []
        #         if not(self.g.outgoingEdges.has_key(v)):
        #             self.adj[v] = []
        #         self.adj[u].append(edge)
        #         self.adj[v].append(redge)
        #         self.flow[edge] = 0
        #         self.flow[redge] = 0

 
    def convertGraph(self, graph):
        nodes = graph.getNodes()
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
        path = self.find_DFS_path(source, sink, [])
        while path != None:
            residuals = [edge.getCapacity() - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_DFS_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))
        
    def find_blocking_edge(self, source, sink, blocking_edges, path):
        if source==sink:
            return "S-T CUT FAILED"
        
        for edge in self.get_edges(source):
            residual = edge.getCapacity() - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_blocking_edge(edge.getSink(), sink, blocking_edges, path + [edge]) 
                if result != None:
                    return result
            elif residual == 0:
                blocking_edges.add(edge)                     

    def get_min_cut(self, graph, source, sink):
        self.convertGraph(graph)
        self.max_flow(source, sink)
        min_cut_edges = set()
        self.find_blocking_edge(source, sink, min_cut_edges, [])
        return min_cut_edges
        
    def clear_flow(self):
        for e in self.flow.keys():
            self.flow[e] = 0