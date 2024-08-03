class Instructor:
    followers = 0
    def __init__(self, instructor_name, instructor_address):
        self.name = instructor_name
        self.address = instructor_address
        # self.followers = 0
    def display(self, subject_name):
        print(f"Hi, I am {self.name} and I teach {subject_name}")

instructor_1 = Instructor("Joshua", "Sunyani")
print(f"Name: {instructor_1.name}\nAddress: {instructor_1.address}\nFollowers: {instructor_1.followers}")
instructor_1.display("Python")
