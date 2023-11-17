import random

rows = 4
cols = 3

def create_class_maps():
    stud = [
        "Stud1",
        "Stud2",
        "Stud3",
        "Stud5",    
        "Stud4",
        "Stud6",
        "Stud7",
        "Stud8",
        "Stud9",
        "Stud10"
    ]

    # Create the first map
    class_seating_map1 = create_class_map(stud)

    # Reset the list of students for the second map due to popping, refactor later
    stud = [
        "Stud1",
        "Stud2",
        "Stud3",
        "Stud5",    
        "Stud4",
        "Stud6",
        "Stud7",
        "Stud8",
        "Stud9",
        "Stud10"
    ]

    # Create the second map based on the first map
    class_seating_map2 = create_class_map(stud, avoid_adjacent=class_seating_map1)

    return class_seating_map1, class_seating_map2

def create_class_map(stud, avoid_adjacent=None):
    class_seating_map = [[0 for x in range(cols)] for x in range(rows)]

    for i in range(rows):
        prev_student = None  # Keep track of the previous student seated in the adjacent position

        for j in range(cols):
            if stud:
                # Ensure the randomly chosen student is different from the previous one and from the first map
                valid_students = [s for s in stud if s != prev_student and (avoid_adjacent is None or s not in avoid_adjacent[i])]
                random_student = random.choice(valid_students)

                class_seating_map[i][j] = random_student
                stud.pop(stud.index(random_student))
                prev_student = random_student 
            else:
                class_seating_map[i][j] = None

    return class_seating_map

map1, map2 = create_class_maps()

print("Map 1:")
for row in map1:
    print(row)

print("\nMap 2:")
for row in map2:
    print(row)
