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
    shep2 = Sheepard.Pastor(14, 18, mapGranja)
    shep3 = Sheepard.Pastor(1, 18, mapGranja)

    entitys = [ovj, bush, shep1, shep2, shep3]
    inicializer(mapGranja, entitys)

    while FINAL:

        clear()

        # Posicionarse en el mapa - Todas las entidades - En sus conocimientos
        ovj.existinmap(ovj.knwlg)
        shep1.existinmap(shep1.knwlg)
        shep2.existinmap(shep1.knwlg)
        shep3.existinmap(shep1.knwlg)

        # Imprimir Mapa o mapas
        printmap(mapGranja)
        # printmap(ovj.knwlg)
        # printmap(shep1.knwlg)
        # printmap(shep2.knwlg)
        # printmap(shep3.knwlg)

        # Moverse

        if shep1.sheepFounded or shep2.sheepFounded or shep3.sheepFounded:
            ovj.canMove = False
            ovj.axisX = 0
            ovj.axisY = 0
        else:
            ovj.move()

        shep1.move()
        shep2.move()
        shep3.move()

        # Limpiar posiciones en el Mapa General de todas las entidades

        renewposition(ovj.pastPostX, ovj.pastPostY, mapGranja)
        renewposition(ovj.pastPostX, ovj.pastPostY, ovj.knwlg)

        # Limpiar pocisiones en el Mapa del granjero 1 Para todas las entidades (incluyendose)

        renewposition(shep1.pastPostX, shep1.pastPostY, mapGranja)
        renewposition(shep1.pastPostX, shep1.pastPostY, shep1.knwlg)
        renewposition(shep1.pastPostX, shep1.pastPostY, shep2.knwlg)
        renewposition(shep1.pastPostX, shep1.pastPostY, shep3.knwlg)

        # Limpiar pocisiones en el Mapa del granjero 2 Para todas las entidades (incluyendose)

        renewposition(shep2.pastPostX, shep2.pastPostY, mapGranja)
        renewposition(shep2.pastPostX, shep2.pastPostY, shep1.knwlg)
        renewposition(shep2.pastPostX, shep2.pastPostY, shep2.knwlg)
        renewposition(shep2.pastPostX, shep2.pastPostY, shep3.knwlg)

        # Limpiar pocisiones en el Mapa del granjero 3 Para todas las entidades (incluyendose)

        renewposition(shep3.pastPostX, shep3.pastPostY, mapGranja)
        renewposition(shep3.pastPostX, shep3.pastPostY, shep1.knwlg)
        renewposition(shep3.pastPostX, shep3.pastPostY, shep2.knwlg)
        renewposition(shep3.pastPostX, shep3.pastPostY, shep3.knwlg)

        # Posicionarse en el mapa - Todas las entidades - En el mapa general

        if shep1.sheepFounded or shep2.sheepFounded or shep3.sheepFounded:
            pass
        else:
            ovj.existinmap(mapGranja)

        shep1.existinmap(mapGranja)
        shep2.existinmap(mapGranja)
        shep3.existinmap(mapGranja)

        time.sleep(.07)

        if ovj.freedom:
            FINAL = False
        elif shep1.jobDone or shep2.jobDone or shep3.jobDone:
            FINAL = False

    ovj.existinmap(ovj.knwlg)  # Posicionarse en el Mapa del agente - Oveja

    renewposition(ovj.pastPostX, ovj.pastPostY, mapGranja)
    renewposition(ovj.pastPostX, ovj.pastPostY, ovj.knwlg)

    clear()
    print("\n\n\n\n\n\n")
    if ovj.freedom:
        print("Eres libre amiga. Save the world - Oveja wins")
    elif shep1.jobDone or shep2.jobDone or shep3.jobDone:
        print("No hay libertad para los malditos - Pastores wins")

    print("\n")

    printmap(mapGranja)

    print("\n")

    printmap(ovj.knwlg)

    print("\n\n")
