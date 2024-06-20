height = int(input("What is your height: "))

if height >= 3:
    print("Can ride")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay 150 cedis")
    elif age <= 18:
        print("Please pay 250 cedis")
    else:
        print("Please pay 500 cedis")
else:
    print("Can't ride")
print("Bye!")