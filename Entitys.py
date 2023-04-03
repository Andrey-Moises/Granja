import random


class Arbusto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Oveja:
    def __init__(self, x, y, map):
        self.pastPostX = 0
        self.pastPostY = 0
        self.axisX = x
        self.axisY = y
        self.figure = "O"
        self.map = map
        self.knwlg = [[]]

    def move(self):
        self.pastPostX = self.axisX
        self.pastPostY = self.axisY
        self.axisX += 1
        self.axisY += 1


class Pastor:
    def __init__(self, x, y, map):
        pass

    def mover(self):
        pass


def existinmap(entity, axisx, axisy, map):
    map[axisx][axisy] = entity


def renewposition(axisx, axisy, map):
    map[axisx][axisy] = ' '


def printmap(map):
    for fila in map:
        for pos in fila:
            print(pos, end=" ")
        print()
