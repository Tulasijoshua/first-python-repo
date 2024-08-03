class Instructor:
    followers = 0
    def __init__(self, instructor_name, instructor_address):
        self.name = instructor_name
        self.address = instructor_address
        # self.followers = 0
    def display(self, subject_name):
        print(f"Hello, I am {self.name} and I handle {subject_name}")
    def update_followers(self, follower_name):
        self.followers += 1

instructor_1 = Instructor("Joshua", "Sunyani")
print(f"{instructor_1.name} from {instructor_1.address} and has {instructor_1.followers} followers")
instructor_1.display("Python")
instructor_1.update_followers("Ali")
print(instructor_1.followers)

instructor_2 = Instructor("Emma", "Bekwai")
instructor_2.update_followers("Joshua")
print(instructor_2.followers)
