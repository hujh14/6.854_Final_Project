from ford_fulkerson import FlowNetwork
from image_graph import ImageGraph
import numpy as np

import numpy as np

class ImageSegmenter:

    def __init__(self, pixels, afn_func):
        height, width, colors = pixels.shape

        self.image_graph = ImageGraph(pixels, afn_func)

        self.solver = FlowNetwork()
        # self.solver = Blocking_Flows()

        self.segmented_image = np.zeros((height, width))

    def segment(self, algorithm, verbose):
        # string algorithm 'bfs' or 'dfs'
        # boolean verbose dictates print statements or na
        for i in xrange(1):
            if verbose:
                print "Segmenting... ", i
            # r_nodes = self.image_graph.randomNodes(2)
            # s = r_nodes[0]
            # t = r_nodes[1]
            s_loc = (2,2)
            t_loc = (16,16)
            s = self.image_graph.locToNodes[s_loc]
            t = self.image_graph.locToNodes[t_loc]
            min_cut = self.solver.get_min_cut(self.image_graph.graph, s, t, algorithm, verbose)

        for edge in min_cut:
            u = edge.u
            v = edge.v
            self.segmented_image[u.x][u.y] = 1.0
            self.segmented_image[v.x][v.y] = 1.0
        return self.segmented_image

