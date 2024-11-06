from collections import deque, defaultdict

MAX_RES = 10**6 + 1

n = int(input())

src = n
sink = src + 1
next_node = sink + 1

capacity = defaultdict(lambda: defaultdict(int))
adj_list = defaultdict(list)

result_map = {}
edge_label = {}

for exp in range(n):
    a, b = map(int, input().split())
    op = [
        (a * b, f'{a} * {b} = {a*b}'),
        (a + b, f'{a} + {b} = {a+b}'),
        (a - b, f'{a} - {b} = {a-b}')
    ]
    prod = a * b
    sum = a + b
    diff = a - b

    capacity[src][exp] = 1
    adj_list[src].append(exp)
    adj_list[exp].append(src)

    for r, calc in op:
        if r not in result_map:
            result_map[r] = next_node
            next_node += 1
        
        res_node = result_map[r]

        # map exp to res_node
        capacity[exp][res_node] = 1
        adj_list[exp].append(res_node)
        adj_list[res_node].append(exp)

        # store calc between exp and res_node
        edge_label[(exp, res_node)] = calc

        # map res_node to sink
        capacity[res_node][sink] = 1
        adj_list[res_node].append(sink)
        adj_list[sink].append(res_node)


class Graph:
 
    def __init__(self, adj_list, capacity):
        self.adj_list = adj_list
        self.capacity = capacity
        # self.COL = len(gr[0])
 
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
 
    def BFS(self, s, t, parent):
 
        # Mark all the vertices as not visited
        visited = {s}
 
        # Create a queue for BFS
        queue = deque([s])
 
         # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.popleft()
 
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for v in self.adj_list[u]:
                if v not in visited and self.capacity[u][v] > 0:
                      # If we find a connection to the sink node, 
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
 
        # We didn't reach sink in BFS starting 
        # from source, so return false
        return False
             
     
    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        solution = {}
 
        # This array is filled by BFS and to store path
        parent = {}
 
        max_flow = 0 # There is no flow initially

        processed = set()
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.capacity[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v][u] += path_flow
                # if u < n and v >= sink + 1 and u not in processed:
                #     solution[u] = edge_label[(u, v)]
                #     processed.add(u)
                v = u

            parent = {}
 
        return max_flow

g = Graph(adj_list, capacity)

flow = g.FordFulkerson(src, sink)

# def print_solution(s):
#     for hash in s.keys():
#         print(s[hash])

if flow < n:
    print("impossible")
else:
    solution = [''] * n
    for exp in range(n):
        for res_node in adj_list[exp]:
            if res_node >= sink + 1 and capacity[exp][res_node] == 0:
                solution[exp] = edge_label[(exp, res_node)]
                break
    for eq in solution:
        print(eq)
