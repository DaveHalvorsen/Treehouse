# This class will praise the 'name' attribute
class Student:
    name = "HAL9000"
    
    def praise(self):
        return "great job %s"%self.name
name = Student()
