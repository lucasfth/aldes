"""
Discussed solution:
Use BFS, spanning tree, or another shortest path algorithm, from each red node to 
find paths to both the start and end nodes.
It will maybe be needed to do this from all red nodes.
We may be able to use dynamic programming to avoid redundant work - but we
can not see how to do this so far.

Another discussed solution:
Use a path algorithm from s to t and from t to s.
Here we should save the set of all the red nodes encountered when running.
After we can compare if these two sets include a common element.
OBS: Ensure that the path finding does not continue after finding either s or t.

Return:
True if a path from s to t includes a red node, False otherwise.
"""

import time
from graph import Graph

class some():
    def load_graph_from_file(self, file):
        names = {}
        reds = []

        with open(file, 'r') as f:
            n, m, r = map(int, f.readline().split())
            g = Graph(n)
            reds = [False for _ in range(n)]  # constant time lookup
            s, t = f.readline().split()
            for i in range(n):
                inp = f.readline().split()
                if (len(inp) == 2):
                    reds[i] = True
                names[inp[0]] = i

            for i in range(m):
                u, x, v = f.readline().split()
                if x == '--':
                    g.add_undirected_edge(names[u], names[v], 1)
                else:
                    g.add_directed_edge(names[u], names[v], 1)

            return g, names[s], names[t], reds


    def run(self, file):
        graph, s, t, r = self.load_graph_from_file(file)
        # DFS solution though I can not figure out the running time
        res = graph.some_dfs(s, t, r)

        print(f"  some: {res}")
