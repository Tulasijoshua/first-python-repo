pizza_size = input("Enter the  size of pizza you want(S/M/L): ")
price = 0
pepperoni = 0
extraCheese = 20

if pizza_size == "S" or pizza_size == "s":
    price = 100
    pepperoni = 30
elif pizza_size == "M" or pizza_size == "m":
    price = 150
    pepperoni = 50
elif pizza_size == "Large" or pizza_size == "l":
    price = 200
    pepperoni = 50
else:
    print("Please enter the correct size!")

want_pepperoni = input("Do you want pepperoni(Y/N)? ")
want_extraCheese = input("Do you want extra cheese(Y/N)? ")

if (want_pepperoni == "y" or want_pepperoni == "Y") and (want_extraCheese == "y" or want_extraCheese == "Y"):
    totalPrice = price + pepperoni + extraCheese
elif (want_pepperoni == "y" or want_pepperoni == "Y"):
    totalPrice = price + pepperoni
elif (want_extraCheese == "y" or want_extraCheese == "Y"):
    totalPrice = price + extraCheese
else:
    totalPrice = price

print(f"Your final bill is {totalPrice}")
print("Thank you!")
