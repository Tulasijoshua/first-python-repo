class Human:
    can_breadth = True
    def __init__(self, num_heart):
        print("Calling init from human class")
        self.nose = 1
        self.eyes = 2
        self.heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self, name):
        print("Calling init from male class")
        self.name = name
    def sleep(self):
        print("I can sleep")

class Boy(Male):
    def __init__(self, heart, name, can_dance):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.know_dancing = can_dance
    def work(self):
        Human.work(self)
        print("I can code")

boy_1 = Boy(1, "Joshua", True)
print(boy_1.know_dancing)
print(boy_1.name)
print(boy_1.can_breadth)
print(Boy.mro())