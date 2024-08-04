class Human:
    def __init__(self, num_heart):
        print("Calling init from Human")
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("I can eat")
    # def work(self):
    #     print("I can work")

class Male:
    def __init__(self, name):
        print("Calling init from Male")
        self.name = name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")
class Boy(Human, Male):
    def __init__(self, name, language, heart):
        self.language = language
        Human.__init__(self, heart)
        Male.__init__(self, name)
    def sleep(self):
        print("I can sleep")
    def display(self):
        print(f"Hi, I am {self.name} and I work on the {self.language}")

boy_1 = Boy("Joshua", "Python", 1)
print(boy_1.num_nose)
print(boy_1.num_heart)
print(boy_1.language)
boy_1.display()