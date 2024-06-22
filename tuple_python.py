# Tuples are unchangeable (immutable)
tuple1 = (12, 6, -8, 'Joshua', True, 6, 12)

# tuple2 = (45,)
# print(type(tuple2))

# print(tuple1)
# print(tuple1[1:4])
# print(tuple1[::2])
# print(len(tuple1))

tuple3 = (45, 67, 90)
tuple4 = (tuple1, tuple3)
# print(tuple4)

tuple5 = tuple1 + tuple3
# print(tuple5)
# print(min(tuple3))

# print(tuple1.count(12))
# print(tuple1.index(12))

list1 = [1,2,3,4,5]
# print(tuple(list1))

tuple6 = (10,)*5
print(tuple6)
