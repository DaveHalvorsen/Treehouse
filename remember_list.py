# This code is based on an example from the
# TeamTreehouse Python Basics course. It was
# initially a shopping list, but I've changed
# it to a list of things to remember (per instructor
# suggestion).
# make a list to hold onto our items
remember_list = []

# print out instructions on how to use the app
print("What should I remember?")
print("Enter 'DONE' to stop adding items.")

while True:
    # ask for new items
    new_item = input("> ")
    
    # be able to quit the app
    if new_item == 'DONE':
        break

    # add new items to our list
    remember_list.append(new_item)

# print out the list
print("Here's your list:")
for item in remember_list:
    print(item)
