# def greet(name, subject, dept="CS"):
#     print(f"Hi {name}")
#     print(f"Do you teach {subject}?")
#     print(f"Are you from {dept} department?")
#
# greet("Joshua",  "Python", "ME")


def add(*numbers):
    c = 0
    for i in numbers:
        c = c + i
    print(f"Sum is {c}")
add(5, 7, 9)
add(1,2,3,4,5,6,7,8,9)