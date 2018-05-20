# The text of this code challenge is:
# Use the list.sort() method to make sure the slots list gets sorted 
# after an item is added. Only do this in the SortedInventory class.

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)
        
class SortedInventory(Inventory):
    
    
    def add_item(self, item):
        super().add_item(item)
        self.item=item
        self.slots.sort()
        pass
