# This is the text of the code challenge: 
# Create a function named combiner that takes a single argument, 
# which will be a list made up of strings and numbers.
# Return a single string that is a combination of all of the 
# strings in the list and then the sum of all of the numbers. 
# For example, with the input ["apple", 5.2, "dog", 8], combiner 
# would return "appledog13.2". Be sure to use isinstance to solve 
# this as I might try to trick you.


def combiner(list):
    # number and string are set to 0 and empty list
    num = 0
    str = []
    # the list will be cycled through
    for item in list:
        # if the item is an integer, then add it to the previous # setting
        if isinstance(item, int):
            num+= item
        # same as int, but with float
        elif isinstance(item, float):
            num += item
        # if the item ISN'T a number, then it's a string
        # append the item to the previous string
        else:
            str.append(item)
    # we have a number and a string, which can't be directly joined
    # the formatting method is used to join the string and the number
    return "{}{}".format("".join(str), num)
