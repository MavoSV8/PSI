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


def bfs(graph, root):
    all_paths = []
    distances = []
    q = []
    path = [root]
    q.append(path)

    while q:
        path = q.pop(0)
        if len(path) == len(graph):
            temp_path = path.copy()
            temp_path.append(root)
            dist = calc_distance(temp_path)
            all_paths.append(temp_path)
            distances.append(dist)

        # for i in path:
        #     print(i, end="")
        # print()
        node = path[0]

        for neighbour in graph[node]:
            if neighbour not in path:
                newpath = path.copy()
                newpath.append(neighbour)
                q.append(newpath)
    return all_paths, distances


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
all_results, dists = bfs(cities, city_A)
end = datetime.datetime.now()
run_time = (end - start).total_seconds()*1000

print("=============result - BFS===============")
for i in range(len(all_results)):
    print("Path: ", end="")
    print(*all_results[i], end=" ")
    print("Distance: ", end="")
    print(dists[i], end="")
    print()
print(min(dists))
print("{0:.5f}ms".format(run_time))
