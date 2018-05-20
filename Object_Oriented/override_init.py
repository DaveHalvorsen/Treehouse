# Here's the text of the code challenge:
# Our Student class is coming along nicely! I'd like to be able to set the name 
# attribute at the same time that I create an instance. Can you add the code for 
# doing that? Remember, you'll need to override the init method. 

# The code needs to override the init method
class Student:
    name = "Your Name"
    # init initializes the initial state
    # **kwargs collects all the keyword arguments in a dictionary
    # It's not mentioned here, but for my own information:
    # *args collects all the positional arguments in a tuple
    def __init__ (self, name, **kwargs):
      # 'self' refers to the newly created object
    	self.name = name

    	for key, value in kwargs.items():
        	setattr(self, key, value)
            
    
    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()
