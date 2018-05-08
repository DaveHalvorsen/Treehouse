# program needs to print out items in 'items', UNLESS
# the item begins with the character 'a'

# standard function definition
def loopy(items):
    for item in items:
        # this selects individual item elements from items
        # and then does nothing (cause continue)
        if item[0] == 'a':
            continue
        # I keep forgetting to put print parenthesis! My
        # code failed at first because my line was print item
        print(item)
