# Demonstration of lists and the following methods: .insert(), .remove(), del
messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
# Your code goes below here
move_item = messy_list.pop(3)
messy_list.insert(0, move_item)
messy_list.remove("a")
messy_list.remove(False)
del messy_list[3]
