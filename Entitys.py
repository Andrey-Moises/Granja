import random as Rm

ENTITYS = ['B', 'S', '=', '0', 'O']


class Arbusto:
    def __init__(self):
        self.axisY = None
        self.axisX = None
        self.figure = 'B'

    def existinmap(self, map):
        map[self.axisX][self.axisY] = self.figure

    def spawn(self, map):
        axisx = Rm.randrange(1, 19)
        axisy = Rm.randrange(1, 19)
        if map[axisx][axisy] == ' ':
            self.axisX = axisx
            self.axisY = axisy
        else:
            self.spawn(self, map)


class Oveja:
    def __init__(self, x, y, map):
        self.pastPostX = 0
        self.pastPostY = 0
        self.axisX = x
        self.axisY = y
        self.canMove = True

        self.eatTime = 0
        self.satiate = False

        self.figure = 'O'

        self.map = map
        self.knwlg = [
            #   Y     0    1    2    3    4    5    6    7    8    9   10   11  12    13   14   15   16   17   18   19    |  X
            ["=", '=', '=', '=', '=', '0', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ],  # 0
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 1
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 2
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 3
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 4
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 5
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 6
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 7
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 8
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],  # 9
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 10
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 11
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 12
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 13
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 14
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 15
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 16
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 17
            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '=', ],
            # 18
            ["=", '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ]  # 19
        ]
        self.exploredPos = [[x, y]]

        self.bushFound = False
        self.bushAxisX = None
        self.bushAxisY = None

        self.knwlg[self.axisX][self.axisY] = self.figure

    def revealmap(self):
        self.knwlg[self.axisX - 1][self.axisY] = self.map[self.axisX - 1][self.axisY]  # Norte
        self.knwlg[self.axisX + 1][self.axisY] = self.map[self.axisX + 1][self.axisY]  # Sur
        self.knwlg[self.axisX][self.axisY - 1] = self.map[self.axisX][self.axisY - 1]  # Est
        self.knwlg[self.axisX][self.axisY + 1] = self.map[self.axisX][self.axisY + 1]  # Oest

    def move(self):

        magicnumber = Rm.randrange(1, 5)
        self.revealmap()
        if magicnumber == 1:
            print(f"{magicnumber}: Norte")
        elif magicnumber == 2:
            print(f"{magicnumber}: Sur")
        elif magicnumber == 3:
            print(f"{magicnumber}: Este")
        elif magicnumber == 4:
            print(f"{magicnumber}: Oeste")

        if self.knwlg[self.axisX - 1][self.axisY] == 'B':
            self.bushAxisX = self.axisX - 1
            self.bushAxisY = self.axisY
            self.bushFound = True
            if self.satiate:
                self.canMove = True
            else:
                self.canMove = False

        elif self.knwlg[self.axisX + 1][self.axisY] == 'B':
            self.bushAxisX = self.axisX + 1
            self.bushAxisY = self.axisY
            self.bushFound = True
            if self.satiate:
                self.canMove = True
            else:
                self.canMove = False

        elif self.knwlg[self.axisX][self.axisY - 1] == 'B':
            self.bushAxisX = self.axisX
            self.bushAxisY = self.axisY - 1
            self.bushFound = True
            if self.satiate:
                self.canMove = True
            else:
                self.canMove = False

        elif self.knwlg[self.axisX][self.axisY + 1] == 'B':
            self.bushAxisX = self.axisX
            self.bushAxisY = self.axisY + 1
            self.bushFound = True
            if self.satiate:
                self.canMove = True
            else:
                self.canMove = False

        if self.canMove:

            if self.knwlg[self.axisX - 1][self.axisY] and self.knwlg[self.axisX][self.axisY - 1] == '=' or \
                    self.knwlg[self.axisX - 1][self.axisY] and self.knwlg[self.axisX][self.axisY + 1] == '=' or \
                    self.knwlg[self.axisX + 1][self.axisY] and self.knwlg[self.axisX][self.axisY - 1] == '=' or \
                    self.knwlg[self.axisX + 1][self.axisY] and self.knwlg[self.axisX][self.axisY + 1] == '=':
                if magicnumber == 1:
                    if self.knwlg[self.axisX - 1][self.axisY] not in ENTITYS:
                        self.exploredPos.append([self.axisX - 1, self.axisY])
                        print(f"{magicnumber}: Norte - Pro")
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX -= 1
                    else:
                        self.move()
                elif magicnumber == 2:
                    if self.knwlg[self.axisX + 1][self.axisY] not in ENTITYS:
                        self.exploredPos.append([self.axisX + 1, self.axisY])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX += 1
                        print(f"{magicnumber}: Sur - pro")
                    else:
                        self.move()
                elif magicnumber == 3:
                    if self.knwlg[self.axisX][self.axisY - 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY - 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY -= 1
                        print(f"{magicnumber}: Este - pro")
                    else:
                        self.move()
                elif magicnumber == 4:
                    if self.knwlg[self.axisX][self.axisY + 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY + 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY += 1
                        print(f"{magicnumber}: Oeste pro")
                    else:
                        self.move()

                    print("Sexo")

            elif [self.axisX - 1, self.axisY] and \
                    [self.axisX + 1, self.axisY] and \
                    [self.axisX, self.axisY - 1] and [self.axisX, self.axisY + 1] in self.exploredPos:

                print("Ya estuve por aqui")

                if magicnumber == 1:
                    if self.knwlg[self.axisX - 1][self.axisY] not in ENTITYS:
                        self.exploredPos.append([self.axisX - 1, self.axisY])
                        print(f"{magicnumber}: Norte - Pro")
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX -= 1
                    else:
                        self.move()
                elif magicnumber == 2:
                    if self.knwlg[self.axisX + 1][self.axisY] not in ENTITYS:
                        self.exploredPos.append([self.axisX + 1, self.axisY])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX += 1
                        print(f"{magicnumber}: Sur - pro")
                    else:
                        self.move()
                elif magicnumber == 3:
                    if self.knwlg[self.axisX][self.axisY - 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY - 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY -= 1
                        print(f"{magicnumber}: Este - pro")
                    else:
                        self.move()
                elif magicnumber == 4:
                    if self.knwlg[self.axisX][self.axisY + 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY + 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY += 1
                        print(f"{magicnumber}: Oeste pro")
                    else:
                        self.move()

            elif [self.axisX - 1, self.axisY] or [self.axisX + 1, self.axisY] or [self.axisX, self.axisY - 1] or [
                self.axisX, self.axisY + 1] not in self.exploredPos:

                if magicnumber == 1:
                    if self.knwlg[self.axisX - 1][self.axisY] not in ENTITYS \
                            and [self.axisX - 1, self.axisY] not in self.exploredPos:
                        self.exploredPos.append([self.axisX - 1, self.axisY])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX -= 1
                        print(f"{magicnumber}: Norte")
                    else:
                        self.move()
                elif magicnumber == 2:
                    if self.knwlg[self.axisX + 1][self.axisY] not in ENTITYS and \
                            [self.axisX, self.axisY + 1] not in self.exploredPos:
                        self.exploredPos.append([self.axisX + 1, self.axisY])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisX += 1
                        print(f"{magicnumber}: Sur")
                    else:
                        self.move()
                elif magicnumber == 3:
                    if self.knwlg[self.axisX][self.axisY - 1] not in ENTITYS and \
                            [self.axisX, self.axisY - 1] not in self.exploredPos:
                        self.exploredPos.append([self.axisX, self.axisY - 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY -= 1
                        print(f"{magicnumber}: Este")
                    else:
                        self.move()
                elif magicnumber == 4:
                    if self.knwlg[self.axisX][self.axisY + 1] not in ENTITYS and \
                            [self.axisX, self.axisY + 1] not in self.exploredPos:
                        self.exploredPos.append([self.axisX, self.axisY + 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY += 1
                        print(f"{magicnumber}: Oeste")
                    else:
                        self.move()
        else:
            print("Comer")

    def movescape(self):

        self.knwlg = [
            #   Y     0    1    2    3    4    5    6    7    8    9   10   11  12    13   14   15   16   17   18   19    |  X
            ["=", '=', '=', '=', '=', '0', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ],  # 0
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 1
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 2
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 3
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 4
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 5
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 6
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 7
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 8
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 9
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],
            # 10
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],
            # 11
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],
            # 12
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],
            # 13
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],
            # 14
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', ],
            # 15
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ],
            # 16
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '█', ' ', ' ', '=', ],
            # 17
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ],
            # 18
            ["=", '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', 'O', 'V', 'J', '=', ]  # 19
        ]

        self.pastPostX = self.axisX
        self.pastPostY = self.axisY

        print(f"[{self.pastPostX}][{self.axisY}]")

        self.axisX -= 1
        # self.axisY += 1

    def existinmap(self, map):
        map[self.axisX][self.axisY] = self.figure

    def eat(self):
        if self.eatTime < 6:
            self.canMove = False
            self.eatTime += 1
        else:
            self.satiate = True


class Pastor:
    def __init__(self, x, y, map):
        self.pastPostX = 0
        self.pastPostY = 0
        self.axisX = x
        self.axisY = y
        self.figure = 'S'
        self.map = map
        self.knwlg = [

            ["=", '=', '=', '=', '=', '0', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ],  # 0
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 1
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 2
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 3
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 4
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 5
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 6
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 7
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 8
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 9
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],
            # 10
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],
            # 11
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],
            # 12
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],
            # 13
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],
            # 14
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', ],
            # 15
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ],
            # 16
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '█', ' ', ' ', '=', ],
            # 17
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ],
            # 18
            ["=", '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ]  # 19
        ]
        self.canMove = True

    def move(self):

        if self.canMove:
            self.pastPostX = self.axisX
            self.pastPostY = self.axisY

            self.knwlg[self.axisX - 1][self.axisY] = self.map[self.axisX - 1][self.axisY]  # Norte
            self.knwlg[self.axisX + 1][self.axisY] = self.map[self.axisX + 1][self.axisY]  # Sur
            self.knwlg[self.axisX][self.axisY - 1] = self.map[self.axisX][self.axisY - 1]  # Este
            self.knwlg[self.axisX][self.axisY + 1] = self.map[self.axisX][self.axisY + 1]  # Oeste

        def selectdirection():
            magicnumber = Rm.randrange(1, 5)

            self.knwlg[self.axisX][self.axisY] = 'X'

            if magicnumber == 1:
                if self.knwlg[self.axisX - 1][self.axisY] == ' ':
                    self.axisX -= 1
                elif self.knwlg[self.axisX - 1][self.axisY] != ' ':
                    selectdirection()
            if magicnumber == 2:
                if self.knwlg[self.axisX + 1][self.axisY] == ' ':
                    self.axisX += 1
                elif self.knwlg[self.axisX + 1][self.axisY] != ' ':
                    selectdirection()
            if magicnumber == 3:
                if self.knwlg[self.axisX][self.axisY - 1] == ' ':
                    self.axisY -= 1
                elif self.knwlg[self.axisX][self.axisY - 1] != ' ':
                    selectdirection()
            if magicnumber == 4:
                if self.knwlg[self.axisX][self.axisY + 1] == ' ':
                    self.axisY += 1
                elif self.knwlg[self.axisX][self.axisY + 1] != ' ':
                    selectdirection()

        selectdirection()

    def existinmap(self, map):
        map[self.axisX][self.axisY] = self.figure


def renewposition(axisx, axisy, map):
    map[axisx][axisy] = ' '


def printmap(map):
    for fila in map:
        for pos in fila:
            print(pos, end=" ")
        print()
