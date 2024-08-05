class Human:
    def __init__(self, name, age):
        print("Calling init from human class")
        self.name = name
        self.age = age
    def showDetails(self):
        print(f"name: {self.name}, age: {self.age}")
    def eat(self):
        print("I can eat")
class Male(Human):
    def __init__(self, m_name, m_age, location):
        Human.__init__(self, m_name, m_age)
        self.location = location
    def sleep(self):
        print("I can sleep whole day.")
class Female(Human):
    def __init__(self, f_name, f_age, can_dance):
        print("Calling init from female class")
        super().__init__(f_name, f_age)
        self.know_dancing = can_dance
    def work(self):
        print("I can code")
    def showDetails_F(self):
        Human.showDetails(self)
        print(f"Know dancing: {self.know_dancing}")

female_1 = Female("Joshua", 21, True)
female_1.eat()
female_1.showDetails_F()
# male_1 = Male("Joshua", 32, "Kumasi")
# print(Male.mro())