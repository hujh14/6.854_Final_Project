from ford_fulkerson import *
from graph import *

color = (5,5,5)

s = Node((0,0), color)
n1 = Node((0,1), color)
n2 = Node((0,2), color)
n3 = Node((0,3), color)
n4 = Node((0,4), color)
t = Node((0,100), color)

edges = [
Edge(s,n1,3),
Edge(s, n2, 20),
Edge(n1,n3, 10),
Edge(n2,n3, 5),
Edge(n2,n4, 11),
Edge(n3,t, 16),
Edge(n4, t, 4),
Edge(n4, n1, 8)
]

g = Graph()

g.addNode(s)
g.addNode(n1)
g.addNode(n2)
g.addNode(n3)
g.addNode(n4)
g.addNode(t)

for e in edges:
    g.addEdge(e)


fn = FlowNetwork()
fn2 = FlowNetwork()

fn.convertGraph(g)
print fn.max_flow(s,t)
cut = fn2.get_min_cut(g, s, t)

cut_val = 0

for edge in cut:
    cut_val += edge.getCapacity()    
    
print "Cut: " + str(cut_val)

for edge in cut:
    print "edge: " + str(edge) + " capacity: " + str(edge.getCapacity())