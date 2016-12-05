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
        for node in graph.outgoingEdges.keys():
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
        
    def get_edges(self, node):
        return self.adj[node]
 
    def find_DFS_path(self, source, sink, path):
        print len(path)
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.getCapacity() - self.flow[edge]
            if residual > 0:
                visited = False
                for e in path:
                    if edge.v == e.v:
                        visited = True
                        break
                if not visited:
                    result = self.find_DFS_path( edge.getSink(), sink, path + [edge]) 
                    if result != None:
                        return result
        return None

    def find_BFS_path(self, source, sink, inp_path): 
    #assumes unit distances, no sorting of queue
        queue = [(source, inp_path)]
        
        while len(queue) > 0:
            (vertex, path) = queue.pop(0)
            for e in self.get_edges(vertex):
                residual = e.getCapacity() - self.flow[e]
                if residual > 0:
                    visited = False
                    for edge in path:
                        if edge.v == e.v:
                            visited = True
                            break
                    if not visited:
                        if e.v == sink:
                            return path + [e]
                        else:
                            queue.append((e.v, path + [e]))
        return None
 
    def max_flow(self, source, sink, algorithm, verbose):
        if algorithm == 'bfs':
            path = self.find_BFS_path(source, sink, [])
        elif algorithm == 'dfs':
            path = self.find_DFS_path(source, sink, [])
            
        counter = Counter()
        while path != None:
            residuals = [edge.getCapacity() - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
                
            if algorithm == 'bfs': #must be better way to not repeat this...
                path = self.find_BFS_path(source, sink, [])
            elif algorithm == 'dfs':
                path = self.find_DFS_path(source, sink, [])
            counter.inc()
            
            if verbose: 
                print "path length using BFS: " + str(len(path))
            
        if verbose:
            print "Using DFS took " + str(counter.getCount()) + " augmentations."
            
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

    def get_min_cut(self, graph, source, sink, algorithm, verbose):
        self.convertGraph(graph)
        self.max_flow(source, sink, algorithm, verbose)
        min_cut_edges = set()
        self.find_blocking_edge(source, sink, min_cut_edges, [])
        return min_cut_edges
        
    def clear_flow(self):
        for e in self.flow.keys():
            self.flow[e] = 0