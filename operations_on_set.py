set1 = {'Tulasi', 'Joshua', 'Mbawini', 'Syntactic Sugar'}
set2 = {'Emmanuel', 'Tulasi', 'Hottor', 'Holali'}
set3 = {'Isaac', 'Yeboah', 'Mawulolo'}

# UNION
# print(set1.union(set2))
# set2.union(set1)
# print(set1 | set2)
# print(set1.union(set2, set3))
# print(set1.union(('Ali', 'Mohammed')))
# set1.update(set2)
# set1.update(['Jed', 'Twist'])

# update using operator
# set1 |= set2
# print(set1)

# INTERSECTION
# print(set1.intersection(set2))
# print(set1.intersection(set2, set3))
# print(set1 & set2)
# print(set1.intersection(['Josh', 'Mohammed']))

set1.intersection_update(set2)
set2.intersection_update(['Kelly', 'Josh'])
# print(set1)
print(set2)