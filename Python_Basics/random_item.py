# EXAMPLE
# random_item("Treehouse")
# The randomly selected number is 4.
# The return value would be "h"
import random
def random_item(argument):
    argument_length = len(argument)
    random_index = random.randint(0, argument_length-1)
    return argument[random_index]
