# import my_module as m
# from my_module import calculator
# from my_module import calculator, a
# from my_module import *
import my_module

a, b = 4, 5

sum = a+b
print("Sum is :", sum)

print(my_module.calculator(3, 2))
print("Value of a from another module is :", my_module.a)