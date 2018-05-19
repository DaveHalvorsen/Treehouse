# This is a small scale demonstration of a game
# in which the player loses points for running
# into a wall

def move(player, direction):
    # player is a tuple of the current position and HP
    x, y, hp = player
    # direction is a tuple of the x and y position
    xx, yy = direction 
    # This is the logic train of when to -5 the points
    # -points happen whenever the player has exited the known 
    # limitation of the physical space
    if xx == -1 and x==0: 
        hp-=5              
    elif xx == 1 and x==9:
        hp-=5
    elif yy ==-1 and y==0:
        hp-=5
    elif yy == 1 and y==9:
        hp-=5  
    else:
        x+=xx
        y+=yy
    return x, y, hp
