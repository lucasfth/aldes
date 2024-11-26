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

class some():
    def load_graph_from_file(self, file):
        names = {}
        reds = []

        with open(file, 'r') as f:
            n, m, r = map(int, f.readline().split())
            reds = [False for _ in range(n)]  # constant time lookup
            s, t = f.readline().split()
            for i in range(n):
                inp = f.readline().split()
                if (len(inp) == 2):
                    reds[i] = True
                names[inp[0]] = i
                
            g = None
            directed = False

            for i in range(m):
                u, x, v = f.readline().split()
                directed = x != '--'
                if g is None:
                    g = Graph(n*2 if directed else n, 0)
                if directed:
                    g.add_directed_edge(names[u] + n, names[v], 1) # size is 2n for node splitting
                else:
                    g.add_undirected_edge(names[u], names[v], 1) # size is only n since we don't have node splitting

            if directed:
                for i in range(n):
                    g.add_directed_edge(i, i + n, 1)

            return g, names[s], names[t], reds, n, directed


    def run(self, file):
        try:
            graph, s, t, r, n, directed = self.load_graph_from_file(file)
            if graph == None:
                # No edges at all, only "True" if source and target is the same node and is red
                return str(s == t and r[s])

            if directed:
                foundPath = False

                for i in range(n):
                    if foundPath:
                        break
                    if r[i]:
                        flow, path1 = graph.FordFulkerson(s, i + n)
                        if flow == 1:
                            flow, _ = graph.FordFulkerson(i + n, t + n)
                            if flow == 1:
                                foundPath = True
                                break
                            graph.RevertPath(s, i + n, path1)
                return str(foundPath)
            else:
                if graph.IsCyclic():
                    # Check for cycles (we can even begin with a quick check based on the number of vertices and edges)
                    return("skip cyc g")
                else:
                    # If no cycles, we can solve the problem with path algorithm and checking if path contains a red node
                    path = [-1] * n
                    foundPathWithRedNode = graph.BFS_with_path(s, t, path) and graph.PathContainsRedNode(s, t, path, r)
                    return str(foundPathWithRedNode)
                    
        except Exception as e:
            return "Error"

if __name__ == "__main__":
    start = time.time()
    some().run("../data/acyclic.txt")
    print("  Time elapsed:", time.time() - start)