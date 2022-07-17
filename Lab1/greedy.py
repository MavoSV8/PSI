import datetime

from Node import Node

import math


def calc_distance(path):
    result = 0
    for i in range(1, len(path)):
        result = result + distance(path[i - 1].x, path[i].x, path[i - 1].y, path[i].y)
    return result


def distance(x1, x2, y1, y2):
    result = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    return result


def greedy(graph, root):
    distances = []
    edge_nodes = []
    overall_distance = 0
    path = [root]
    q = [root]

    while q:
        node = q.pop(0)
        for neighbour in graph[node]:
            if neighbour not in path:
                distances.append(distance(node.x, neighbour.x, node.y, neighbour.y))
                edge_nodes.append(neighbour)
        if len(distances) != 0:
            temp_vertice = edge_nodes.pop(distances.index(min(distances)))
            overall_distance = overall_distance + min(distances)
            path.append(temp_vertice)
            q.append(temp_vertice)
            edge_nodes = []
            distances = []
    overall_distance = overall_distance + distance(path[len(path)-1].x, root.x, path[len(path)-1].y, root.y)
    path.append(root)
    return path, overall_distance


city_A = Node(0, 0, "A")
city_B = Node(2, 1, "B")
city_C = Node(2, 4, "C")
city_D = Node(5, 3, "D")
city_E = Node(1, 1, "E")
city_F = Node(3, 3, "F")
city_G = Node(4, 7, "G")

cities = {
    city_A: [city_B, city_C, city_D, city_E, city_F, city_G],
    city_B: [city_A, city_C, city_D, city_E, city_F, city_G],
    city_C: [city_B, city_A, city_D, city_E, city_F, city_G],
    city_D: [city_B, city_C, city_A, city_E, city_F, city_G],
    city_E: [city_B, city_C, city_D, city_A, city_F, city_G],
    city_F: [city_B, city_C, city_D, city_E, city_A, city_G],
    city_G: [city_B, city_C, city_D, city_E, city_F, city_A]
}

# cities = {
#     city_A: [city_B, city_C, city_D],
#     city_B: [city_A, city_C, city_D],
#     city_C: [city_B, city_A, city_D],
#     city_D: [city_B, city_C, city_A]
# }
start = datetime.datetime.now()
all_results, dist = greedy(cities, city_B)
end = datetime.datetime.now()
run_time = (end - start).total_seconds() * 1000

print("=============result - greedy===============")
print("Path: ", end="")
print(*all_results, end=" ")
print("Distance: ", end="")
print(dist, end="")
print()
print("{0:.5f}ms".format(run_time))
