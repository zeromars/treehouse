import random

CELLS = [
    (0,0),(0,1),(0,2),
    (1,0),(1,1),(1,2),
    (2,0),(2,1),(2,2)
]

def get_location():
    #monster = random
    #door = random
    #start = random
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)

    #if monster, door, start the same location do it again
    if monster == door or monster == start or door == start:
        return get_location()

    # return monster, door, start
    return monster, door, start

def move_player(player, move):
    #get the player current location
    #if move is left y-1
    #if move is right y+1
    #if move is up x-1
    #if move is down x+1
    x, y = player
    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1
    return x,y

def get_moves(player):
    moves = ['LEFT','RIGHT','UP','DOWN']
    #player = (x,y)
    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT') 
    if player[0] == 0:
        moves.remove('UP') 
    if player[0] == 2:
        moves.remove('DOWN')        
    #if players y = 0 remove left
    #if players x = 0 remove up
    #if players y = 2 remove right
    #if players x = 2 remove down
    return moves

def draw_map(player):
    print(' _ _ _ ')
    tile = '|{}'

    for idx, cell in enumerate(CELLS):
        if idx in [0,1,3,4,6,7]:
            if cell == player:
                print(tile.format('X'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))


monster, door, player = get_location()
print("Welcome to the dungeon game")

while True:
    moves = get_moves(player)        
    print("You are currently in room {}".format(player)) # fill in with player position
    
    draw_map(player)
    
    print("You can move {}".format(moves)) #fill in with available moves
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    if move in moves:
        player = move_player(player, move)
    else:
        print("Walls are hard stop walking into them")
        continue
    
    if player == door:
        print("You escaped!")
        break
    elif player == monster:
        print("You were eaten by the grue!")
        break
    

    # good move change players position
    # bad move dont change anything
    # if new player position is the door they win 
    # if the new player position is the monster they lose
    # otherwise continue
