# Code lent from GeeksForGeeks: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
from collections import deque
import sys
sys.setrecursionlimit(100000)

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

        dist = [sys.maxsize] * self.V # shortest distance from start to all nodes 
        dist[src] = 0 # distance from source to source
        sptSet = [False] * self.V # added
        parents = [-1] * self.V # Stores the vertices included in the shortest path
        parents[src] = -1 #There is no shortest path to yourself

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
            if x == -1: #Skips over red nodes
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
                    parents[y] = x # add the path
                    dist[y] = dist[x] + self.graph[x][y]

        self.dist = dist
        self.parents = parents


    def alt_rec(self, cur_node, visited):
        if cur_node in visited:
            return
        
        visited.add(cur_node)

        for y in range(self.V):
            if self.graph[cur_node][y] > 0 and y not in visited:
                self.alt_rec(y, visited)
        

    def alt_dfs(self, src):
        visited = set()
        self.alt_rec(src, visited)
        return visited
    

    def some_rec(self, cur_node, reds, visited, sink, hasEncounteredRed):
        if cur_node == sink:
            return hasEncounteredRed
        
        if cur_node in visited:
            return False

        visited.add(cur_node)

        curHasEncounteredRed = hasEncounteredRed or reds[cur_node]

        for y in range(self.V):
            if self.graph[cur_node][y] > 0 and y not in visited:
                if self.some_rec(y, reds, visited, sink, curHasEncounteredRed):
                    return True

        return False
    

    def some_dfs(self, src, sink, reds):

        visited = set()

        hasEncounteredRed = reds[src]
        
        return self.some_rec(src, reds, visited, sink, hasEncounteredRed)


    def BFS(self, s, t):
        self.dist = [sys.maxsize] * self.V  # Sets distance from s to all nodes to max int
        self.dist[s] = 0  # Distance from s to s is 0
        queue = deque([s])

        while queue:  # While queue is not empty
            u = queue.popleft()

            # Iterate over actual neighbors with non-negative edges
            for v in range(self.V):
                if self.graph[u][v] == -1: continue  # Skip negative edges
                if self.dist[v] > self.dist[u] + 1:  # Only consider shorter paths
                    self.dist[v] = self.dist[u] + 1
                    queue.append(v)
                    if v == t:
                        return self.dist[t]  # Early exit if we reach the target

        return self.dist[t] if self.dist[t] != sys.maxsize else -1  # Return distance or -1 if unreachable
