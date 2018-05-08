# This code accepts a string as input
# it checks the length of the string
# it does 1 of 3 things based on the
# length of the string input
def just_right(string):
    if len(string) < 5:
        return "Your string is too short"
    elif len(string) > 5:
        return "Your string is too long"
    else:
        return True
