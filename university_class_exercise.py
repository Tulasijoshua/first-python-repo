class University:
    def __init__(self, name):
        self.name = name
    def showDetails(self):
        print(f"University name is {self.name}")
class Course(University):
    def __init__(self, uni_name, course_name):
        University.__init__(self, uni_name)
        self.course_name = course_name
    def showDetails(self):
        print(f"School is {self.name} and they offer {self.course_name}")
class Branch(University):
    def __init__(self, uni_name, branch_name):
        University.__init__(self, uni_name)
        self.branch_name = branch_name
    def showDetails(self):
        print(f"School is {self.name} and has a branch {self.branch_name}")
class Student(Course, Branch):
    def __init__(self, uni_name, course_name, branch_name, student_name):
        self.student_name = student_name
        Course.__init__(self, uni_name, course_name)
        Branch.__init__(self, uni_name, branch_name)

    def showDetails(self):
        print(f"My name is {self.student_name} and I attend {self.name}. I offer {self.course_name} at {self.branch_name}")
class Faculty(Branch):
    def __init__(self, uni_name, branch_name, faculty_name):
        Branch.__init__(self, uni_name, branch_name)
        self.faculty_name = faculty_name
    def showDetails(self):
        print(f"I attend {self.name} and I am in the faculty of {self.faculty_name} at {self.branch_name} branch")

student_1 = Student("UENR", "Python", "Dormaa", "Joshua")
student_1.showDetails()
faculty_1 = Faculty("UENR", "Dormaa", "Computer")
faculty_1.showDetails()