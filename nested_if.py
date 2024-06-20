height = int(input("What is your height: "))
bill = 0
if height >= 3:
    print("Can ride")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 150
        print("Please pay 150 cedis")
    elif age <= 18:
        bill = 250
        print("Please pay 250 cedis")
    else:
        bill = 500
        print("Please pay 500 cedis")

    want_photo = input("Do you want to take photo(Y/N)? ")
    if want_photo == 'y' or want_photo == 'Y':
        bill = bill + 50
    print(f"Your total bill is {bill}")
else:
    print("Can't ride")
print("Bye!")