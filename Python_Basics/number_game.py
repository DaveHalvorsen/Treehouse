# This game taks the user with guessing the randomly 
# generated number. It uses randit to generate a random
# number between a and b (in this case a is 1 and b is 10).
import random

# generate a random number between 1 and 10
secret_num = random.randint(1, 10)

while True:
    # get a number guess from the player
    guess = int(input("Guess a number between 1 and 10: "))
    
    # compare guess to secret number
    if guess == secret_num:
        print("You got it! My number was {}".format(secret_num))
        break
    else:
        print("That's not it!")
