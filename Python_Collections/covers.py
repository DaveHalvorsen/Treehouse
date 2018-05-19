# This is a dictionary of sets
COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}
# This function accepts a single parameter (set of topics)
# this function returns a list of courses from COURSES
# where the supplied set and the course's value overlap
covers({"Python"}) would return ["Python Basics"].
def covers(arg):
    # this holds the list that we'll build
    hold = []
    # this cycles through each key (and it's value) from COURSES
    # if the given value matches the supplied argument, then the 
    # hold list is appended with the value's key.
    for key, value in COURSES.items():
        if value & arg:
            hold.append(key)
    return hold
