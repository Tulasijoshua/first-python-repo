numbers = input("Enter list of numbers separated by space: ")

numbers = numbers.split()
sum = 0
for i in numbers:
    sum += int(i)
else:
    length = len(numbers)
    height = sum/length
print("The average height is: " + round(height))

# height_list = input("Enter a list separated by space: ")
#
# height_list = height_list.split()
# count = 0
# for height in height_list:
#     count = count+1
# for i in range(count):
#     height_list[i] = int(height_list[i])
#
# total = 0
# for person in height_list:
#     total += person
# avg = total/count
# print(round(avg))