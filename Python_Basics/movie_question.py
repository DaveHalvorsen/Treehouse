# This program asks you if you want to start the movie.
# if the user enters 'n' or 'N', the program exits 
# using sys.exit(). Otherwise, the program tells you
# to enjoy the show.

import sys
answer = input("Do you want to start the movie?")
if answer.lower() == 'n':
    sys.exit()
else:
    print("Enjoy the show!")
