exam_scores = input("Enter your exams scores for 3 courses separated by comma: ")
exam_scores = exam_scores.split(',')

def grade_point(scores):
    if scores >= 80:
        return 4.0
    elif scores >= 75:
        return 3.5
    elif scores >= 70:
        return 3.0
    elif scores >= 65:
        return 2.5
    elif scores >= 60:
        return 2.0
    elif scores >= 55:
        return 1.5
    elif scores >= 50:
        return 1.0
    else:
        return 0.5

total_grade_point = 0
total_credit_hours = 3 * len(exam_scores)
if len(exam_scores) == 3:
    for score in exam_scores:
        grade_point_value = grade_point(int(score))
        total_grade_point += grade_point_value
    GPA = (total_grade_point * 3) / total_credit_hours
    print(GPA)
else:
    print("Enter scores for 3 courses")