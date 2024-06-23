tuple1 = (2, 56, 34, 3, 5, -1)

for i in tuple1:
    print(i)
    if i%6 == 0:
        break
    # else:
    #     print("There is no number divisible by 6 in this sequence")
    # if i == 5:
    #     break
else:
    print("There is no number divisible by 6 in this sequence")
    # print("Loop successfully completed and we are in else block now!!!")