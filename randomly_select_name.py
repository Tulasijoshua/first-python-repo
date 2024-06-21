import random

names = input("Enter names separated by comma: ")
names = names.split(",")

print(names)
choose = random.randint(0, len(names))
print(f"{names[choose]} will pay the bill!")