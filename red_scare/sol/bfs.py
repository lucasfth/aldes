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
            