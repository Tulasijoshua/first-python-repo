# def add(a, *numbers):
#     c = 0
#     print(numbers)
#     print(a)
#     for i in numbers:
#         c += i
#     print(f"Sum is {c}")
#
# add(1, 2, 5)
# add(6, 5, 6)
# add(1, 2, 3, 4, 56, 8)

def info_person(*args, **kwargs ):
    for key, value in kwargs.items():
        print(key, value)
    print(args)
#
info_person(1, 2, name="Ram", age="30", dept="CSE")
info_person(1, 2, 3, name="Shyam", dept="CSE")

def multiply(*numbers):
    c = 1
    for i in numbers:
        c *= i
    print(c)

multiply(2, 3, -6, 8)
multiply(2, 5, 8, 9, 0, 6)