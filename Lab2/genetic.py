import random


def create_pop():
    pop = []
    for i in range(1, 128):
        pop.append(random.randrange(1, 128))
    return pop


def to_binary(pop):
    binary_pop = []
    for i in pop:
        binary_pop.append('{0:08b}'.format(i))
    return binary_pop


def to_decimal(pop):
    decimal_pop = []
    for i in pop:
        decimal_pop.append(int(i, 2))
    return decimal_pop


def cross(pop):
    chances = [0, 1]
    i = 0
    while i < len(pop) - 1:
        if random.choices(chances, weights=[.1, .9], k=1) == [1]:
            first_parent = pop[i]
            second_parent = pop[i + 1]
            first_child = first_parent[:int(len(first_parent) / 2)] + second_parent[int(len(second_parent) / 2):]
            second_child = second_parent[:int(len(second_parent) / 2)] + first_parent[int(len(first_parent) / 2):]
            pop[i] = first_child
            pop[i + 1] = second_child
        i += 2


def mutate(pop):
    i = 0
    chances = [0, 1]
    while i < len(pop):
        if random.choices(chances, weights=[.9, .1], k=1) == [1]:
            position = random.choices([1, 2, 3, 4, 5, 6, 7], k=1).pop(0)
            if pop[i][position] == '0':
                pop[i] = pop[i][:position] + "1" + pop[i][position + 1:]
            else:
                pop[i] = pop[i][:position] + "0" + pop[i][position + 1:]
        i += 1


def new_generation(current_pop):
    probabilities = []
    for i in current_pop:
        probabilities.append(2 * (pow(i, 2) + 1))

    new_pop = random.choices(current_pop, probabilities, k=len(current_pop))
    return new_pop


def find_best_specimens(start_pop):
    binary_pop = to_binary(start_pop)
    cross(binary_pop)
    mutate(binary_pop)

    for i in range(1, 500):
        start_pop = new_generation(to_decimal(binary_pop))
        binary_pop = to_binary(start_pop)
        cross(binary_pop)
        mutate(binary_pop)
    print("Final population:\n" + start_pop.__str__())


population = create_pop()
find_best_specimens(population)


