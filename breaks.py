# This code challenge is from the TeamTreehouse 
# Python Basics course. The code prints out the 
# provided items (into loopy), BUT it will stop
# if "STOP" is provided. I've added the function 
# titled input_function; it accepts the input that
# is then funneled into the loopy function. The old
# exercise code only allowed for internal testing 
# whereas this lets you play with it. 

# loopy cycles throught he provided input items
def loopy(items):
    for item in items:
        # this commented out code was originally
        # how it worked, but I've moved that to 
        # the input_function
        # if item == "STOP":
            # break
        print(item)
        
# This function collects the inputs that are then funneled
# into the loopy function. 
def input_function():
    # creating an empty list
    items = []
    # running until break
    while True:
        new_input = input("What item do you want to add? ")
        # user input of "STOP" will break the function (end it). 
        if new_input == "STOP":
            break
        items.append(new_input)
    loopy(items)

# Here input_function is getting called, which will then call
# the loopy function with the created list. 
input_function()    
