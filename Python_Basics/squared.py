# The code needs to produce the follwing:
# squared(5) would return 25
# squared("2") would return 4
# squared("tim") would return "timtimtim"

def squared(argument):
    # first int is used to make sure the supplied value is int-friendly
    # then it's squared
    try:
        argument = int(argument)
        return argument * argument
    # if the value can't be converted (cause it's text), then the whole
    # string is multiplied by the length
  
    except ValueError:
        length = len(argument)
        argument = argument * length
        return argument
        
