tuple1 = (2, 12, 56, 34, 3, 5, -1)

for i in tuple1:
    print(i)
    if i%6==0:
        print(i)
        break
    # else:
    #     print("There is no number divisible by 6 in this sequence!")
else:
    print("There is no number divisible by 6 in this sequence!")

print("Out of for/else!")

# Else will not be executed when there is a break