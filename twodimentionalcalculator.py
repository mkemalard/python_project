# TWO-DIMENTIONAL CALCULATOR
# This calculator can calculate the area and perimeter of a square, triangle, circle, or trapezoid based on variables inputted by the user. In addition, this calculator can also calculate the Pythagorean theorem.

# TWO-DIMENTIONAL CALCULATOR
import math

question = input("What do you want to know?(area/perimeter/phytagoras): ")

while question != "area" and question != "perimeter" and question != "phytagoras":
    print("Sorry for the inconvenience. We are still working on it!")
    print("or may be there are some typo")
    question = input("What do you want to know?(area/perimeter/phytagoras): ")

# AREA CALCULATION 
if question == "area":
    shape_list = print("rectangle, circle, triangle, trapezoid, parallelogram ")
    shape = input("Choose the shape: ")  
    while shape != "rectangle" and shape != "circle" and shape != "triangle" and shape != "trapezoid" and shape != "parallelogram":
        print("Sorry for the inconvenience. We still working on it")
        print("or maybe there are some typo")
        print("rectangle, circle, triangle, trapezoid, parallelogram ")
        shape = input("Choose the shape: ")
    if shape == "rectangle":
        length = float(input("Insert the length: "))
        width = float(input("Insert the width: "))
        area_rectangle = length * width
        print(f"the area of the rectangle is:  {round(area_rectangle,4)}")
    elif shape == "circle":
        radius = float(input("Insert the radius: "))
        area_circle = math.pi * pow(radius, 2)
        print(f"The are of the circle is: {round(area_circle,4)}")
    elif shape == "triangle":
        base = float(input("Insert the base: "))
        height = float(input("Insert the height: "))
        area_triangle = 1/2 * base * height
        print(f"The area of the triagle is: {round(area_triangle,4)}")
    elif shape == "trapezoid":
        a = float(input("Insert value a: "))
        b = float(input("Insert value b: "))
        height = float(input("Insert height: "))
        area_trapezoid = ((a+b) * height)/2
        print(f"The area of the trapezoid is: {round(area_trapezoid,4)}")
    elif shape == "parallelogram":
        height = float(input("Insert the height: "))
        base = float(input("Insert the base: "))
        area_parallelogram = height * base
        print(f"The area of the parallelogram is: {round(area_parallelogram,4)}")


# PERIMETER CALCULATION
elif question == "perimeter":
    shape_list = print("rectangle, circle, triangle, trapezoid, parallelogram ")
    shape = input("Choose the shape: ")
    while shape != "rectangle" and shape != "circle" and shape != "triangle" and shape != "trapezoid" and shape != "parallelogram":
        print("Sorry for the inconvenience. We still working on it")
        print("or maybe there are some typo")
        print("rectangle, circle, triangle, trapezoid, parallelogram ")
        shape = input("Choose the shape: ")
    if shape == "rectangle":
        length = float(input("Insert the length: "))
        width = float(input("Insert the width: "))
        perimeter_rectangle = 2* (length + width)
        print(f"the area of the rectangle is:  {round(perimeter_rectangle,4)}")
    elif shape == "circle":
        radius = float(input("Insert the radius: "))
        perimeter_circle = 2 * math.pi * radius
        print(f"The are of the circle is: {round(perimeter_circle,4)}")
    elif shape == "triangle":
        a = float(input("Insert value a: "))
        b = float(input("Insert value b: "))
        c = float(input("Insert value c: "))
        perimeter_triangle = a + b + c
        print(f"The area of the triagle is: {round(perimeter_triangle,4)}")
    elif shape == "trapezoid" or shape == "parallelogram":
        print("The perimeter is sum of all sides :)")


# PHYTAGORAS CALCULATION
elif question == "phytagoras":
    side = input("Which side you want to know? (a/b/c): ")
    while side != "a" and side != "b" and side != "c":
        print("You enter the wrong variable!")
        side = input("Which side you want to know? (a/b/c): ")
    if side == "a":
        a_b = float(input("Insert side b: "))
        a_c = float(input("Insert side c: "))
        side_a = math.sqrt(pow(a_c,2) - pow(a_b,2))
        print(f"The value of a is: {side_a}")
    elif side == "b":
        b_a = float(input("Insert side a: "))
        b_c = float(input("Insert side c: "))
        side_b = math.sqrt(pow(b_c,2) - pow(b_a,2))
        print(f"The value of b is: {side_b}")
    elif side == "c":
        c_a = float(input("Insert side a: "))
        c_b = float(input("Insert side b: "))
        side_c = math.sqrt(pow(c_a,2) + pow(c_b,2))
        print(f"The value of c is: {side_c}")    




        






