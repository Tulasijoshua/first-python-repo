your_name = input("Enter your name: ")
other_name = input("Enter his or her name: ")

your_name = your_name.lower()
other_name = other_name.lower()

full_name = your_name + other_name
countTrue = 0
countLove = 0
countTrue += full_name.count("t")
countTrue += full_name.count("r")
countTrue += full_name.count("u")
countTrue += full_name.count("e")

countLove += full_name.count("l")
countLove += full_name.count("o")
countLove += full_name.count("v")
countLove += full_name.count("e")

print(countTrue)
print(countLove)

love_score = (str(countTrue) + str(countLove))
love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score} and you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score} and you are alright together")
else:
    print(f"Your love score is {love_score}")