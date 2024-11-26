"""
Discussed solution:
We use a reduced longest path algorithm for Directed Acyclic Graphcs (DAGs).
Black nodes have incoming edges with weight 0, and reds have incoming edges of weight 1.
That way a path with most reds is prioritized because it is the longest path.
Undirected and cyclic graphs are ignored/skipped in the solution.

Return:
The maximum amount of nodes you can visit in a path from s to t.
"""

# Inspiration taken from: https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/

from collections import defaultdict


class many:
    def load_file(self, file_name):
        with open(file_name, "r") as file:
            n, m, r = map(int, file.readline().split())
            graph = defaultdict(dict)
            verts = []
            reds = set()
            s, t = file.readline().split()
            for _ in range(n):
                input = file.readline().split()
                v = input[0]
                verts.append(v)
                if len(input) == 2:
                    reds.add(v)
            for i in range(m):
                a, x, b = file.readline().split()
                if x == "--":
                    # Graph is undirected, which we cannot solve for.
                    return None
                w = 1 if b in reds else 0
                graph[a][b] = w
            return n, graph, verts, reds, s, t

    def dfs(self, v, graph, visited, rec_stack, stack):
        visited[v] = True
        rec_stack[v] = True
        for u in graph[v]:
            if not visited[u]:
                if self.dfs(u, graph, visited, rec_stack, stack):
                    return True
            elif rec_stack[u]:
                return True
        rec_stack[v] = False
        stack.append(v)
        return False

    def topological_sort(self, verts, graph):
        stack = []
        visited = defaultdict(lambda: False)
        rec_stack = defaultdict(lambda: False)
        for v in verts:
            if not visited[v]:
                if self.dfs(v, graph, visited, rec_stack, stack):
                    # Graph is cyclic, which we cannot solve for.
                    return None
        return stack

    def run(self, file_name):
        parsed = self.load_file(file_name)
        if parsed is None:
            return "skip undir g"
        n, graph, verts, reds, s, t = parsed
        dist = defaultdict(lambda: -1)
        dist[s] = 0
        stack = self.topological_sort(verts, graph)
        if stack is None:
            return "skip cyclic g"
        while len(stack) > 0:
            v = stack.pop()
            for u, w in graph[v].items():
                dist[u] = max(dist[u], dist[v] + w)
        result = dist[t] + 1 if s in reds else dist[t]
        return str(result)
