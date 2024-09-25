sub_marks = input("Enter marks of 5 subjects separated by comma: ")
sub_marks = sub_marks.split(',')

total_grade_points = 0
grade = 0
total_credit_unit = len(sub_marks) * 3
if len(sub_marks) == 5:
    for i in sub_marks:
        if int(i) >= 80:
            i = 4.0
        elif int(i) >= 75:
            i = 3.5
        elif int(i) >= 70:
            i = 3.0
        elif int(i) >= 65:
            i = 2.5
        elif int(i) >= 60:
            i = 2.0
        elif int(i) >= 55:
            i = 1.5
        elif int(i) >= 50:
            i = 1
        else:
            i = 0.5

        total_grade_points += i
    grade = (total_grade_points * 3)/total_credit_unit
    print(grade)
else:
    print("Subjects must be 5")