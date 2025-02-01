class Human:
    def __init__(self, name, age):
        print("Calling init from Human")
        self.name = name
        self.age = age

    def showDetails(self):
        print(f"name: {self.name}, age: {self.age}")
    def eat(self):
        print("I can eat")

class Male(Human):
    def __init__(self, name, age, location):
        print("Calling init from Male")
        Human.__init__(self, name, age)
        self.location = location
    def sleep(self):
        print("I can sleep whole day")
class Female(Human):
    def __init__(self, name, age, can_dance):
        super().__init__(name, age)
        self.know_dance = can_dance
    def work(self):
        print("I can code")
    def showDetails_F(self):
        Human.showDetails(self)
        print(f"Know dancing: {self.know_dance}")

female_1 = Female("Joshua", 12, True)
print(female_1.age)
female_1.showDetails_F()

# male_1 = Male("Joshua", 12, "Sunyani")
# male_1.sleep()