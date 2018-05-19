# This code creates a small grid and places a monster, a player and
# an escape route on a grid.
import os
import random

# These are the possible locations for items to be
CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

# This will clear the screen and is OS-specific
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# This returns a RANDOM location for each item
def get_locations():
    return random.sample(CELLS, 3)

# This programs in how the player can move
def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y

# This interprets the move English language command into
# the physical movement on the plane.
def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves

# This prints out the map
def draw_map(player):
    print(" _"*5)
    tile = "|{}"
    
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)

# This is the programmatic structure of everything
def game_loop():
    monster, door, player = get_locations()
    playing = True
    # The screen gets cleared and redrawn with the current player location
    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)
        # This prints out location information and choices to the user
        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit")
        
        move = input("> ")
        move = move.upper()
        # This checks for valid moves and allows the user to quit
        if move == 'QUIT':
            print("\n ** See you next time! **\n")
            break
        if move in valid_moves:
            player = move_player(player, move)
            # if the player meets the monster, the player loses
            if player == monster:
                print("\n ** Oh no! The monster got you! Better luck next time! **\n")
                playing = False
            if player == door:
                print("\n ** You escaped! Congratulations! **\n")
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! **\n")
    else:
        if input("Play again? [Y/n] ").lower() != "n":
            game_loop()


clear_screen()
print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()
