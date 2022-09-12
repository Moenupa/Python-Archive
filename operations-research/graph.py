class Graph():
    def __init__(self, n_vertices) -> None:
        self.V = n_vertices
        self.graph = [[0 for column in range(n_vertices)] for row in range(n_vertices)]
        
    def genGraphFromEdges(self, edges):
        for edge in edges:
            self.graph[edge[0]][edge[1]] = edge[2]
            self.graph[edge[1]][edge[0]] = edge[2]
        # for edge in edges:
        #     self.graph[edge[0] - 1][edge[1] - 1] = edge[2]
        #     self.graph[edge[1] - 1][edge[0] - 1] = edge[2]
        
    def setGraph(self, graph):
        self.graph = graph