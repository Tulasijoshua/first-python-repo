names = input('Enter names separated by comma: ')
names = names.split(",")

if len(names) == 5:
    names.reverse()
    print(names)
elif len(names) < 5:
    print('Names are not up to 5')
elif len(names) > 5:
    print('Names exceeds 5')
else:
    print('Enter name')

# for i in range(1, 50):
#     if i % 2 == 0:
#         print(i)

# names = [input(f"Enter name {i+1}: ") for i in range(5)]
#
# # Printing the list in reverse order
# print("Names in reverse order:", names[::-1])