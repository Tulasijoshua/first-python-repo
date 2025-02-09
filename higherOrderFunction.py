# def greet_louder(name):
#     print(f"Hi, {name.upper()}")
# def greet_softer(name):
#     print(f"Hi {name.lower()}")
# def hello(other_def_func, name1):
#     print("This is display() function")
#     other_def_func(name1)
# hello(greet_louder, "Joshua")
# hello(greet_softer, "JOSHUA")

# def hello(name):
#     print("hello has bee executed.")
#     def greet():
#         print("Hare Krishna")
#     def welcome():
#         print("Jai Shree Ram")
#     if name=="Joshua":
#         return greet
#     else:
#         return welcome
# new_func = hello("Joshua Tulasi")
# new_func()

def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x, y):
    return x/y

def calculate(num, x, y):
    print(num(x, y))

calculate(add, 2, 3)