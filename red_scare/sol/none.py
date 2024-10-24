"""
Discussed solution:
Use BFS (or another shortest path algorithm) to find a path without any red nodes.
Potentially you can remove the red nodes from the graph before solving,
but it may become problematic if we want to give the program a finished graph object.

Return:
Length of the shortest path without any red nodes.
"""

from dijsktra import Graph
import sys

def load_graph_from_file(file):
    names = {}
    reds = []
    
    with open(file, 'r') as f:
        n, m, r = map(int, f.readline().split())
        g = Graph(n)
        reds = [False for _ in range(n)] # constant time lookup
        s, t = f.readline().split()
        for i in range(n):
            inp = f.readline().split()
            if (len(inp) == 2):
                reds[i] = True
            names[inp[0]] = i
        
        for i in range(m):
            u, x, v = f.readline().split()
            w = -1 if reds[names[v]] else 1
            if x == '--':
                g.add_undirected_edge(names[u], names[v], w)
            else:
                g.add_directed_edge(names[u], names[v], w)
                
        return g, names[s], names[t]

def run(file):
    graph, s, t = load_graph_from_file(file)
    # graph.printGraph()
    graph.dijkstra(s)
    
    res = graph.distance(t)

    print(res)

run("../data/G-ex.txt")
 