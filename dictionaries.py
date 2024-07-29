phone_no = {
    'Ram': 1234,
    'Shyam': 3456,
    'Mohan': 8766,
}

# phone_no = dict({
#     'Ram': 112,
#     'Shyam': 3456,
#     'Mohan': 8766
# })

# phone_no = dict([('Ram', 432), ('Shyam', 3457), ('Mohan', 8976)])

# print(phone_no)
# print(phone_no['Ram'])

# print(phone_no)
# phone_no['Hadhav']= {1111, 2222, 3333}
# phone_no['Shyam']={'Shyam_Home': 5555, 'Shyam_work': 4444}
# print(phone_no['Shyam'])
# print(phone_no['Shyam']['Shyam_work'])
# print(phone_no.get('ram'))
# print(phone_no.get('Ram'))

data= {
    1: 'jenny',
    2: 'Ram',
    0: 'Mohan'
}

# print(data[0])
# del phone_no['Ram']
# print(phone_no.pop('Shyam'))
# print(phone_no.popitem())
# print(phone_no.clear())
# print(phone_no.keys())
# print(phone_no.values())
# print(phone_no.items())
# print(phone_no)

# phone_no2 = phone_no.copy()
# print(phone_no2)
print(len(phone_no))

for i in phone_no:
    # print(i)
    print(phone_no[i])