list1 = input("Enter a list of numbers separated by space: ")

list1 = list1.split()
print(list1)


for i in range(len(list1)):
    list1[i] = int(list1[i])
maximum_number = 0
for i in list1:
    if i > maximum_number:
        maximum_number = i
print(f"The maximum number is: {maximum_number}")
