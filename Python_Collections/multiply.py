# a demonstration of *args
def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    return product
    
    
