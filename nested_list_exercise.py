list = [[1,2,3],[4,5,6],[7,8,9]]

position = input("Enter two digits separated by comma: ")
position_entered = position.split(",")
position_entered = position_entered
first = int(position_entered[0])
second = int(position_entered[1])

# entered = position[position_entered[0][1]]
list[first-1][second-1] = "X"
print(list)