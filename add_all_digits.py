numbers = input("Enter numbers of your choice: ")

# sum_digits = 0
#
# for i in numbers:
#     sum_digits+=int(i)
# print(sum_digits)
digits = sum(int(digit) for digit in str(numbers))
print(digits)