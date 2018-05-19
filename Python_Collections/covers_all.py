# This code takes a single set (topics) as an argument
# It returns the name of any courses (a list) where *ALL*
# of the topics of the supplied set are covered.
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

def covers_all(topics):
    # This creates an empty list
    all_courses = []
    # This for loop cycles through the list of keys and values
    # from the COURSES dictionary
    for keys, values in COURSES.items():
        # issuperset returns a Boolean for if a given set contains
        # the specified set (topics). If TRUE, the all_courses list
        # gets appended with the name of the class that the supplied lists reside within
        if values.issuperset(topics):
            all_courses.append(keys)
    return all_courses
