import Entitys as Ent
import time as Time
import os


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
    ovj = Ent.Oveja(1, 5, mapGranja)
    bush = Ent.Arbusto()
    bush.spawn(mapGranja)

    while FINAL:

        if os.name == "posix":
            var = "clear"
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            var = "cls"
        os.system(var)

        print("\n")

        ovj.existinmap(mapGranja)   # Posicionarse en el mapa Global - Oveja
        bush.existinmap(mapGranja)  # Posicionarse en el Mapa Global - Arbusto

        ovj.revealmap()

        ovj.existinmap(ovj.knwlg)   # Posicionarse en el Mapa del agente - Oveja

        Ent.printmap(mapGranja) # Imprimir Mapa Global
        Ent.printmap(ovj.knwlg) # Imprimir Mapa del agente - Oveja

        ovj.move()
        print(f"Posicion actual: [{ovj.axisX}][{ovj.axisY}]")
        print(ovj.exploredPos)
        print(f"Posicion norte: [{ovj.axisX - 1}, {ovj.axisY}]"
              f"\nPosicion sur: [{ovj.axisX + 1}, {ovj.axisY}]"
              f"\nPosicion Este: [{ovj.axisX}, {ovj.axisY - 1}]"
              f"\nPosicion oeste: [{ovj.axisX}, {ovj.axisY + 1}]")

        Ent.renewposition(ovj.pastPostX, ovj.pastPostY, mapGranja) # Limpiar posicion de la oveja
        Ent.renewposition(ovj.pastPostX, ovj.pastPostY, ovj.knwlg)

        ovj.existinmap(mapGranja)
        Time.sleep(.10)










