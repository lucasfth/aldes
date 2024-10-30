# Code lent from GeeksForGeeks: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys


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
    
    def numRedsInPath (self, terminal, parents, names, reds):
        path = []
        counter = 0
        current_vertex = terminal
        while current_vertex != -1:
            path.append(current_vertex)
            current_vertex = parents[current_vertex]

        for node in path:
            index = names.get(f"{node}")
            if reds[index] is True:
                counter += 1
        return counter

        
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
    def dijkstra(self, src, includeRed):

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
            if includeRed is False and x == -1: #Skips over red nodes
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



    #def dijkstraWithReds(self, src): # include red nodes

    #    dist = [sys.maxsize] * self.V
    #    dist[src] = 0
    #    sptSet = [False] * self.V
    #    
    #    #Added lines
    #    parents = [-1] * self.V # Stores the vertices included in the shortest path
    #    parents[src] = -1 #There is no shortest path to yourself
    #    

    #    for vertex in range(self.V): #Goes through every verte

    #        # Pick the minimum distance vertex from
    #        # the set of vertices not yet processed.
    #        # x is always equal to src in first iteration
    #        x = self.minDistance(dist, sptSet)


    #        nearest = -1
    #        shortest_distance = sys.maxsize
    #        for vertex_index in range(self.V):
    #            if sptSet[vertex] == False and dist[vertex_index] < shortest_distance:
    #                nearest = vertex_index
    #                shortest_distance = dist[vertex_index]

    #        # Put the minimum distance vertex in the
    #        # shortest path tree
    #        sptSet[x] = True
    #        
    #        """
    #        for vertex_index in range(self.V):
    #            edge_distance = self.graph[nearest][vertex_index]

    #            if edge_distance > 0 and shortest_distance + edge_distance < dist [vertex_index]:
    #                parent[vertex_index] = nearest
    #                shortest_distance[vertex_index] = shortest_distance +  edge_distance
    #        """
    #            

    #        # Update dist value of the adjacent vertices
    #        # of the picked vertex only if the current
    #        # distance is greater than new distance and
    #        # the vertex in not in the shortest path tree
    #        for y in range(self.V):
    #            if self.graph[x][y] >= 0 and sptSet[y] == False and \
    #                    dist[y] > dist[x] + self.graph[x][y]:
    #                parents[y] = x # add the path
    #                dist[y] = dist[x] + self.graph[x][y]

    #    self.dist = dist
    #    self.parents = parents