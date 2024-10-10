# List to hold student information
student_info = []
for i in range(2):
    name = input("Enter student name: ")
    grades = input(f"Enter grades for {name} separated by comma: ").split(',')
    student_info.append({'name': name, 'grades': grades})


# Function to calculate GPA for each student
def get_student_gpa(student_info):
    results = []
    for student in student_info:
        name = student['name']
        grades = student['grades']

        total_grade_point = 0.0
        total_courses = len(grades)

        for grade in grades:
            if grade.strip() == 'A':  # Ensure to handle potential extra spaces
                grade_point = 4.0
            elif grade.strip() == 'B':
                grade_point = 3.5
            elif grade.strip() == 'C':
                grade_point = 3.0
            elif grade.strip() == 'D':
                grade_point = 2.5
            else:
                grade_point = 1.0  # If it's any other grade, assume 1.0

            total_grade_point += grade_point

        gpa = total_grade_point / total_courses

        results.append({'name': name, 'total_grade': gpa})

    return results


final_results = get_student_gpa(student_info)

# Output each student's GPA
for result in final_results:
    print(f"{result['name']}: GPA = {result['total_grade']:.2f}")
