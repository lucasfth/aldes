"""
Solution:
Maxflow
1. Create a new graph with 2*n+2 nodes, where n is the number of nodes in the original graph.
2. For each node s, create two nodes s_in and s_out with an edge inbetween of capacity 1. (Ensuring we only use each node once for a simple path)
3. For all edges (u, v) loaded in the file, the edge should go from u_out to v_in with capacity 1.
4. Save this graph as the "original graph".
5. For each red node r in R, do the following for source s and target t on a copy of the original graph:
    1. Run maxflow from r_out to s_out and save the graph from this run
    2. On the same graph, run maxflow from r_out to t_out
    3. If both runs return a flow of 1, return True
    4. Otherwise continue to the next red node
6. If no red node has a path to both s and t, return False

Note:
Due to step 2, we will have a graph of size 2*n ^ 2.
This is handled when loading the graph by having idx i as the node i_in and idx i+n as the node i_out.

Return:
True if a path from s to t includes a red node, False otherwise.
"""

import time
from graph import Graph

class some2():
    def load_graph_from_file(self, file):
        names = {}
        reds = []

        with open(file, 'r') as f:
            n, m, r = map(int, f.readline().split())
            g = Graph(n*2, 0)
            reds = [False for _ in range(n)]  # constant time lookup
            s, t = f.readline().split()
            for i in range(n):
                inp = f.readline().split()
                if (len(inp) == 2):
                    reds[i] = True
                names[inp[0]] = i
                
                g.add_directed_edge(i, i + n, 1)

            for i in range(m):
                u, x, v = f.readline().split()
                if x == '--':
                    g.add_directed_edge(names[u] + n, names[v], 1)
                    g.add_directed_edge(names[v] + n, names[u], 1)
                    
                else:
                    return False
                    # raise NotImplementedError("Cannot handle directed edges")
                    # g.add_directed_edge(names[u], names[v], 1)

            return g, names[s], names[t], reds, n


    def run(self, file):
        graph, s, t, r, n = self.load_graph_from_file(file)
        
        if not graph:
            print("  some2: Cannot handle directed edges")
            return

        for i in range(len(r)):
            if r[i]:
                g = graph.clone()
                res = g.FordFulkerson(i + n, s + n)
                # print(f"  {i} to source: {res}")
                if res == 1:
                    res = g.FordFulkerson(i + n, t + n)
                    # print(f"  {i} to target: {res}")
                    if res == 1:
                        print("  some2: True")
                        return

        print("  some2: False")

if __name__ == "__main__":
    start = time.time()
    some2().run("../data/G-ex.txt")
    print("  Time elapsed:", time.time() - start)
    