sub_marks = input("Enter marks of 5 subjects separated by comma: ")
sub_marks = sub_marks.split(',')

total_grade_points = 0
grade = 0
def grade_point(i):
    if i >= 80:
        return 4.0
    elif i >= 75:
        return 3.5
    elif i >= 70:
        return 3.0
    elif i >= 65:
        return 2.5
    elif i >= 60:
        return 2.0
    elif i >= 55:
        return 1.5
    elif i >= 50:
        return 1
    else:
        return 0.5


total_credit_unit = len(sub_marks) * 3
if len(sub_marks) == 5:
    for i in sub_marks:
        grade_point_value = grade_point(int(i))
        total_grade_points += grade_point_value
    grade = (total_grade_points * 3)/total_credit_unit
    print(grade)
else:
    print("Subjects must be 5")