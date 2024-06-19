maxYears = 90
maxWeeks = 52 * 90
maxMonths = 12 * 90
maxDays = 365 * 90
age = input("What is your age? ")
years_left = maxYears - int(age)
weeks_left = years_left * 52
months_left = years_left * 12
days_left = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")
