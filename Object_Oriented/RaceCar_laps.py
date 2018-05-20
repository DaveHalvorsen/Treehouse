# This is the code challenge text for this exercise:
# OK, now let's add a method named run_lap. It'll take a length argument. 
# It should reduce the fuel_remaining attribute by length multiplied by 0.125.
# Oh, and add a laps attribute to the class, set to 0, and increment it each time the run_lap method is called.

class RaceCar:
    def __init__(self,color,fuel_remaining,**kwargs):
        self.color=color
        self.fuel_remaining=fuel_remaining
        self.laps = 0
        
        for key,value in kwargs.items():
            setattr(self,key,value)
    # the run_lap method determines the remaining fuel after running laps
    # AND it bumps up the lap # based on how many times it's been called
    def run_lap(self, length):
        self.fuel_remaining -= length * 0.125
        self.laps = self.laps+1
