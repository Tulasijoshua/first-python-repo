class Human:
    def __init__(self, num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self, name, heart):
        super().__init__(heart)
        self.name = name
        self.heart = heart
    def flirt(self):
        print("I can flirt")
    def work(self):
        Human.work(self)
        print("I can code")
    def eat(self):
        super().eat()
        print("I can eat fufu")
    def display(self):
        print(f"Hi, I am {self.name} and I have {self.num_heart} heart.")

male_1 = Male("Tulasi", 1)
print(male_1.name)
male_1.work()
print(f"Male has {male_1.num_heart}")
male_1.display()