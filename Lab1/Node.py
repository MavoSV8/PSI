class Node:
    f_score = 99999999999999999999999
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return "{}".format(self.name)

    def set_f_score(self, f):
        self.f_score = f

    def get_f_score(self):
        return self.f_score

    def get_coordinates(self):
        return [self.x, self.y]

    # def set_coordinates(self, coordinates):
    #     self.coordinates = coordinates
