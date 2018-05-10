
# This is a demonstration of creating a dictionary of # of counts for 
# words from a string input. The string is split into words with the split
# method. It drops everything with .lower to make capitalization issues
# less complicated. Then it uses for to cycle through the words and 
# either initiate the word in the dictionary OR +1 it.

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.
def word_count(string_argument):
    dictionary = dict()
    string_argument = string_argument.split(" ")
    for word in string_argument:
        word = word.lower()
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary
print(word_count("The been The The The The rumors of my death have been widely rumors rumors exaggerated."))
print(word_count("I do not like it Sam I Am"))
