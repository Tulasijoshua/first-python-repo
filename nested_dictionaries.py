# student_data = {
#     "Ram": {"roll_no": 10, "age": 20, "course": "Python"},
#     "Mohan": {"roll_no": 20, "age": 22, "course": "Java"},
# }
#
# print(student_data["Ram"])
# print(student_data["Mohan"]["roll_no"])
# student_data["Mohan"]["phone"]=782732
# print(student_data["Mohan"])
# # del student_data["Mohan"]["phone"]
# print(student_data["Mohan"].pop("phone"))
# print(student_data["Mohan"])

# travel_data = {
#     "Gujrat": ["Dwarkadhish", "Somnath", "Statue of unity"],
#     "Rajasthan": ["Jaipur", "Udaipur"]
# }
#
# print(travel_data)


student_data = [
    {
        "Name": "Ram",
        "roll_no": 10,
        "age": 20,
        "course": "Python"
    },
    {
        "Name": "Mohan",
        "roll_no": 20,
        "age": 20,
        "course": "Java",
        "Phone_no": [8298298, 232213]
    },
]

def new_entry(name, roll, age, course):
    student_data.append({"Name": name, "roll_no": roll, "age": age, "course": course})

def new_dict(name, roll, age, course):
    new_std_data={}
    new_std_data["name"] = name
    new_std_data["roll"] = roll
    new_std_data["age"] = age
    new_std_data["course"] = course
    student_data.append(new_std_data)

new_dict("Joshua", 32, 23, "Python")


# new_entry("Shyam", 22, 18, "C++")
# new_entry("Tulasi", 75, 22, "C#")


print(student_data)
