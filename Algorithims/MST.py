import heapq


def Prims(G):

    MST = []
    PrioQ = []
    num_vertices = len(G)
    starting_vertex = 0

    Visited = set([starting_vertex])

    for i in range(num_vertices):
        if G[starting_vertex][i] != 0:
            heapq.heappush(PrioQ, (G[starting_vertex][i], starting_vertex, i))

    while PrioQ:
        weight, v1, v2 = heapq.heappop(PrioQ)

        if v2 not in Visited:
            MST.append((v1, v2, weight))
            Visited.add(v2)

            for i in range(num_vertices):
                if (G[v2][i] != 0 and i not in Visited):
                    heapq.heappush(PrioQ, (G[v2][i], v2, i))

    return MST
