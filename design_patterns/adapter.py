import math


class RoundPeg:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


class RoundHole:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, peg: RoundPeg):
        return self.get_radius() >= peg.get_radius()


class SquarePeg:
    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width


class SquarePegAdapter(RoundPeg):

    def __init__(self, peg: SquarePeg):
        self.peg = peg

    def get_radius(self):
        return self.peg.get_width() * math.sqrt(2) / 2
