# This code is from an example in the
# TeamTreehouse Python Basics course. It was
# initially a shopping list, but I've changed
# it to a list of things to remember (per instructor
# suggestion).

# make a list to hold onto our items
remember_list = []

# This prints out the options for the user. I like the
# usage of triple quotes to contain ALL of the HELP messages
# in one block of text. NOTE that all of the text is left-aligned
# to prevent those tabs from being printed in the message to 
# the user.
def show_help():
    # print out instructions on how to use the app
    print("What should I remember?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
          """)

# This prints out the list    
def show_list():
    # print out the list
    print("Here's your list:")
    for item in remember_list:
        print(item)

# This adds members to the list
def add_to_list(new_item):
    # add new items to our list
    remember_list.append(new_item)
    # This is a cool line! I <3 these {} .format code snippets. I haven't 
    # encountered them before (only %d, %s).
    print("Added {}. List now has {} items.".format(new_item, len(remember_list)))
    
    
# help gets shown before the while loop starts. This is the only
# time that it gets called without the user initiating it. It should
# be called without the user requesting it because the user doesn't know
# how to use the program yet.
show_help()

# While True cycles through it's code FOREVER, unless stopped by break
while True:
    # ask for new items
    new_item = input("> ")
    
    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        # don't wanna add HELP to the list, so using continue
        continue
    elif new_item == 'SHOW':
        show_list()
        # don't wanna add HELP to the list, so using continue
        continue
    
    add_to_list(new_item)

show_list()
