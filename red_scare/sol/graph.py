# Code lent from GeeksForGeeks: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
from collections import deque
import sys
sys.setrecursionlimit(10000)

class Graph():

    def __init__(self, n):
        self.V = n
        self.graph = [[-1 for column in range(n)]
                      for row in range(n)]

    def printSolution(self):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", self.dist[node])
            
    def printGraph(self):
        for i in range(self.V):
            print(self.graph[i])

    def distance(self, node):
        d = self.dist[node]
        if d == sys.maxsize:
            return -1
        return d

    def add_directed_edge(self, u, v, w):
        self.graph[u][v] = w
    
    def add_undirected_edge(self, u, v, w):
        self.add_directed_edge(u, v, w)
        self.add_directed_edge(v, u, w)    
    
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize
        min_index = -1

        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
            if x == -1:
                continue

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] >= 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.dist = dist

    def alt_rec(self, cur_node, reds, visited, wasRed):
        isRed = True if reds[cur_node] else False

        if isRed == wasRed: # Two nodes of same colors in a row
            return
        
        if cur_node in visited:
            return
        
        visited.add(cur_node)

        for y in range(self.V):
            if self.graph[cur_node][y] > 0:
                self.alt_rec(y, reds, visited, isRed)

        

    def alt_dfs(self, src, reds):

        visited = set()

        isRed = False if reds[src] else True
        self.alt_rec(src, reds, visited, isRed)

        return visited


    def BFS(self, s, t):
        self.dist = [sys.maxsize] * self.V # Sets distance from s to all nodex to max int
        self.dist[s] = 0 # Distance from s to s is 0
        queue = deque([s])

        while queue: # While queue is not empty
            u = queue.popleft()
            
            for v in range(self.V): # Iterate over all possible neighbors in the row
                if self.graph[u][v] >= 0 and self.dist[v] > self.dist[u] + 1: # Only consider non-negative edges
                    self.dist[v] = self.dist[u] + 1
                    queue.append(v) 
                    if v == t:
                        return self.dist[t] # Early exit if we reach the target

        return self.distance(t)