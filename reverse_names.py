names = input("Enter 5 names separated by comma: ")
names = names.split(",")

if len(names) == 5:
    names.reverse()
    print(names)
else:
    print("Enter names of 5 people!!!")