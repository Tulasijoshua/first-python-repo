class Human:
    def __init__(self):
        print("Calling init from Human")
        self.num_eyes=2
        self.num_nose=1
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male:
    def __init__(self,name):
        print("Calling init from Male")
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")
class Boy(Human, Male):
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can test")

boy_1 = Boy()
boy_1.work()
print(boy_1.num_nose)