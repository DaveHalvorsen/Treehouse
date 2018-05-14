# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.
def num_teachers(a):
    count = 0

    for key in a.keys():
        count += 1
    return count

def num_courses(a):
    count = 0
    for key in a.keys():
        for value in a[key]:
            count +=1
    return count
def courses(a):
    single_list = []
    for key in a.keys():
        for value in a[key]:
            single_list.append(value)
    return single_list
def most_courses(a):
    highest_teacher_name = ''
    max_count = 0
    current_count = 0
    for key in a.keys():
        for value in a[key]:
            current_count += 1
        if current_count > max_count:
            max_count = current_count
        else:
            pass
    current_count = 0
    for key in a.keys():
        for value in a[key]:
            current_count += 1
        if current_count == max_count:
            highest_teacher_name = key
        else:
            pass
    return highest_teacher_name
    # stats should return a list of lists where the first item in each inner list is the teacher's name 
    # and the second item is the number of courses that teacher has. For example, it might return: 
    # [["Kenneth Love", 5], ["Craig Dennis", 10]]
def stats(a):
    statslist = []
    for teacher, courses in a.items():
        total = 0
        for value in a.values():
            for course in value:
                total += 1
                statslist.append([teacher, total])
    return statslist
                             
                             

                

        
