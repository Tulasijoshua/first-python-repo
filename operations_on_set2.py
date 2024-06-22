set1 = {'Tulasi', 'Joshua', 'Mbawini', 'Syntactic Sugar'}
set2 = {'Emmanuel', 'Tulasi', 'Hottor', 'Holali'}
set3 = {'Isaac', 'Yeboah', 'Mawulolo'}

# DIFFERENCE
# print(set1.difference(set2))
# print(set1 - set2)
# print(set1.difference(('Josh', 'Jed')))
# print(set1.difference(set2, set3))
# set1.difference_update(set2)
# set2.difference_update(set1)
# print(set1)
# print(set2)

# SYMMETRIC DIFFERENCE
# It is not allowed for multiple sets
# print(set1.symmetric_difference((set2)))
# print(set1 ^ set2 ^ set3)
# allowed for multiple arguments

# set2.symmetric_difference_update(set1)
set1.symmetric_difference_update(('Josh', 'Emma'))
print(set2)
print(set1)