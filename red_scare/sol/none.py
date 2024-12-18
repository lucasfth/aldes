"""
Discussed solution:
Use BFS (or another shortest path algorithm) to find a path without any red nodes.
Potentially you can remove the red nodes from the graph before solving,
but it may become problematic if we want to give the program a finished graph object.

Return:
Length of the shortest path without any red nodes.
"""

from graph import Graph
import sys

class none():
    def load_graph_from_file(self, file):
        names = {}
        reds = []
        startIndex = -1
        
        with open(file, 'r') as f:
            n, m, r = map(int, f.readline().split())
            g = Graph(n)
            reds = [False for _ in range(n)] # constant time lookup
            s, t = f.readline().split()
            for i in range(n):
                inp = f.readline().split()
                if(inp[0] == s): startIndex = i
                if (len(inp) == 2):
                    reds[i] = True
                names[inp[0]] = i
            
            for i in range(m):
                u, x, v = f.readline().split()
                w = -1 if reds[names[v]] else 1
                if i == startIndex and reds[startIndex]:
                    w = -1
                if x == '--':
                    g.add_undirected_edge(names[u], names[v], w)
                else:
                    g.add_directed_edge(names[u], names[v], w)
                    
            return g, names[s], names[t]

    def run(self, file):
        graph, s, t = self.load_graph_from_file(file)
        # graph.printGraph()
        res = graph.BFS(s, t)
        
        res = graph.distance(t)

        return str(res)

# run("../data/G-ex.txt")
