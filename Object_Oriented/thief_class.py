# The Thief class will randomly assign 'thief' status
import random

class Thief:
    sneaky = True
    
    # This randomly determines if the member is a thief
    def pickpocket(self):
        if self.sneaky:
            return bool(random.randint(0,1))
        return False
