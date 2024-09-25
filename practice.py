year = int(input("Enter a year: "))
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                False
        else:
            return True
    else:
        return False

if leap_year(year):
    print(f"The year {year} is a leap year!")
else:
    print(f"The year {year} is not a leap year!!!")