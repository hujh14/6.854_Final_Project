from image_graph import *
from node import *
from edge import *

class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
        self.nodes = set()
 
    def convertGraph(self, graph):
        for node in graph.nodes:
            self.nodes.add(node)
            for edge in graph.outgoingEdges[node]:
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
 
    def find_DFS_path(self, source, sink, path, visited):
        if source == sink:
            return path
        for edge in self.adj[source]:
            residual = edge.getCapacity() - self.flow[edge]
            if residual > 10**-8:
                if edge.v not in visited:
                    visited.add(edge.v)
                    result = self.find_DFS_path( edge.getSink(), sink, path + [edge], visited) 
                    if result != None:
                        return result
        return None

    # def find_BFS_path(self, source, sink): 
    # #assumes unit distances, no sorting of queue
    #     visited = {}
    #     parent = {}
    #     for node in self.nodes:
    #         visited[node] = False
    #     queue = []
    #     queue.append(source)
    #     visited[source] = True
        
    #     while queue:
    #         u = queue.pop(0)
    #         if u == sink:
    #             return self.make_BFS_Path(parent, source, sink)
    #         for e in self.adj[source]:
    #             residual = e.getCapacity() - self.flow[e]
    #             if not(visited[e.getSink()]) and  residual > 0:
    #                 queue.append(e.getSink())
    #                 visited[e.getSink()] = True
    #                 parent[e.getSink()] = e.getSource()
    #     return None
        
    # def make_BFS_Path(self, parent, source, sink):
    #     reversePath = [sink]
    #     current = sink
    #     while not(current == source):
    #         current = parent[current]
    #         reversePath.append(current)
    #     path = reversePath.reverse()
    #     return path
 
    def max_flow(self, source, sink):
        print "Finding max flow..."
        path = self.find_DFS_path(source, sink, [], set())
        path_number = 1
        # path = self.find_BFS_path(source, sink, [])
        while path != None:
            flow = 10**8
            min_edge = None
            for edge in path:
                residual = edge.getCapacity() - self.flow[edge]
                if residual < flow:
                    flow = residual
                    min_edge = edge
            print path_number, flow, min_edge

            # residuals = [edge.getCapacity() - self.flow[edge] for edge in path]
            # flow = min(residuals)

            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_DFS_path(source, sink, [], set())
            # path = self.find_BFS_path(source, sink, [])
            path_number += 1
        print "Done."
        return sum(self.flow[edge] for edge in self.adj[source])

    def find_S(self, source, S):
        for edge in self.adj[source]:
            residual = edge.getCapacity() - self.flow[edge]
            if residual > 10**-8 and edge.v not in S:
                S.add(edge.v)
                self.find_S(edge.v, S)


    def get_min_cut(self, graph, source, sink):
        self.convertGraph(graph)
        self.max_flow(source, sink)

        print "Finding min cut..."
        min_cut_edges = set()
        S = set([source])
        self.find_S(source, S)
        for edge in graph.edges:
            if edge.u in S and edge.v not in S:
                min_cut_edges.add(edge)
        print "S: ", len(S), " Mincut size:", len(min_cut_edges)
        return min_cut_edges
        
    def clear_flow(self):
        for e in self.flow.keys():
            self.flow[e] = 0