# This program cycles through the items
# in TILES and prints the items UNLESS
# the item == '||'; the double pipe character
# will result in a new line to be printed.
# To ensure that the single line print
# requests stay on 1 line, I've used the
# end parameter for the print command.
TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for item in TILES:
    if item == '||':
        print('\n')
    else:
        print(item, end ="")
