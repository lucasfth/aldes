"""
Discussed solution:
Use BFS or something similar with an extra constraint in terms of
how you can explore the graph.

Return:
Truth value of whether you can find a path from s to t with an alternating path.
"""

from graph import Graph

class alternate():
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
                u_idx, v_idx = names[u], names[v]
                if reds[u_idx] != reds[v_idx]:
                    if x == '--':
                        g.add_undirected_edge(names[u], names[v], 1)
                    else:
                        g.add_directed_edge(names[u], names[v], 1)

            return g, names[s], names[t], reds


    def run(self, file):
        graph, s, t, r = self.load_graph_from_file(file)
        res = graph.alt_dfs(s)

        print(f"  alternate: {t in res}")
