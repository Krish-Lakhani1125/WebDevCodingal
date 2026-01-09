class Shapes:
    def __init__(self):
        self.__triangle = 3

    def sides(self):
        print("A Triangle has this number of sides: {}".format(self.__triangle))

    def setMaxPrice(self, sides):
        self.__triangle = sides

c = Shapes()
c.sides()


