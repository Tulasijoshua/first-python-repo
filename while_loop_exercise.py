number = int(input("enter 0 to quite: "))

sum = 0
while number != 0:
    sum += number
    number = int(input("enter 0 to quite: "))
else:
    print("In else block")
print(f'Sum of the numbers entered is: {sum} ')
