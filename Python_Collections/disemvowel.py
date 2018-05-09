# This program returns a version of the inputted word argument 
# with all vowels removed. It uses a for loop to cycler through 
# individual letters, comparing them to the vowels list, with
# .lower() and appends them to the new word_replacment that
# is then returned
def disemvowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_replacement = ''
    for letter in word:
        if letter.lower() in vowels:
            continue
        else:
            word_replacement += letter
    return word_replacement
