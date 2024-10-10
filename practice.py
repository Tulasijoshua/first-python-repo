def compute_gpas(students_info):
    gpas = []

    # Grade points mapping (example: A = 4.0, B = 3.0, etc.)
    grade_points = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }

    for student in students_info:
        name = student['name']
        grades = student['grades']
        total_points = 0
        num_courses = len(grades)

        for grade in grades:
            total_points += grade_points.get(grade, 0)

        gpa = total_points / num_courses if num_courses > 0 else 0
        gpas.append({'name': name, 'gpa': gpa})

    return gpas


# Example usage
students_info = []

for i in range(3):
    name = input(f"Enter the name of student {i + 1}: ")
    grades = input(f"Enter the grades for {name} (separated by spaces, e.g., 'A B C'): ").split()
    students_info.append({'name': name, 'grades': grades})

gpas = compute_gpas(students_info)

for student in gpas:
    print(f"{student['name']}: GPA = {student['gpa']:.2f}")