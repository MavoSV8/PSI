import datetime
import math
import random

class City_node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.path = []
        self.total_estimation = 0
        self.cost = 0


def calculate_distance(node1: City_node, node2: City_node):
    return math.sqrt(pow(node1.x - node2.x, 2) + pow(node1.y - node2.y, 2))


def generate_cities(n: int):
    cities_list = []
    for i in range(0, n):
        cities_list.append(City_node("City_" + str(i + 1), random.randrange(0, 11), random.randrange(0, 11)))
    return cities_list


def a_star(root: City_node, graph: list):
    root_cpy = City_node(root.name, root.x, root.y)
    nodes_to_visit = [root_cpy]
    best_path = []
    best_cost = -1
    while len(nodes_to_visit) > 0:
        nodes_to_visit.sort(key=lambda x: x.total_estimation)
        current_node = nodes_to_visit.pop(0)  # 0
        current_node.path.append(current_node.name)
        if len(current_node.path) >= len(graph):
            if len(current_node.path) == len(graph) + 1:
                best_cost = current_node.cost
                best_path = current_node.path
                break
            new_node = City_node(root.name, root.x, root.y)
            new_node.cost = current_node.cost + calculate_distance(current_node, new_node)
            new_node.path = list(current_node.path)
            new_node.total_estimation = new_node.cost + calculate_distance(new_node, root)
            nodes_to_visit.append(new_node)
        else:
            temp_nodes_to_visit = []
            for child in graph:
                if (child.name not in current_node.path):
                    new_node = City_node(child.name, child.x, child.y)
                    new_node.cost = current_node.cost + calculate_distance(current_node, new_node)
                    new_node.path = list(current_node.path)
                    new_node.total_estimation = new_node.cost + calculate_distance(new_node, root)
                    temp_nodes_to_visit.append(new_node)
            nodes_to_visit = temp_nodes_to_visit + nodes_to_visit
    return [best_path, best_cost]

for i in range(5, 12):
    graph = generate_cities(i)

    start_time = datetime.datetime.now()
    a_star_res = a_star(graph[0], graph)
    end_time = datetime.datetime.now()
    a_execution_time = (end_time - start_time).total_seconds() * 1000

    print("for " + str(i) + " nodes:"
          + "\n\ta* time:     {0}ms".format(round(a_execution_time, 1)) + "\tcost:{0} path: {1}".format(
        round(a_star_res[1], 3), a_star_res[0]))