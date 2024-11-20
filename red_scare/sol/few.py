"""
Discussed solution:
Use Djikstra's algorithm to find the shortest path from s to t.
Though the costs to move to black nodes are zero and to red nodes are one.

Return:
The minimum number of red nodes you can have in a path from s to t.
"""
from graph import Graph
import sys

class few():
    def load_graph_from_file(self, file):
        names = {}
        reds = []
        startIndex = -1
        
        with open(file, 'r') as f:
            n, m, r = map(int, f.readline().split()) # m being number of edges
            g = Graph(n)
            reds = [False for _ in range(n)] # constant time lookup
            s, t = f.readline().split() 
            for i in range(n): # n being number of nodes
                inp = f.readline().split() # inp = <nodename> or <nodename *> for example 4 *
                if(inp[0] == s): startIndex = i
                if (len(inp) == 2): # if it has a star then set reds for that index to be true
                    reds[i] = True
                names[inp[0]] = i # inp[0] is name of node 
            
            for i in range(m): # m = number edges
                u, x, v = f.readline().split() # u = node from, x = --, v = node to
                # w = -1 if reds[names[v]] else 1 # 0, so it priorities black nodes ie. giving us the path with least amount of reds
                w_u = 1 if reds[names[u]] else 0
                w_v = 1 if reds[names[v]] else 0
                if i == startIndex and reds[startIndex]:
                    w_u = 1
                    w_v = 1

                if x == '--': # 
                    g.add_directed_edge(names[v], names[u], w_u) # if undirected add directions both ways
                    g.add_directed_edge(names[u], names[v], w_v)
                else:
                    g.add_directed_edge(names[u], names[v], w_v)
                    
            return g, names[s], names[t], names, reds

    def run(self, file):
        graph, s, t, _ , _ = self.load_graph_from_file(file)
        graph.dijkstra(s)
        res = graph.distance(t)
        print(f"  few: {res}")
 