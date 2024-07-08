from math import ceil

h = float(input("Enter the height of the area in meters: "))
w = float(input("Enter the weight of the area in meters: "))
coverage = 7
def area_of_paint(height, weight, cover):
    area = (height * weight)
    no_of_cans = area / cover
    no_of_cans = ceil(no_of_cans)
    print(f"You will need {no_of_cans} cans of paint.")

area_of_paint(height=h, weight=w, cover=coverage)