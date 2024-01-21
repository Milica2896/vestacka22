SET_STONE = 'set'
MOVE_STONE = 'move'
REMOVE_STONE = 'remove'

WHITE = 1
BLACK = -1

MOVE_TYPE = 0
MOVE_COLOR = 1
MOVE_X = 2
MOVE_Y = 3
MOVE_Z = 4

COMPUTER_PLAYER = 1
PLAYER = -1

def is_end(state): #da li je kraj 
    return state['white_remaining'] == 0 and state['black_remaining'] == 0 and (state['white_count'] <= 2 or state['black_count'] <= 2)






def custom_easy_evaluate(state): 
    kamenje = state['stones'] #stanje igre
    vrednost = 0 #vrednost za trenutno stanje igre

    # težine za komponente heuristike
    tezina_kamena = 5  
    tezina_potencijalnih_milnova = 3  
    tezina_milna = 10  
    tezina_pokretljivosti = 2  
    tezina_linije = 5  

    #vrednosti za tezinu kamenja
    vrednost -= state['white_count'] * tezina_kamena  
    vrednost += state['black_count'] * tezina_kamena 

            # Dodaj vrednost na osnovu broja slobodnih polja na tabli
        vrednost += kamenje.count(0) * tezina_pokretljivosti  #+przna polja
        vrednost -= kamenje.count(1) * tezina_pokretljivosti  #-za zauzeta polja
#mi moramo da dodamo tezinu_pokretljivost na ova przna polja jer nam prilikom bacanja oni znace

   #  prepoznavanje i ocenjivanje mlinova na tabli igre
        for kvadrat in range(3):
            for linija in [0, 2]:
                suma_linije = sum(kamenje[kvadrat][linija])
                if abs(suma_linije) == 3:
                    vrednost += tezina_milna if suma_linije > 0 else -tezina_milna
        # Brojanje linija
        for kvadrat in range(3):
            for linija in [0, 1, 2]:
                suma_linije = sum(kamenje[kvadrat][linija])
                if abs(suma_linije) == 3:
                    vrednost += tezina_linije if suma_linije > 0 else -tezina_linije

        return vrednost


def srednja_heuristika(state):
   
    kamenje = state['stones']

    
    vrednost = 0

    # težine za komponente heuristike
    tezina_kamena = 5  
    tezina_potencijalnih_milnova = 3  
    tezina_milna = 20  
    tezina_pokretljivosti = 5  
    tezina_linije = 15 

    # brojanje broja kamena
    vrednost -= state['white_count'] * 200
    vrednost += state['black_count'] * 250  

        # brojanje potencijalnih mlinova
        for kvadrat in range(3):
            for linija in [0, 2]:
                suma_linije = sum(kamenje[kvadrat][linija])
                if abs(suma_linije) == 2 and 0 in kamenje[kvadrat][linija]:
                    vrednost += tezina_potencijalnih_milnova if suma_linije > 0 else -tezina_potencijalnih_milnova

            #  prepoznavanje i ocenjivanje mlinova na tabli igre
        for kvadrat in range(3):
            for linija in [0, 2]:
                suma_linije = sum(kamenje[kvadrat][linija])
                if abs(suma_linije) == 3:
                    vrednost += tezina_milna if suma_linije > 0 else -tezina_milna

   
            #u zavisnosti na 
        vrednost += kamenje.count(0) * tezina_pokretljivosti 
        vrednost -= kamenje.count(1) * tezina_pokretljivosti 

        # Brojanje linija
        for kvadrat in range(3):
            for linija in [0, 1, 2]:
                suma_linije = sum(kamenje[kvadrat][linija])
                if abs(suma_linije) == 3:
                    vrednost += tezina_linije if suma_linije > 0 else -tezina_linije


        return vrednost

def hard_heuristika(state):
    
    kamenje = state['stones']

    vrednost = 0

   
    tezina_kamena = 5  
    tezina_potencijalnih_milnova = 3 
    tezina_milna = 20  
    tezina_pokretljivosti = 5  
    tezina_linije = 15  

   
    vrednost += state['white_count'] *  100
    vrednost -= state['black_count'] *  250 

       
        for kvadrat in range(3):
            for linija in [0, 2]:
                suma_linije = sum(kamenje[kvadrat][linija])
                if abs(suma_linije) == 2 and 0 in kamenje[kvadrat][linija]:
                    vrednost += tezina_potencijalnih_milnova if suma_linije > 0 else -tezina_potencijalnih_milnova

            
        for kvadrat in range(3):
            for linija in [0, 2]:
                suma_linije = sum(kamenje[kvadrat][linija])
                if abs(suma_linije) == 3:
                    vrednost += tezina_milna if suma_linije > 0 else -tezina_milna

   
            
        vrednost += kamenje.count(0) * tezina_pokretljivosti  
        vrednost -= kamenje.count(1) * tezina_pokretljivosti  

        # Brojanje linija
        for kvadrat in range(3):
            for linija in [0, 1, 2]:
                suma_linije = sum(kamenje[kvadrat][linija])
                if abs(suma_linije) == 3:
                    vrednost += tezina_linije if suma_linije > 0 else -tezina_linije

       
          napravljen_mlin += tezina_linije if suma_linije == 3 else -tezina_linije
          
                potez_unazad = izvrsi_potez_unazad(state)
                vrednost -= srednja_heuristika(state)  
                poništi_potez(state, potez_unazad)

                potez_unapred = izvrsi_potez_unapred(state)
                vrednost += srednja_heuristika(state) 
                poništi_potez(state, potez_unapred)
        return vrednost





def susedna_mesta(state, x, y, z):
    stones = state['stones']
    
    # levo
    if y != 1 and z - 1 >= 0 and stones[x][y][z - 1] == 0:
        yield x, y, z - 1
    
    # desno
    if y != 1 and z + 1 <= 2 and stones[x][y][z + 1] == 0:
        yield x, y, z + 1
    
    # gore
    if z != 1 and y - 1 >= 0 and stones[x][y - 1][z] == 0:
        yield x, y - 1, z
    
    # dole
    if z != 1 and y + 1 <= 2 and stones[x][y + 1][z] == 0:
        yield x, y + 1, z
    
    # 
    if (y == 1 or z == 1) and x - 1 >= 0 and stones[x - 1][y][z] == 0:
        yield x - 1, y, z
    
    # 
    if (y == 1 or z == 1) and x + 1 <= 2 and stones[x + 1][y][z] == 0:
        yield x + 1, y, z


def sledeci_potez(state, player, line_made):
    # ukloni kamen
    if line_made:
        for s, square in enumerate(state['stones']):
            for i, row in enumerate(square):
                for j, element in enumerate(row):
                    if element == player * -1:
                        yield REMOVE_STONE, player, s, i, j
        return
    
    #postavi kamen
    if state['white_remaining' if player == 1 else 'black_remaining'] > 0:
        for s, square in enumerate(state['stones']):
            for i, row in enumerate(square):
                for j, element in enumerate(row):
                    if i == 1 and j == 1:
                        continue
                    if element == 0:
                        yield SET_STONE, player, s, i, j
                    
        return
    
    #pomeri kamen
    for s, square in enumerate(state['stones']):
        for i, row in enumerate(square):
            for j, element in enumerate(row):
                if element == player:
                    for x, y, z in susedna_mesta(state, s, i, j):
                        yield MOVE_STONE, player, x, y, z, s, i, j


def pravi_liniju(state, move):
    stones = state['stones']
    _, _, x, y, z, *_ = move
    
    # Provera horizontalne linije
    if abs(sum(stones[x][y])) == 3:
        return True
    
    # Provera vertikalne linije
    if abs(sum(stones[x][i][z] for i in range(3))) == 3:
        return True
    
    # Provera dijagonalne linije koja prolazi kroz centar
    if x == 1 and y == 1 and z == 1:
        if abs(sum(stones[i][1][1] for i in range(3))) == 3:
            return True
    
    # Provera dijagonalne linije koja prolazi kroz sredinu tabele
    if abs(sum(stones[i][1][1] for i in range(3))) == 3:
        return True
    if abs(sum(stones[1][i][1] for i in range(3))) == 3:
        return True
    if abs(sum(stones[1][1][i] for i in range(3))) == 3:
        return True

    
    return False



def primeni_potez(state, move):    
    stones = state['stones'] 
    if move[MOVE_TYPE] == SET_STONE: #proveravamo tip poteza
        _, color, x, y, z = move #gledamo boju kamena
        stones[x][y][z] = color #postavljamo kamen odredjene boje
        state['white_remaining' if color == WHITE else 'black_remaining'] -= 1  #smanjujemo preostali
        state['white_count' if color == WHITE else 'black_count'] += 1 #povecava broj postavljenih
    elif move[MOVE_TYPE] == REMOVE_STONE: #uklanjanje
        _, color, x, y, z = move 
        stones[x][y][z] = 0 #postavi  se vrednost 0 na mestu gde se ukloni
        state['white_count' if color == WHITE else 'black_count'] -= 1 #smanjuje se broj postavljenih kamena za odgovarajucu boju
    elif move[MOVE_TYPE] == MOVE_STONE: #pomeranje
        _, color, to_x, to_y, to_z, from_x, from_y, from_z = move
        stones[from_x][from_y][from_z] = 0 #uklanja se kamen sa polazne pozicije
        stones[to_x][to_y][to_z] = color #nova pozicija
        
    state['turn'] += 1

def ponisti_potez(state, move):
    stones = state['stones']
    if move[MOVE_TYPE] == SET_STONE:
        _, color, x, y, z = move
        stones[x][y][z] = 0 #uklanjamo kamen sa te pozicije
        state['white_remaining' if color == WHITE else 'black_remaining'] += 1 #povecava se broj preostalih kamenova za odgovarajucu boju
        state['white_count' if color == WHITE else 'black_count'] -= 1 #smanjuje se broj postavljenih  kamenova za odgovarajucu boju
    elif move[MOVE_TYPE] == REMOVE_STONE:
        _, color, x, y, z = move
        stones[x][y][z] = color * -1 #na mestu gde se uklanja postavlja se kamen druge boje
        state['white_count' if color == WHITE else 'black_count'] += 1 #povecava se broj postavljenih kamenova za odgovarajucu boju
    elif move[MOVE_TYPE] == MOVE_STONE:
        _, color, to_x, to_y, to_z, from_x, from_y, from_z = move
        stones[from_x][from_y][from_z] = color #na mestu polazne pozicije postavlja se kamen
        stones[to_x][to_y][to_z] = 0 #na mestu ciljne pozicije uklanja se kamen
    
    state['turn'] -= 1 #smanjujemo broj poteza




def minimax(state, depth, player, line_made=False, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or is_end(state):
        return custom_easy_evaluate(state), None

    next_player = PLAYER if player == COMPUTER_PLAYER else COMPUTER_PLAYER

    if player == COMPUTER_PLAYER:
        value = float('-inf')
        best_move = None
        for move in sledeci_potez(state, player, line_made):
            primeni_potez(state, move)
            if pravi_liniju(state, move):
                next_player *= -1
                line_made = True
            if move[MOVE_TYPE] == REMOVE_STONE:
                line_made = False
            new_value, _ = minimax(state, depth - 1, next_player, line_made, alpha, beta)
            if new_value > value:
                best_move = move
                value = new_value
            line_made = False
            ponisti_potez(state, move)
            alpha = max(alpha, value)
            if value >= beta:
                break
        return value, best_move
    else:
        value = float('inf')
        best_move = None
        for move in sledeci_potez(state, player, line_made):
            primeni_potez(state, move)
            if pravi_liniju(state, move):
                next_player *= -1
                line_made = True
            if move[MOVE_TYPE] == REMOVE_STONE:
                line_made = False
            new_value, _ = minimax(state, depth - 1, next_player, line_made, alpha, beta)
            if new_value < value:
                best_move = move
                value = new_value
            line_made = False
            ponisti_potez(state, move)
            beta = min(beta, value)
            if value <= alpha:
                break
        return value, best_move


import random








def alphabeta(state, depth, a, b, player, line_made=False):
    if depth == 0 or is_end(state):
        return hard_heuristic(state), None

    next_player = PLAYER if player == COMPUTER_PLAYER else COMPUTER_PLAYER

    if player == COMPUTER_PLAYER:
        value = float('-inf')
        best_move = None
        for move in sledeci_potez(state, player, line_made):
            primeni_potez(state, move)
            if pravi_liniju(state, move):
                next_player *= -1
                line_made = True
            if move[MOVE_TYPE] == REMOVE_STONE:
                line_made = False
            new_value, _ = alphabeta(state, depth - 1, a, b, next_player, line_made)
            if new_value > value:
                best_move = move
                value = new_value
            line_made = False
            ponisti_potez(state, move)
            a = max(a, value)
            if value >= b:
                break
        return value, best_move
    else:
        value = float('inf')
        best_move = None
        for move in sledeci_potez(state, player, line_made):
            primeni_potez(state, move)
            if pravi_liniju(state, move):
                next_player *= -1
                line_made = True
            if move[MOVE_TYPE] == REMOVE_STONE:
                line_made = False
            new_value, _ = alphabeta(state, depth - 1, a, b, next_player, line_made)
            if new_value < value:
                best_move = move
                value = new_value
            line_made = False
            ponisti_potez(state, move)
            b = min(b, value)
            if value <= a:
                break
        return value, best_move



def alphabeta(state, depth, a, b, player, line_made=False):
    if depth == 0 or is_end(state):
        return hard_heuristic(state), None

    next_player = PLAYER if player == COMPUTER_PLAYER else COMPUTER_PLAYER

    if player == COMPUTER_PLAYER:
        value = float('-inf')
        best_move = None
        for move in sledeci_potez(state, player, line_made):
            primeni_potez(state, move)
            if pravi_liniju(state, move):
                next_player *= -1
                line_made = True
            if move[MOVE_TYPE] == REMOVE_STONE:
                line_made = False
            new_value, _ = alphabeta(state, depth - 1, a, b, next_player, line_made)
            if new_value > value:
                best_move = move
                value = new_value
            line_made = False
            ponisti_potez(state, move)
            a = max(a, value)
            if value >= b:
                break
        return value, best_move
    else:
        value = float('inf')
        best_move = None
        for move in sledeci_potez(state, player, line_made):
            primeni_potez(state, move)
            if pravi_liniju(state, move):
                next_player *= -1
                line_made = True
            if move[MOVE_TYPE] == REMOVE_STONE:
                line_made = False
            new_value, _ = alphabeta(state, depth - 1, a, b, next_player, line_made)
            if new_value < value:
                best_move = move
                value = new_value
            line_made = False
            ponisti_potez(state, move)
            b = min(b, value)
            if value <= a:
                break
        return value, best_move


