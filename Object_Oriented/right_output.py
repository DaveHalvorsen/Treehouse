# This is the text of the code challenge:
# I want you to add a __str__ method to the Letter class that loops 
# through the pattern attribute of an instance and returns "dot" for 
# every "." (period) and "dash" for every "_" (underscore). Join them 
# with a hyphen. I've included an S class as an example (I'll generate 
# the others when I test your code) and it's __str__ output should 
# be "dot-dot-dot".

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
    # This is the magic string method that I was asked to produce
    def __str__(self):
        # This list gets appended by the for logic
        hyphen_code = []
        for i in self.pattern:
            # a '.' will produce a "dot"
            if i == '.':
                hyphen_code.append("dot")
            # a '_' will produce a "dash"
            elif i == '_':
                hyphen_code.append("dash")
        # The return statement is joined with "-"
        return "-".join(hyphen_code)

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)
