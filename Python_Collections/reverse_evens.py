# This is a demonstration of various list slicing methods
# Everything is self-explanatory EXCEPT reverse_evens
# reverse_evens starts at the last even index and jumps 
# back by evens (by 2) until it gets to the first even index
# last even # is found by getting length and subtracting 1 (
# to get index position) and then checking if that index is
# even. If it's even, then it's the starting position. If it's odd
# than it -1 is the last even position. Index end isn't given
# cause that's the beginning of the list. 
def first_4(iterable):
    return iterable[:4]
def first_and_last_4(iterable):
    first_four = iterable[:4]
    last_four = iterable[-4:]
    return first_four + last_four
def odds(iterable):
    return iterable[1::2]
def reverse_evens(iterable):
    iterable_length = len(iterable)
    iterable_index_position = iterable_length - 1
    if iterable_index_position % 2 == 0:
        last_even = iterable_index_position
    else:
        last_even = iterable_index_position -1
    return iterable[last_even::-2]

    
    
