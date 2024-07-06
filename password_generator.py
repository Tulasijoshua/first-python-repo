import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbools = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '_', '/']

print("Welcome to Password Generator")

num_letters = int(input("How many letters you want in your password?\n"))
num_symbols = int(input("How many symbols you want in your password?\n"))
num_numbers = int(input("How many numbers you want in your password?\n"))

password = ""
list_pass = []

# You can also concatenate list using +
for i in range(1, num_letters+1):
    char = random.choice(letters)
    password += char
    list_pass.append(char)

for i in range(1, num_symbols + 1):
    char = random.choice(symbools)
    password += char
    list_pass.append(char)

for i in range(1, num_numbers+1):
    char = random.choice(numbers)
    password += char
    list_pass.append(char)

# random.shuffle(password)
print(type(password))
random.shuffle(list_pass)

random_pass = ""
for i in list_pass:
    random_pass += i
print(list_pass)
print(random_pass)