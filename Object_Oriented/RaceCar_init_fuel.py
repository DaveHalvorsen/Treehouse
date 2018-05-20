# The challenge prompt is:
# First, create a class named RaceCar. In the __init__ for the class, take arguments 
# for color and fuel_remaining. Be sure to set these as attributes on the instance.
# Also, use setattr to take any other keyword arguments that come in.

# The class is RaceCar
class RaceCar:
    # it's initialized with self, color, fuel_remaining, and kwargs
    # kwargs is a dicitonary by the way
    def __init__(self, color, fuel_remaining, **kwargs):
        # initializing color and fuel
        self.color = color
        self.fuel_remaining = fuel_remaining
        # setting attributes for the dictionary of kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
