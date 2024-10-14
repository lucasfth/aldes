import networkx as nx

def print_shooter(g):
    g = sorted(g, key=lambda x: x[0])
    prev = 0
    for a, b in g:
        if a == prev:
            a, b = b, a
        prev = a

    for _, b in g:
        print(b)

n_players, n_pairs = map(int, input().split())

graph = nx.Graph()
graph.add_nodes_from(range(1, n_players+1))

for _ in range(n_pairs):
    a, b = map(int, input().split())
    graph.add_edge(a, b)

# print(graph.nodes)
# print(graph.edges)

try:
    res = nx.find_cycle(graph)
except nx.NetworkXNoCycle:
    res = []

if res:
    for a, b in res:
        graph.remove_edge(a, b)

if len(graph.edges) == 0:
    print_shooter(res)
    exit()

# print(graph.edges)

res += list(nx.max_weight_matching(graph, maxcardinality=True))

if len(res) != n_players:
    print("Impossible")
    exit()

print_shooter(res)
