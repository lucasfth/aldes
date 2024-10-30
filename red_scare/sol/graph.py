# Code lent from GeeksForGeeks: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
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
        # print(f"cur_node: {cur_node}\nreds: {reds}\nvisited: {visited}\nwasRed: {wasRed}")
        isRed = True if reds[cur_node] else False

        if isRed == wasRed: # Two nodes of same colors in a row
            # print(f"\t{cur_node} was illegal")
            return
        
        if cur_node in visited:
            # print(f"\t{cur_node} was visited")
            return
        
        visited.add(cur_node)

        for y in range(self.V):
            if self.graph[cur_node][y] > 0:
                # print(f"Try {y}")
                self.alt_rec(y, reds, visited, isRed)

        

    def alt_dfs(self, src, reds):

        visited = set()
        # visited.add(src)

        # isRed = False if reds[src] else True
        # print("---")
        # print(f"src: {src}\nreds: {reds}\nvisited: {visited}\nisRed: {isRed}")
        # print("---")

        # missing = {src}

        # for x in range(self.V):
        # print(f"------------ Checking {src} --------------")
        isRed = False if reds[src] else True
        self.alt_rec(src, reds, visited, isRed)
        # print(f"------------ Done with {src} --------------")

        return visited
        
        # for x in range(self.V):
        #     for y in range(self.V):
        #         if self.graph[x][y] >= 0:
        #             if y in reds and not isRed:
        #                 visited.add(y)
        #                 res.add(self.alt_rec(self, y, reds, visited, isRed))
        #             elif y not in reds and isRed:
        #                 visited.add(y)

    def BFS(self, s, t, parent):
 
        # Mark all the vertices as not visited
        visited = {s}
 
        # Create a queue for BFS
        queue = deque([s])
 
         # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.popleft()
 
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for v in self.adj_list[u]:
                if v not in visited and self.capacity[u][v] > 0:
                      # If we find a connection to the sink node, 
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
 
        # We didn't reach sink in BFS starting 
        # from source, so return false
        return False