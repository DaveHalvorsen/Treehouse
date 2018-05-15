# TeamTreehouse asked for a tuple of the different kinds of case settings possible
# it wouldn't accept the piecemeal tuple creation ... is that even a tuple? (the first # part)
# doing it all on the return line worked fine
def stringcases(single_string):
    #uppercase = tuple(list(single_string.upper())
    #lowercase = tuple(list(single_string.lower())
    #titlecase = tuple(list(single_string.title())
    #reverse = tuple(list(single_string[::-1]))
    #return(uppercase, lowercase, titlecase, reverse)
    return (single_string.upper(), single_string.lower(), single_string.title(), single_string[::-1])
    
