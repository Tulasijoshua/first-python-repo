year = int(input("Enter year:  "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is s leap year")
        else:
            print(f"Not a leap year")
    else:
        print(f"The year {year} is a leap year")
else:
    print("Not a leap year")