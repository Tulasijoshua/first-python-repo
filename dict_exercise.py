student_marks = {
    "Jenny": 92,
    "Harry": 78,
    "Dimpy": 56,
    "Rahul": 41,
    "Aniket": 99,
    "Prem": 34,
}

student_grades = {}

for student in student_marks:
    if student_marks[student] < 90 >= 100:
        student_grades[student] = "A+"
    elif student_marks[student] > 80:
        student_grades[student] = "A"
    elif student_marks[student] > 70:
        student_grades[student] = "B+"
    elif student_marks[student] > 60:
        student_grades[student] = "B"
    elif student_marks[student] > 50:
        student_grades[student] = "C"
    elif student_marks[student] > 40:
        student_grades[student] = "D"
    elif student_marks[student] < 40 and student_marks[student] > 0:
        student_grades[student] = "F"
    else:
        print("Invalid grade!")

print(student_grades)