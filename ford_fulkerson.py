class Ford_Fulkerson:
    def __init__(self, graph):
        self.graph = graph

        self.max_flow = Graph()
        self.residual = graph

    def BFS(self):
        # Run BFS on residual
        return flow_path # List of nodes

    def push_flow(self, flow_path):
        # Add flow to self.max_flow
        # Update self.residual


    def find_max_flow(self):
        while True:
            flow_path = self.BFS
            if flow_path == None:
                break
            push_flow(flow_path)

    def find_min_cut(self):
        self.find_max_flow()
