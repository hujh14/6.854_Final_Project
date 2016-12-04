from ford_fulkerson import *

color = (5,5,5)

s = Node((0,0), color)
n1 = Node((0,1), color)
n2 = Node((0,2), color)
n3 = Node((0,3), color)
n4 = Node((0,4), color)
t = Node((0,100), color)

s.addNeighborWithWeight(n1, 3)
s.addNeighborWithWeight(n2, 20)
n1.addNeighborWithWeight(n3, 10)
n2.addNeighborWithWeight(n3, 5)
n2.addNeighborWithWeight(n4, 11)
n3.addNeighborWithWeight(t, 16)
n4.addNeighborWithWeight(t, 4)
n4.addNeighborWithWeight(n1, 8)


g = FlowNetwork()
g.add_vertex(s)
g.add_vertex(n1)
g.add_vertex(n2)
g.add_vertex(n3)
g.add_vertex(n4)
g.add_vertex(t)

cut = g.get_min_cut(s,t)
cut_val = 0

for edge in cut:
    cut_val += edge.getCapacity()    
    
print "Cut: " + str(cut_val)

for edge in cut:
    print "edge: " + str(edge) + " capacity: " + str(edge.getCapacity())