import Entitys as Ent
import time as Time

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
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '█', ' ', ' ', '=', ], #17
        ["=", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', '=', ], #18
        ["=", '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ]  #19
    ]
    ovj = Ent.Oveja(1, 4, mapGranja)

    shep1 = Ent.Pastor(18, 14, mapGranja)
    shep2 = Ent.Pastor(14, 15, mapGranja)
    shep3 = Ent.Pastor(12, 18, mapGranja)

    bush = Ent.Arbusto()
    bush.spawn(mapGranja)

    while FINAL:
        print("\n")

        ovj.existinmap(mapGranja)   # Posicionarse en el mapa Global - Oveja
        bush.existinmap(mapGranja)  # Posicionarse en el Mapa Global - Arbusto
        # shep1.existinmap(mapGranja) # Posicionarse en el Mapa Global - Granjero 1
        # shep2.existinmap(mapGranja) # Posicionarse en el Mapa Global - Granjero 2
        # shep3.existinmap(mapGranja) # Posicionarse en el Mapa Global - Granjero3
        ovj.existinmap(ovj.knwlg)   # Posicionarse en el Mapa del agente - Oveja

        Ent.printmap(mapGranja) # Imprimir Mapa Global
        Ent.printmap(ovj.knwlg) # Imprimir Mapa del agente - Oveja

        ovj.move()
        # shep1.move() # ?
        # shep2.move() # ?
        # shep3.move() # ?

        Ent.renewposition(ovj.pastPostX, ovj.pastPostY, mapGranja) # Limpiar posicion de la oveja
        # Ent.renewposition(shep1.pastPostX, shep1.pastPostY, mapGranja)
        # Ent.renewposition(shep2.pastPostX, shep2.pastPostY, mapGranja)
        # Ent.renewposition(shep3.pastPostX, shep3.pastPostY, mapGranja)

        ovj.existinmap(mapGranja)
        # shep1.existinmap(mapGranja)
        # shep2.existinmap(mapGranja)
        # shep3.existinmap(mapGranja)










