def get_neighbors(graph, vertex):
    return graph[vertex]

def dijkstra(start_node, graph):
    distance_dict = {vertex: float('infinity') for vertex in graph.keys()}
    distance_dict[start_node] = 0

    visited = set()
    queue = [(0, start_node)]

    while queue:
        queue.sort()
        distance, node = queue.pop(0)

        if node in visited:
            continue

        visited.add(node)

        for neighbor, neighbour_distance in get_neighbors(graph, node):
            total_distance = distance + neighbour_distance

            if total_distance < distance_dict[neighbor]:
                distance_dict[neighbor] = total_distance
                queue.append((total_distance, neighbor))

    return distance_dict

def dijkstra(start_node, graph):
    distance_dict = {vertex: float('infinity') for vertex in graph.keys()}
    distance_dict[start_node] = 0

    visited = set()
    queue = [(0, start_node)]

    while queue:
        queue.sort()
        distance, node = queue.pop(0)

        if node in visited:
            continue

        visited.add(node)

        for neighbor, neighbour_distance in get_neighbors(graph, node):
            total_distance = distance + neighbour_distance

            if total_distance < distance_dict[neighbor]:
                distance_dict[neighbor] = total_distance
                queue.append((total_distance, neighbor))

    return distance_dict


def GAMSRV(graph, client_list):
    result_list = []
    non_clients = list(set(graph.keys()) - set(client_list))
    for node in non_clients:
        helper = dijkstra(node, graph)
        res = -1
        for client in client_list:
            res = max(res, helper[client])
        result_list.append((res, node))
    return min(result_list)


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        N, M = map(int, file.readline().split())
        clients = file.readline().split()
        graph = {str(i): [] for i in range(1, N + 1)}
        for _ in range(M):
            start_node, end_node, latency = map(int, file.readline().split())
            graph[str(start_node)].append((str(end_node), latency))
            graph[str(end_node)].append((str(start_node), latency))

    return graph, clients


def write_output_file(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))


input_file_path = './results/gamsrv.in'
output_file_path = './results/gamsrv.out'

graph = {
    "A": [("H", 1), ("C", 3), ("J", 4), ("B", 8)],
    "B": [("A", 8), ("J", 9), ("E", 9)],
    "C": [("I", 2), ("A", 3)],
    "D": [("H", 20), ("F", 7)],
    "E": [("B", 9), ("G", 3), ("H", 11), ("F", 15)],
    "F": [("E", 15), ("G", 6), ("D", 7)],
    "G": [("J", 4), ("K", 8), ("E", 3), ("F", 6)],
    "H": [("E", 11), ("A", 1), ("D", 20)],
    "I": [("K", 17), ("J", 5), ("C", 2)],
    "J": [("E", 2), ("A", 4), ("B", 9), ("G", 4), ("I", 5), ("K", 1)],
    "K": [("J", 1), ("G", 8), ("I", 17)],
}

client_list = ["E", "B", "I", "J"]
clients = ["A", "C", "K", "E", "H"]
print(GAMSRV(graph, client_list))
print(GAMSRV(graph, clients))



