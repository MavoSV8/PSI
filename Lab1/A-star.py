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
        for neighbour in graph[node]:
            if neighbour not in path:
                new_cost = g_score[node] + distance(node.x, neighbour.x, node.y, neighbour.y)
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
city_H = Node(7, 3, "H")
city_I = Node(3, 8, "I")
city_J = Node(6, 6, "J")
city_K = Node(9, 4, "K")
city_L = Node(8, 3, "L")
city_M = Node(12, 10, "M")
city_N = Node(1, 3, "N")
city_O = Node(9, 11, "O")
city_P = Node(10, 11, "P")
city_R = Node(11, 11, "R")
city_S = Node(5, 5, "S")
city_T = Node(9, 8, "T")
city_U = Node(3, 1, "U")

# 5 - cities
cities5 = {
    city_A: [city_B, city_C, city_D, city_E],
    city_B: [city_A, city_C, city_D, city_E],
    city_C: [city_B, city_A, city_D, city_E],
    city_D: [city_B, city_C, city_A, city_E],
    city_E: [city_B, city_C, city_D, city_A]
}
# 10 - cities
cities10 = {
    city_A: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J],
    city_B: [city_A, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J],
    city_C: [city_B, city_A, city_D, city_E, city_F, city_G, city_H, city_I, city_J],
    city_D: [city_B, city_C, city_A, city_E, city_F, city_G, city_H, city_I, city_J],
    city_E: [city_B, city_C, city_D, city_A, city_F, city_G, city_H, city_I, city_J],
    city_F: [city_B, city_C, city_D, city_E, city_A, city_G, city_H, city_I, city_J],
    city_G: [city_B, city_C, city_D, city_E, city_F, city_A, city_H, city_I, city_J],
    city_H: [city_B, city_C, city_D, city_E, city_F, city_G, city_A, city_I, city_J],
    city_I: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_A, city_J],
    city_J: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_A]
}

# 15 - cities
cities15 = {
    city_A: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O],
    city_B: [city_A, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O],
    city_C: [city_B, city_A, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O],
    city_D: [city_B, city_C, city_A, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O],
    city_E: [city_B, city_C, city_D, city_A, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O],
    city_F: [city_B, city_C, city_D, city_E, city_A, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O],
    city_G: [city_B, city_C, city_D, city_E, city_F, city_A, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O],
    city_H: [city_B, city_C, city_D, city_E, city_F, city_G, city_A, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O],
    city_I: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_A, city_J, city_K, city_L, city_M, city_N,
             city_O],
    city_J: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_A, city_K, city_L, city_M, city_N,
             city_O],
    city_K: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_A, city_L, city_M, city_N,
             city_O],
    city_L: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_A, city_M, city_N,
             city_O],
    city_M: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_A, city_N,
             city_O],
    city_N: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_A,
             city_O],
    city_O: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_A],
}

# 20 - cities
cities20 = {
    city_A: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_B: [city_A, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_C: [city_B, city_A, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_D: [city_B, city_C, city_A, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_E: [city_B, city_C, city_D, city_A, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_F: [city_B, city_C, city_D, city_E, city_A, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_G: [city_B, city_C, city_D, city_E, city_F, city_A, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_H: [city_B, city_C, city_D, city_E, city_F, city_G, city_A, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_I: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_A, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_J: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_A, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_K: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_A, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_L: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_A, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_M: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_A, city_N,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_N: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_A,
             city_O, city_P, city_R, city_S, city_T, city_U],
    city_O: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_A, city_P, city_R, city_S, city_T, city_U],
    city_P: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_A, city_R, city_S, city_T, city_U],
    city_R: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_A, city_S, city_T, city_U],
    city_S: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_A, city_T, city_U],
    city_T: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_A, city_U],
    city_U: [city_B, city_C, city_D, city_E, city_F, city_G, city_H, city_I, city_J, city_K, city_L, city_M, city_N,
             city_O, city_P, city_R, city_S, city_T, city_A]
}

start = datetime.datetime.now()
all_results = a_star(cities5, city_A)
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
