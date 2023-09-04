import abc


class Graphic(abc.ABC):
    @abc.abstractmethod
    def move(self, x, y):
        pass

    @abc.abstractmethod
    def draw(self):
        pass


class Dot(Graphic):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        pass  # drawing a dot on the screen


class Circle(Graphic):

    def move(self, x, y):
        self.x += x
        self.y += y

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pass  # draw a circle with (x,y) center and radius of 'radius'


class CompoundGraphic(Graphic):

    def __init__(self):
        self.children: list[Graphic] = []

    def add(self, child: Graphic):
        self.children.append(child)

    def remove(self, child: Graphic):
        self.children.remove(child)

    def move(self, x, y):
        for child in self.children:
            child.move(x, y)

    def draw(self):
        for child in self.children:
            child.draw()
