# This is a demonstration of the random.sample method
# The get_locations function will return 3 random choices from the
# cells iterable
import random

def get_locations(cells): 
    return random.sample(cells, 3)
