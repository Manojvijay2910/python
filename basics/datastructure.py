students = {'John' : ['Python', 'DJango', 'DRF'], 'Bob': ['Java', 'Spring'], 'Jim': ['Js', 'Node', 'React']}
keys = students.keys()

for key in keys:
    print("Courses taken by", key, " are: ")
    for course in students[key]:
        print(course)