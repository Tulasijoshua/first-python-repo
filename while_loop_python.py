

# Sentinel value : A value used to terminate a loop we don't know how many times it will execute
# count = 5
# while count > 0:
#     print(count)
#     count -= 1
#     if count == 3:
#         break
# else:
#     print("In else block")
# print("out from loop")

# number = int(input("Enter a number(-1 to quit): "))
# while number != -1:
#     print(number)
#     number = int(input("Enter a number(-1 to quit"))
# else:
#     print("In else block")

count1 = 0
while True:
    print(count1)
    count1 += 1
    if count1 == 5:
        break
else:
    print("In else block")
print("Out from loop")