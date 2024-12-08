import heapq
import networkx as nx

def shortest_path(graph, source, to, weight = "Time"):
    distances = {node: float('inf') for node in graph.nodes}
    distances[source] = 0
    pri_queue = [(0, source)]
    predecessors = {}

    while pri_queue:
        curr_distance, curr_node = heapq.heappop(pri_queue)

        if curr_node == to:
            break

        for neighbour, edge_attrs in graph[curr_node].items():
            weight_value = edge_attrs.get(weight, 1)
            distance_through_curr = curr_distance + weight_value

            if distance_through_curr < distances[neighbour]:
                distances[neighbour] = distance_through_curr
                heapq.heappush(pri_queue, (distance_through_curr, neighbour))
                predecessors[neighbour] = curr_node

    path = []
    current = to
    while current in predecessors:
        path.insert(0, current)
        current = predecessors[current]
    if path:
        path.insert(0, source)

    return path, distances[to]
