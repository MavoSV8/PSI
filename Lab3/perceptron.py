import random
from matplotlib import pyplot

x1 = []
x2 = []
y1 = []
y2 = []
learning_rate = 0.1
bias = 1
weights = []
wholeSet = []


def generate_data(size):
    for i in range(size):
        x = round(random.uniform(-10, 10), 2)
        y = round(random.uniform(-10, 10), 2)
        if y > x:
            output = 1
        else:
            output = -1
        wholeSet.append([x, y, output])


def split_data_to_two_sets():
    half = len(wholeSet) / 2
    quarter = half / 2
    testLen = half + quarter

    train = wholeSet[int(testLen):]
    test = wholeSet[:int(quarter)]

    return train, test


def generate_weights(size):
    for i in range(size):
        weights.append(round(random.uniform(0, 10), 2))


def trainer(inp, b=bias):
    result = processor(inp)
    error = inp[2] - result
    weights[0] += error * inp[0] * learning_rate
    weights[1] += error * inp[1] * learning_rate
    b += error * learning_rate


def processor(inp):
    output = bias + weights[0] * inp[0] + weights[1] * inp[1]
    if output < 0:
        return -1
    else:
        return 1


def plot_points(x1, x2, y1, y2):
    pyplot.plot(x1, y1, marker="+", ls="")
    pyplot.plot(x2, y2, marker="*", ls="")
    pyplot.show()
    return 0


generate_data(1000)
trainingSet, testSet = split_data_to_two_sets()
generate_weights(2)
counter = 0
for test in testSet:
    if processor(test) == test[2]:
        x1.append(test[0])
        y1.append(test[1])
        counter += 1
    else:
        x2.append(test[0])
        y2.append(test[1])

plot_points(x1, x2, y1, y2)
print("Result before training: {}/{}".format(counter, len(testSet)))
for i in range(len(trainingSet)):
    trainer(trainingSet[i])
counter = 0
x1 = []
x2 = []
y1 = []
y2 = []
for test in testSet:
    check = processor(test)
    if check == test[2]:
        x1.append(test[0])
        y1.append(test[1])
        counter += 1
    else:
        x2.append(test[0])
        y2.append(test[1])


plot_points(x1, x2, y1, y2)
print("Result after training: {}/{}".format(counter, len(testSet)))
classification = (counter/len(testSet))*100
print("Classification: {}%".format(classification))
