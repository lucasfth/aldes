"""
Discussed solution:
You probably have to brute force this one.
Thus not solving the assignment.

Return:
The maximum amount of nodes you can visit in a path from s to t.
"""

# Inspiration taken from: https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/

from collections import defaultdict
from os import path
from sys import setrecursionlimit
import networkx as nx
import matplotlib.pyplot as plt

setrecursionlimit(100000)


def load_file(file_name):
    with open(file_name, "r") as file:
        n, m, r = map(int, file.readline().split())
        graph = defaultdict(dict)
        reds = set()
        s, t = file.readline().split()
        for _ in range(n):
            input = file.readline().split()
            v = input[0]
            if len(input) == 2:
                reds.add(v)
        for i in range(m):
            a, x, b = file.readline().split()
            if x == "--":
                # Graph is undirected, which we cannot solve for.
                return None
            w = 1 if b in reds else 0
            graph[a][b] = w
        return n, graph, reds, s, t


def topological_sort(v, graph, stack, visited):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            topological_sort(u, graph, stack, visited)
    stack.append(v)


def solve(file_name):
    parsed = load_file(file_name)
    if parsed is None:
        print(f"Cannot solve Many for undirected graph: {path.basename(file_name)}")
        return
    n, graph, reds, s, t = parsed
    print(graph)
    stack = []
    visited = defaultdict(lambda: False)
    dist = defaultdict(lambda: float("-inf"))
    dist[s] = 0
    topological_sort(s, graph, stack, visited)
    while len(stack) > 0:
        v = stack.pop()
        for u, w in graph[v].items():
            dist[u] = max(dist[u], dist[v] + w)
    for v, d in dist.items():
        print(f"distance to {v}: {d}")
    result = dist[t] + 1 if s in reds else dist[t]
    print(f"distance to target: {result}")


def add_verts_and_edges(v, graph, reds, verts, edges, visited):
    visited[v] = True
    verts.append(v)
    for u in graph[v]:
        edges.append((v, u))
        if not visited[u]:
            add_verts_and_edges(u, graph, reds, verts, edges, visited)


def visualize(file_name):
    n, graph, reds, s, t = load_file(file_name)
    print(f"start: {s}, target: {t}")
    verts = []
    edges = []
    visited = defaultdict(lambda: False)
    add_verts_and_edges(s, graph, reds, verts, edges, visited)
    G = nx.DiGraph()
    G.add_nodes_from(verts)
    G.add_edges_from(edges)
    colors = ["#f00" if v in reds else "#999" for v in verts]
    nx.draw(G, with_labels=True, font_weight="bold", node_color=colors)
    plt.show()


file_name = "../data/increase-n8-1.txt"
solve(file_name)
visualize(file_name)
