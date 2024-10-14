n_children, m_toys, p_category = map(int, input().split())

node_amount = n_children + m_toys + p_category + 2
src = node_amount - 1
sink = node_amount - 2

capacity = [[0] * node_amount for _ in range(node_amount)]

# map source to each child
for child in range(n_children):
    capacity[src][child] = 1

for child in range(n_children):
    data = list(map(int, input().split()))

    # map child to toy - elem 0 can be ignored as it is the number of toys
    for toy in data[1:]:
        capacity[child][n_children + toy - 1] = 1

toy_in_cat = set()

# iterate over categories
for category in range(p_category):
    data = list(map(int, input().split()))
    weight = data[-1]

    node_idx = n_children + m_toys + category

    # map toy to category
    for toy in data[1:-1]:
        capacity[n_children + toy - 1][node_idx] = 1
        toy_in_cat.add(toy)

    # map category to sink
    capacity[n_children + m_toys + category][sink] = weight

# map toy not in category to sink
for toy in range(m_toys):
    if toy+1 not in toy_in_cat:
        capacity[n_children + toy][sink] = 1

class Graph:
 
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self. ROW = len(graph)
        # self.COL = len(gr[0])
 
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
 
    def BFS(self, s, t, parent):
 
        # Mark all the vertices as not visited
        visited = [False]*(self.ROW)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
         # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                      # If we find a connection to the sink node, 
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
 
        # We didn't reach sink in BFS starting 
        # from source, so return false
        return False
             
     
    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow

g = Graph(capacity)

print(g.FordFulkerson(src, sink))
