import math
import random

import numpy
import skfuzzy
from skfuzzy import control

g = 9.81
rules = []


def calculate_initial_velocity(a, d):
    v0 = math.sqrt((g * d) / math.sin(2 * math.radians(a)))
    return v0


def create_input():
    d = control.Antecedent(numpy.arange(1, 11, 1), 'distance')
    a = control.Antecedent(numpy.arange(1, 46, 1), 'angle')

    d.automf(3)
    a.automf(3)
    return d, a


def create_output():
    v0 = control.Consequent(numpy.arange(1, 55, 1), 'initial_velocity')
    v0['very low'] = skfuzzy.trimf(v0.universe, [1, 1, 11])
    v0['low'] = skfuzzy.trimf(v0.universe, [1, 11, 22])
    v0['medium'] = skfuzzy.trimf(v0.universe, [11, 22, 33])
    v0['high'] = skfuzzy.trimf(v0.universe, [22, 33, 44])
    v0['higher'] = skfuzzy.trimf(v0.universe, [33, 44, 55])
    v0['very high'] = skfuzzy.trimf(v0.universe, [44, 55, 55])
    return v0


def create_rules(d, a, v):
    rules_array = [control.Rule(d['poor'] & a['poor'], v['medium']),
                   control.Rule(d['poor'] & a['average'], v['low']),
                   control.Rule(d['poor'] & a['good'], v['very low']),
                   control.Rule(d['average'] & a['poor'], v['high']),
                   control.Rule(d['average'] & a['average'], v['medium']),
                   control.Rule(d['average'] & a['good'], v['low']),
                   control.Rule(d['good'] & a['poor'], v['higher']),
                   control.Rule(d['good'] & a['average'], v['medium']),
                   control.Rule(d['good'] & a['good'], v['low'])]

    return rules_array


distance, angle = create_input()
initial_velocity = create_output()

fuzz_v0_rules = control.ControlSystem(create_rules(distance, angle, initial_velocity))
fuzz_v0 = control.ControlSystemSimulation(fuzz_v0_rules)



print(calculate_initial_velocity(1, 10))

temp_list = []
for i in range(1, 11):
    print("================")
    for j in range(1, 46):
        fuzz_v0.input['distance'] = i
        fuzz_v0.input['angle'] = j
        fuzz_v0.compute()
        temp = calculate_initial_velocity(j, i)
        temp_list.append(temp)
        print("distance: {} angle: {} v0: {} fuzzy output: {}".format(i, j, temp, fuzz_v0.output.get("initial_velocity")))

