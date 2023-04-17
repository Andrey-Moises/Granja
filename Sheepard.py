import random as rm
ENTITYS = ['B', 'S', '=', '0', 'O']


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
        self.exploredPos = [[x, y]]

        self.canMove = True

        self.sheepFounded = False
        self.sheepCordinates = []

    def move(self):

        magicnumber = rm.randrange(1, 5)

        if self.knwlg[self.axisX - 1][self.axisY] == 'O':
            self.sheepCordinates = [self.axisX - 1, self.axisY]
            self.sheepFounded = True

        elif self.knwlg[self.axisX + 1][self.axisY] == 'O':
            self.sheepCordinates = [self.axisX + 1, self.axisY]
            self.sheepFounded = True

        elif self.knwlg[self.axisX][self.axisY - 1] == 'O':
            self.sheepCordinates = [self.axisX, self.axisY - 1]
            self.sheepFounded = True

        elif self.knwlg[self.axisX][self.axisY + 1] == 'O':
            self.sheepCordinates = [self.axisX, self.axisY + 1]
            self.sheepFounded = True

        if self.sheepFounded:

            self.canMove = False
            print("La vi pero no la toque UnU")

        if self.canMove:

            if self.knwlg[self.axisX - 1][self.axisY] and self.knwlg[self.axisX][self.axisY - 1] == '=' or \
                    self.knwlg[self.axisX - 1][self.axisY] and self.knwlg[self.axisX][self.axisY + 1] == '=' or \
                    self.knwlg[self.axisX + 1][self.axisY] and self.knwlg[self.axisX][self.axisY - 1] == '=' or \
                    self.knwlg[self.axisX + 1][self.axisY] and self.knwlg[self.axisX][self.axisY + 1] == '=':
                if magicnumber == 1:
                    if self.knwlg[self.axisX - 1][self.axisY] not in ENTITYS:
                        self.exploredPos.append([self.axisX - 1, self.axisY])
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
                    else:
                        self.move()
                elif magicnumber == 3:
                    if self.knwlg[self.axisX][self.axisY - 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY - 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY -= 1
                    else:
                        self.move()
                elif magicnumber == 4:
                    if self.knwlg[self.axisX][self.axisY + 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY + 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY += 1
                    else:
                        self.move()

            elif [self.axisX - 1, self.axisY] or [self.axisX + 1, self.axisY] or [self.axisX, self.axisY - 1] or \
                    [self.axisX, self.axisY + 1] == ' ':

                if magicnumber == 1:
                    if self.knwlg[self.axisX - 1][self.axisY] not in ENTITYS:
                        self.exploredPos.append([self.axisX - 1, self.axisY])
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
                    else:
                        self.move()
                elif magicnumber == 3:
                    if self.knwlg[self.axisX][self.axisY - 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY - 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY -= 1
                    else:
                        self.move()
                elif magicnumber == 4:
                    if self.knwlg[self.axisX][self.axisY + 1] not in ENTITYS:
                        self.exploredPos.append([self.axisX, self.axisY + 1])
                        self.pastPostX = self.axisX
                        self.pastPostY = self.axisY
                        self.axisY += 1
                    else:
                        self.move()

    def existinmap(self, map):
        map[self.axisX][self.axisY] = self.figure
