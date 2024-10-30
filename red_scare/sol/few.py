"""
Discussed solution:
Use Djikstra's algorithm to find the shortest path from s to t.
Though the costs to move to black nodes are zero and to red nodes are one.

Return:
The minimum number of red nodes you can have in a path from s to t.
"""
from dijsktra import Graph
import sys

def load_graph_from_file(file):
    names = {}
    reds = []
    
    with open(file, 'r') as f:
        n, m, r = map(int, f.readline().split()) # m being number of edges
        g = Graph(n)
        reds = [False for _ in range(n)] # constant time lookup
        s, t = f.readline().split() 
        for i in range(n): # n being number of nodes
            inp = f.readline().split() # inp = <nodename> or <nodename *> for example 4 *
            if (len(inp) == 2): # if it has a star then set reds for that index to be true
                reds[i] = True
            names[inp[0]] = i # inp[0] is name of node 
        
        for i in range(m): # m = number edges
            u, x, v = f.readline().split() # u = node from, x = --, v = node to
            w = -1 if reds[names[v]] else 1 # 0, so it priorities black nodes ie. giving us the path with least amount of reds
            if x == '--': # 
                g.add_undirected_edge(names[u], names[v], w)
            else:
                g.add_directed_edge(names[u], names[v], w)
                
        return g, names[s], names[t], names, reds

def run(file):
    graph, s, t, names, reds = load_graph_from_file(file)
    graph.dijkstra(s, True)
    res = graph.numRedsInPath(t, graph.parents, names, reds)
    
    print(res)

run("../data/G-ex.txt")
 