height = float(input("Enter your height in m: "))
weight = int(input("Enter weight in kg: "))

BMI = round(weight / height ** 2)

print(f"Your BMI is {BMI}")

if BMI < 16.0:
    print("You are underweight")
elif BMI <= 16.9:
    print("You're underweight (Moderate thinness")
elif BMI <= 18.4:
    print("You're underweight (Mild thinness")
elif BMI <= 24.9:
    print("You're in a normal range")
elif BMI <= 29.9:
    print("You're Overweight (Pre-obese)")
elif BMI <= 34.9:
    print("You're obese (Class I)")
elif BMI <= 39.9:
    print("You're obese (Class II)")
elif BMI >= 40:
    print("You're obese (Class III)")
else:
    print("Enter correct inputs")