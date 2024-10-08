import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]  # Adjacency matrix

    # Function to print the shortest distance from source to all vertices
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(f"{node} \t {dist[node]}")

    # Utility function to find the vertex with the minimum distance value, from the set of vertices not yet processed
    def minDistance(self, dist, sptSet):
        min_val = sys.maxsize  # Initialize min value as infinity
        min_index = -1

        # Find the vertex with minimum distance value not yet included in sptSet
        for v in range(self.V):
            if dist[v] < min_val and not sptSet[v]:
                min_val = dist[v]
                min_index = v

        return min_index

    # Function that implements Dijkstra's single source shortest path algorithm using an adjacency matrix
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V  # Distance of all vertices from source, initialized to infinity
        dist[src] = 0  # Distance of source vertex from itself is always 0
        sptSet = [False] * self.V  # Boolean array to keep track of visited vertices

        for count in range(self.V):
            # Pick the minimum distance vertex from the set of vertices not yet processed
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True  # Mark the picked vertex as processed

            # Update the distance value of the adjacent vertices of the picked vertex
            for v in range(self.V):
                if (self.graph[u][v] > 0 and not sptSet[v] and 
                    dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        # Print the constructed distance array
        self.printSolution(dist)

# Driver code
g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

# Run Dijkstra's algorithm from vertex 0 (can change this to any source)
g.dijkstra(0)
