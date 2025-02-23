# Area of a square and area of a rectangle

shape = input("would you like to calculate the area of a square or the area of a rectangle: ")

if shape == "rectangle" :
    length = int(input("what is the length of your rectangle: "))
    width = int(input("what is the width of your rectangle: "))
    print (length*width, "is the area of your rectangle")

elif shape == "square" :
    length = int(input("what is the length of your square: "))
    width = int(input("what is the width of your square: "))
    print (length*width, "is the area of your square")

else :
    print("Error ,please try again")