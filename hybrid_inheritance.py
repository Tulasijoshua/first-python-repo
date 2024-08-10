class A:
    def display(self):
        print("display from A class")
class B(A):
    def display(self):
        print("display from B class")
class C:
    def show(self):
        print("Hi from C class")
class D(B,C):
    def display(self):
        print("display from D class")
        # super().display()
        A.display(self)
        C.show(self)
d1 = D()
d1.display()