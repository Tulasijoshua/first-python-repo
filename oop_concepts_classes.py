class Instructor:
    def __init__(self, instructor_name, address):
        self.name=instructor_name
        self.address=address
        self.followers = 0

instructor_1 = Instructor("Joshua", "Kumasi", )

print(instructor_1.followers)

instructor_2 = Instructor("Tulasi", "Sunyani")

instructor_3 = Instructor("Emma", "Bekwai")
print(instructor_3.name, instructor_3.address)

instructor_4 = Instructor("Isaac", "Obuasi")
print(instructor_4.name)