source s
sink t

connect source to all pixels with weight
t-links

connect sink to all pixels with weight
t-links

only one of each?
all of them with probability?


connect pixels to each other with weight intensity
n-links


define graph:

adjacency matrix with weights

dictionary of 
[node: (neighbor node, weight), (neighbor node, weight)]

Node:
    pixel coordinate
    

Edge class:
    two nodes
    
    
graph:
    bunch of nodes (set list)
    bunch of edges (set list)
    
node:
    coordinates of pixel
    color of pixel
    intensity of pixel
    list of neighbor nodes
    source/sink
    
edge:
    node1
    node2