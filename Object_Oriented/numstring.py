# This is the text of the code challenge:
# I need to you add __mul__ to NumString so we can multiply our number 
# string by a number. Go ahead and add __rmul__, too.

class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
         return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)
    
    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other
                         
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        self.value = self + other
        return self.value
    # __mul__ should return the correct value depending on if
    # the value is a float or an int
    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other
    
    def __rmul__(self, other):
        return self * other
        
