from image_graph import *
from node import *
from edge import *
from counter import *

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

# def find_BFS_path(self, source, sink, inp_path): 
#     #assumes unit distances, no sorting of queue
#         queue = [(source, inp_path)]
        
#         while len(queue) > 0:
#             (vertex, path) = queue.pop(0)
#             for e in self.get_edges(vertex):
#                 residual = e.getCapacity() - self.flow[e]
#                 if residual > 0:
#                     visited = False
#                     for edge in path:
#                         if edge.v == e.v:
#                             visited = True
#                             break
#                     if not visited:
#                         if e.v == sink:
#                             return path + [e]
#                         else:
#                             queue.append((e.v, path + [e]))
#         return None
 
    def max_flow(self, source, sink, algorithm, verbose):
        if verbose:
            print "Finding max flow..."
            
        if algorithm == 'bfs':
            path = self.find_BFS_path(source, sink, [])
        elif algorithm == 'dfs':
            path = self.find_DFS_path(source, sink, [], set())
            
        counter = Counter()
        path_number = 1
        
        while path != None:
            flow = 10**8
            min_edge = None
            for edge in path:
                residual = edge.getCapacity() - self.flow[edge]
                if residual < flow:
                    flow = residual
                    min_edge = edge
            if verbose:
                print path_number, flow, min_edge

            # residuals = [edge.getCapacity() - self.flow[edge] for edge in path]
            # flow = min(residuals)

            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
                
            if algorithm == 'bfs': #must be better way to not repeat this...
                path = self.find_BFS_path(source, sink, [])
            elif algorithm == 'dfs':
                path = self.find_DFS_path(source, sink, [],  set())
            counter.inc()
            
            if verbose and not path==None: 
                print "path length using " + algorithm + ": " + str(len(path))
            
        if verbose:
            print "Using DFS took " + str(counter.getCount()) + " augmentations."
            
        return sum(self.flow[edge] for edge in self.adj[source])
        
    def find_blocking_edge(self, source, sink, blocking_edges, path, verbose):
        if source==sink:
            return "S-T CUT FAILED"
        for edge in self.get_edges(source):
            path = self.find_DFS_path(source, sink, [], set())
            # path = self.find_BFS_path(source, sink, [])
            path_number += 1
        if verbose:
            print "Done finding blocking edges."
        return sum(self.flow[edge] for edge in self.adj[source])

    def find_S(self, source, S):
        for edge in self.adj[source]:
            residual = edge.getCapacity() - self.flow[edge]
            if residual > 10**-8 and edge.v not in S:
                S.add(edge.v)
                self.find_S(edge.v, S)

    def get_min_cut(self, graph, source, sink, algorithm, verbose):
        self.convertGraph(graph)
        self.max_flow(source, sink, algorithm, verbose)
        if verbose:
            print "Finding min cut..."
        min_cut_edges = set()
        S = set([source])
        self.find_S(source, S)
        for edge in graph.edges:
            if edge.u in S and edge.v not in S:
                min_cut_edges.add(edge)
        if verbose:
            print "S: ", len(S), " Mincut size:", len(min_cut_edges)
        return min_cut_edges
        
    def clear_flow(self):
        for e in self.flow.keys():
            self.flow[e] = 0