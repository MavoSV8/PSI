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


def a_star(graph, root):
    heuristic = 0
    root.set_f_score(0)
    g_score = dict()
    g_score[root] = 0
    path = []
    q = [root]
    while q:
        q.sort(key=lambda x: x.f_score)
        node = q.pop(0)
        path.append(node)
        print(node)
        for neighbour in graph[node]:
            if neighbour not in path:
                new_cost = g_score[node] + distance(node.x, neighbour.x, node.y, neighbour.y)
                print(neighbour)
                print(new_cost)
                if neighbour not in g_score or new_cost < g_score[neighbour]:
                    g_score[neighbour] = new_cost
                    neighbour.set_f_score(new_cost + heuristic)
                    if neighbour not in q:
                        q.append(neighbour)
    path.append(root)
    return path


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
all_results = a_star(cities, city_A)
end = datetime.datetime.now()
run_time = (end - start).total_seconds() * 1000

final_distance = calc_distance(all_results)



print("=============result - A-star===============")
print("Path: ", end="")
print(*all_results)
print("Distance: ", end="")
print(final_distance)
print()
print("{0:.5f}ms".format(run_time))
