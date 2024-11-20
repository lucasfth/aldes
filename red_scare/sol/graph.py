# Code lent from GeeksForGeeks: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
from collections import deque
import sys


class Graph:

    def __init__(self, n, initial_value=-1):
        self.V = n
        self.graph = [[initial_value for column in range(n)] for row in range(n)]

    def clone(self):
        g = Graph(self.V)
        for i in range(self.V):
            for j in range(self.V):
                g.graph[i][j] = self.graph[i][j]
        return g

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

        dist = [sys.maxsize] * self.V  # shortest distance from start to all nodes
        dist[src] = 0  # distance from source to source
        sptSet = [False] * self.V  # added
        parents = [-1] * self.V  # Stores the vertices included in the shortest path
        parents[src] = -1  # There is no shortest path to yourself

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
            if x == -1:  # Skips over red nodes
                continue

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if (
                    self.graph[x][y] >= 0
                    and sptSet[y] == False
                    and dist[y] > dist[x] + self.graph[x][y]
                ):
                    parents[y] = x  # add the path
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

    def BFS(self, s, t):
        self.dist = [
            sys.maxsize
        ] * self.V  # Sets distance from s to all nodes to max int
        self.dist[s] = 0  # Distance from s to s is 0
        queue = deque([s])

        while queue:  # While queue is not empty
            u = queue.popleft()

            # Iterate over actual neighbors with non-negative edges
            for v in range(self.V):
                if self.graph[u][v] == -1:
                    continue  # Skip negative edges
                if self.dist[v] > self.dist[u] + 1:  # Only consider shorter paths
                    self.dist[v] = self.dist[u] + 1
                    queue.append(v)
                    if v == t:
                        return self.dist[t]  # Early exit if we reach the target

        return (
            self.dist[t] if self.dist[t] != sys.maxsize else -1
        )  # Return distance or -1 if unreachable

    def BFS_with_path(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    # If we find a connection to the sink node,
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        # We didn't reach sink in BFS starting
        # from source, so return false
        return False

    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.V)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS_with_path(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

