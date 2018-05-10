# This program takes a single_string as its input
# it returns the first half of that string lowercase
# and the second half of that string as uppercase.
def sillycase(single_string):
    string_length = len(single_string)
    print("string length: ")
    print(string_length)
    last_index = int(string_length -1)
    print("last index: ")
    print(last_index)
    middle_index = int(last_index / 2)
    print("middle index: ")
    print(middle_index)
    first_half = single_string[:(middle_index)].lower()
    second_half = single_string[(middle_index):].upper()
    single_string = first_half + second_half
    return single_string
print(sillycase('treehouse'))
