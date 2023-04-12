import random as Rm



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
            self.axisX = 2
            self.axisY = 4
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

        self.bushFound = False
        self.bushAxisX = None
        self.bushAxisY = None

        self.knwlg[self.axisX][self.axisY] = self.figure

    def move(self):

        def traped(): # Checar que se pueda mover
            if          self.knwlg[self.axisX - 1][self.axisY] == 'X' or self.knwlg[self.axisX - 1][self.axisY] == '='\
                    and self.knwlg[self.axisX + 1][self.axisY] == 'X' or self.knwlg[self.axisX + 1][self.axisY] == '='\
                    and self.knwlg[self.axisX][self.axisY - 1] == 'X' or self.knwlg[self.axisX][self.axisY - 1] == '='\
                    and self.knwlg[self.axisX][self.axisY + 1] == 'X' or self.knwlg[self.axisX][self.axisY + 1] == '=':
                return True

        def selectdirection():

            magicnumber = Rm.randrange(1, 5)

            if  self.knwlg[self.axisX - 1][self.axisY] == 'B':
                self.bushAxisX = self.axisX - 1
                self.bushAxisY = self.axisY
                self.bushFound = True
                self.eat()

            elif self.knwlg[self.axisX + 1][self.axisY] == 'B':
                self.bushAxisX = self.axisX + 1
                self.bushAxisY = self.axisY
                self.bushFound = True
                self.eat()

            elif self.knwlg[self.axisX][self.axisY - 1] == 'B':
                self.bushAxisX = self.axisX
                self.bushAxisY = self.axisY - 1
                self.bushFound = True
                self.eat()

            elif self.knwlg[self.axisX][self.axisY + 1] == 'B':
                self.bushAxisX = self.axisX
                self.bushAxisY = self.axisY + 1
                self.bushFound = True
                self.eat()

            else:

                self.knwlg[self.axisX][self.axisY] = 'X'

                if magicnumber == 1:
                    if self.knwlg[self.axisX - 1][self.axisY] == ' ':
                        self.axisX -= 1
                    elif traped():
                        self.knwlg = [
                            #   Y     0    1    2    3    4    5    6    7    8    9   10   11  12    13   14   15   16   17   18   19    |  X
                            ["=", '=', '=', '=', '=', '0', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=',
                             '=', ],  # 0
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 1
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 2
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 3
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 4
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 5
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 6
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 7
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 8
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 9
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 10
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 11
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 12
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 13
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 14
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 15
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 16
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 17
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 18
                            ["=", '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=',
                             '=', ]  # 19
                        ]
                        self.knwlg[self.axisX][self.axisY] = self.figure
                        if self.knwlg[self.axisX - 1][self.axisY] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX - 1][self.axisY] = self.map[self.axisX - 1][self.axisY]  # Norte

                        if self.knwlg[self.axisX + 1][self.axisY] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX + 1][self.axisY] = self.map[self.axisX + 1][self.axisY]  # Sur

                        if self.knwlg[self.axisX][self.axisY - 1] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX][self.axisY - 1] = self.map[self.axisX][self.axisY - 1]  # Este

                        if self.knwlg[self.axisX][self.axisY + 1] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX][self.axisY + 1] = self.map[self.axisX][self.axisY + 1]  # Oeste

                    else:
                        selectdirection()
                if magicnumber == 2:
                    if self.knwlg[self.axisX + 1][self.axisY] == ' ':
                        self.axisX += 1
                    elif traped():
                        self.knwlg = [
                            #   Y     0    1    2    3    4    5    6    7    8    9   10   11  12    13   14   15   16   17   18   19    |  X
                            ["=", '=', '=', '=', '=', '0', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=',
                             '=', ],  # 0
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 1
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 2
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 3
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 4
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 5
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 6
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 7
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 8
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 9
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 10
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 11
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 12
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 13
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 14
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 15
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 16
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 17
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 18
                            ["=", '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=',
                             '=', ]  # 19
                        ]
                        self.knwlg[self.axisX][self.axisY] = self.figure
                        if self.knwlg[self.axisX - 1][self.axisY] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX - 1][self.axisY] = self.map[self.axisX - 1][self.axisY]  # Norte

                        if self.knwlg[self.axisX + 1][self.axisY] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX + 1][self.axisY] = self.map[self.axisX + 1][self.axisY]  # Sur

                        if self.knwlg[self.axisX][self.axisY - 1] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX][self.axisY - 1] = self.map[self.axisX][self.axisY - 1]  # Este

                        if self.knwlg[self.axisX][self.axisY + 1] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX][self.axisY + 1] = self.map[self.axisX][self.axisY + 1]  # Oeste

                    else:
                        selectdirection()
                if magicnumber == 3:
                    if self.knwlg[self.axisX][self.axisY - 1] == ' ':
                        self.axisY -= 1
                    elif traped():
                        self.knwlg = [
                            #   Y     0    1    2    3    4    5    6    7    8    9   10   11  12    13   14   15   16   17   18   19    |  X
                            ["=", '=', '=', '=', '=', '0', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=',
                             '=', ],  # 0
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 1
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 2
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 3
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 4
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 5
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 6
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 7
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 8
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 9
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 10
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 11
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 12
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 13
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 14
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 15
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 16
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 17
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 18
                            ["=", '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=',
                             '=', ]  # 19
                        ]
                        self.knwlg[self.axisX][self.axisY] = self.figure
                        if self.knwlg[self.axisX - 1][self.axisY] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX - 1][self.axisY] = self.map[self.axisX - 1][self.axisY]  # Norte

                        if self.knwlg[self.axisX + 1][self.axisY] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX + 1][self.axisY] = self.map[self.axisX + 1][self.axisY]  # Sur

                        if self.knwlg[self.axisX][self.axisY - 1] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX][self.axisY - 1] = self.map[self.axisX][self.axisY - 1]  # Este

                        if self.knwlg[self.axisX][self.axisY + 1] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX][self.axisY + 1] = self.map[self.axisX][self.axisY + 1]  # Oeste

                    else:
                        selectdirection()
                if magicnumber == 4:
                    if self.knwlg[self.axisX][self.axisY + 1] == ' ':
                        self.axisY += 1
                    elif traped():
                        self.knwlg = [
                            #   Y     0    1    2    3    4    5    6    7    8    9   10   11  12    13   14   15   16   17   18   19    |  X
                            ["=", '=', '=', '=', '=', '0', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=',
                             '=', ],  # 0
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 1
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 2
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 3
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 4
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 5
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 6
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 7
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 8
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],  # 9
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 10
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 11
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 12
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 13
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 14
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 15
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 16
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 17
                            ["=", '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓',
                             '=', ],
                            # 18
                            ["=", '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=',
                             '=', ]  # 19
                        ]
                        self.knwlg[self.axisX][self.axisY] = self.figure
                        if self.knwlg[self.axisX - 1][self.axisY] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX - 1][self.axisY] = self.map[self.axisX - 1][self.axisY]  # Norte

                        if self.knwlg[self.axisX + 1][self.axisY] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX + 1][self.axisY] = self.map[self.axisX + 1][self.axisY]  # Sur

                        if self.knwlg[self.axisX][self.axisY - 1] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX][self.axisY - 1] = self.map[self.axisX][self.axisY - 1]  # Este

                        if self.knwlg[self.axisX][self.axisY + 1] != 'X' and self.knwlg[self.axisX - 1][
                            self.axisY] != 'B':
                            self.knwlg[self.axisX][self.axisY + 1] = self.map[self.axisX][self.axisY + 1]  # Oeste

                    else:
                        selectdirection()

        if self.canMove:

            self.pastPostX = self.axisX
            self.pastPostY = self.axisY

            # FUNCIONES QUE REVELAN EL MAPA EN DIRECCION A LOS PUNTOS CARDINALES

            if self.knwlg[self.axisX - 1][self.axisY] != 'X' and self.knwlg[self.axisX - 1][self.axisY] != 'B':
                self.knwlg[self.axisX - 1][self.axisY] = self.map[self.axisX - 1][self.axisY]  # Norte

            if self.knwlg[self.axisX + 1][self.axisY] != 'X' and self.knwlg[self.axisX - 1][self.axisY] != 'B':
                self.knwlg[self.axisX + 1][self.axisY] = self.map[self.axisX + 1][self.axisY]  # Sur

            if self.knwlg[self.axisX][self.axisY - 1] != 'X' and self.knwlg[self.axisX - 1][self.axisY] != 'B':
                self.knwlg[self.axisX][self.axisY - 1] = self.map[self.axisX][self.axisY - 1]  # Este

            if self.knwlg[self.axisX][self.axisY + 1] != 'X' and self.knwlg[self.axisX - 1][self.axisY] != 'B':
                self.knwlg[self.axisX][self.axisY + 1] = self.map[self.axisX][self.axisY + 1]  # Oeste

            selectdirection()

        else:
            self.existinmap(self.knwlg)
            selectdirection()

    def existinmap(self, map):
        map[self.axisX][self.axisY] = self.figure

    def eat(self):
        print(self.eatTime)
        self.canMove = False
        self.eatTime += 1
        if self.eatTime > 6:
            self.knwlg[self.bushAxisX][self.axisY] = ' '
            self.canMove = True


class Pastor:
    def __init__(self, x, y, map):
        self.pastPostX = 0
        self.pastPostY = 0
        self.axisX = x
        self.axisY = y
        self.figure = 'S'
        self.map = map
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
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 10
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 11
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 12
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 13
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ],  # 14
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', ],# 15
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ],# 16
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '█', ' ', ' ', '=', ],# 17
            ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ],# 18
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
