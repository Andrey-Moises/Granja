import Sheep
import time
import os
import Sheepard
import Bush


def renewposition(axisx, axisy, map):
    map[axisx][axisy] = ' '


def printmap(map):
    for fila in map:
        for pos in fila:
            print(pos, end=" ")
        print()


def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def inicializer(map, caracters=None):
    if caracters is None:
        caracters = []
    else:
        for entity in caracters:
            entity.existinmap(map)


if __name__ == '__main__':

    FINAL = True

    mapGranja = [
#   Y     0    1    2    3    4    5    6    7    8    9   10   11  12    13   14   15   16   17   18   19    |  X
        ["=", '=', '=', '=', '=', '0', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ], #0
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #1
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #2
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #3
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #4
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #5
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #6
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #7
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #8
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #9
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #10
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #11
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #12
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #13
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ], #14
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', ], #15
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ], #16
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ], #17
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ], #18
        ["=", '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ]  #19
    ]
    ovj = Sheep.Oveja(1, 5, mapGranja)
    bush = Bush.Arbusto()
    bush.spawn(mapGranja)
    shep1 = Sheepard.Pastor(18, 1, mapGranja)
    shep2 = Sheepard.Pastor(18, 15, mapGranja)
    shep3 = Sheepard.Pastor(16, 10, mapGranja)

    entitys = [ovj, bush, shep1, shep2, shep3]

    inicializer(mapGranja, entitys)

    while FINAL:

        clear()

        ovj.revealmap()
        ovj.existinmap(ovj.knwlg)

        shep1.existinmap(shep1.knwlg)
        shep1.existinmap(shep2.knwlg)
        shep1.existinmap(shep3.knwlg)

        shep2.existinmap(shep1.knwlg)
        shep2.existinmap(shep2.knwlg)
        shep2.existinmap(shep3.knwlg)

        shep3.existinmap(shep1.knwlg)
        shep3.existinmap(shep2.knwlg)
        shep3.existinmap(shep3.knwlg)

        printmap(mapGranja)
        printmap(shep1.knwlg)

        ovj.move()
        shep1.move()
        shep2.move()
        shep3.move()

        renewposition(ovj.pastPostX, ovj.pastPostY, mapGranja) # Limpiar posicion de la oveja
        renewposition(ovj.pastPostX, ovj.pastPostY, shep1.knwlg)

        renewposition(shep1.pastPostX, shep1.pastPostY, mapGranja)
        renewposition(shep1.pastPostX, shep1.pastPostY, shep1.knwlg)
        renewposition(shep2.pastPostX, shep2.pastPostY, shep2.knwlg)
        renewposition(shep3.pastPostX, shep3.pastPostY, shep3.knwlg)

        renewposition(shep2.pastPostX, shep2.pastPostY, mapGranja)
        renewposition(shep1.pastPostX, shep1.pastPostY, shep1.knwlg)
        renewposition(shep2.pastPostX, shep2.pastPostY, shep2.knwlg)
        renewposition(shep3.pastPostX, shep3.pastPostY, shep3.knwlg)

        renewposition(shep3.pastPostX, shep3.pastPostY, mapGranja)
        renewposition(shep1.pastPostX, shep1.pastPostY, shep1.knwlg)
        renewposition(shep2.pastPostX, shep2.pastPostY, shep2.knwlg)
        renewposition(shep3.pastPostX, shep3.pastPostY, shep3.knwlg)

        ovj.existinmap(mapGranja)
        shep1.existinmap(mapGranja)
        shep2.existinmap(mapGranja)
        shep3.existinmap(mapGranja)

        time.sleep(.5)

        if ovj.freedom:
            FINAL = False

    ovj.existinmap(ovj.knwlg)  # Posicionarse en el Mapa del agente - Oveja

    printmap(mapGranja)  # Imprimir Mapa Global
    printmap(ovj.knwlg)  # Imprimir Mapa del agente - Oveja
    renewposition(ovj.pastPostX, ovj.pastPostY, mapGranja)  # Limpiar posicion de la oveja
    renewposition(ovj.pastPostX, ovj.pastPostY, ovj.knwlg)

    print("Eres libre amiga. Save the World")










