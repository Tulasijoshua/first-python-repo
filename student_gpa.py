name = input("Enter your name: ")
gpa = float(input("Enter your GPA: "))

def get_gpa(gpa):
    if gpa >= 3.6:
        return 'First class'
    elif gpa >= 3.0:
        return 'Second class upper'
    elif gpa >= 2.5:
        return 'Second class lower'
    elif gpa >= 2.0:
        return 'Third class'
    elif gpa >= 1.0:
        return 'Pass'
    else:
        return 'Failed'

print(f"{name} is in {get_gpa(gpa)}")
