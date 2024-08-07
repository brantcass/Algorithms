def solve_tsp(G):
    n = len(G)
    path = [0]
    visited = [False] * n
    visited[0] = True

    while len(path) < n:
        current_node = path[-1]
        min_distance = float('inf')
        next_node = None

        for i in range(n):
            if not visited[i] and G[current_node][i] < min_distance:
                min_distance = G[current_node][i]
                next_node = i

        if next_node is None:
            for i in range(n):
                if not visited[i]:
                    next_node = i
                    break

        if next_node is None:
            break

        path.append(next_node)
        visited[next_node] = True

    if len(path) < n:
        return []

    path.append(0)
    return path
