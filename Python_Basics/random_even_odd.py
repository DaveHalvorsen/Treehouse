# This program randomly selects #s between 1 and 99 and
# then it prints whether the #s are odd or even. The 
# program only does this 5 times.

import random

# start will drop by 1 each time the while is run (until it's falsey)
start = 5
# even# modulo(%) will always be 0, so 'not' that is 1. return of 1
# means that we have an even #
def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    return not num % 2

# random.randit picks random numbers and then .format
# is used to print out the number and its odd vs even
# status
while start:
    random_number = random.randint(1, 99)
    if even_odd(random_number):
        print("{} is even".format(random_number))
    else:
        print("{} is odd".format(random_number))
    start -=1
