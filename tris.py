def mossa(x:int, y:int, tris:list[list[int]], player:int)->int:
    tris[x][y] = player
    stampa(tris)
    return 3 - player

def stampa(tris:list[list[int]])->None:
    for x in range(3):
        for y in range(3):
            if tris[x][y] == 0:
                print(" ", end="|")
            elif tris[x][y] == 1:
                print("X", end="|")
            else:
                print("O", end="|")
        print("")

def vittoria(player:int, tris:list[list[int]])->bool:
        if tris[0][0] == player and tris[0][1] == player and tris[0][2] == player:
            return True
        elif tris[1][0] == player and tris[1][1] == player and tris[1][2] == player:
            return True
        elif tris[2][0] == player and tris[2][1] == player and tris[2][2] == player:
            return True
        
        elif tris[0][0] == player and tris[1][0] == player and tris[2][0] == player:
            return True
        elif tris[0][1] == player and tris[1][1] == player and tris[2][1] == player:
            return True
        elif tris[0][2] == player and tris[1][2] == player and tris[2][2] == player:
            return True

        elif tris[0][0] == player and tris[1][1] == player and tris[2][2] == player:
            return True
        elif tris[0][2] == player and tris[1][1] == player and tris[2][0] == player:
            return True
        else:
            return False

def gioca()->None:

    tris = [
        [0, 0, 0],  # 0 = niente
        [0, 0, 0],  # 1 = X
        [0, 0, 0]   # 2 = O
    ]

    end = False
    turno = 0
    player = 1  # 1 = player 1, 2 = player 2

    print("Benvenuti su TRIS\n")

    while not end and turno < 9:
        turno += 1
        if(player == 1):
            print("Turno giocatore 1 (X)")
        else:
            print("Turno giocatore 2 (O)")

        while True:
            while True:
                x = int(input("Inserisci la riga della tua mossa: ")) - 1
                if 0 <= x < 3:
                    break
                else:
                    print("Riga non esistente")
            
            while True:
                y = int(input("Inserisci la colonna della tua mossa: ")) - 1
                if 0 <= y < 3:
                    break
                else:
                    print("Riga non esistente")
            if tris[x][y] != 0:
                print("Casella gia assegnata")
            else:
                break

        player = mossa(x, y, tris, player)
        end = vittoria(3 - player, tris)
        if end:
            print("\nComplimenti giocatore", 3 - player,"hai VINTO!!!!!" )
        
        elif turno == 9:
            print("\nPareggio")
        

gioca()