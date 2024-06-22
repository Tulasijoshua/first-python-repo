import random

names = input("Enter names separated by comma: ")
names = names.split(",")

print(names)
length = len(names)
choose = random.randint(0, length - 1)
print(f"{names[choose]} will pay the bill!")

# person_selected = random.choice(names)
# print(f"{person_selected} will pay the bill")