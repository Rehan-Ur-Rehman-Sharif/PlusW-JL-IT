first_name = input("enter first name: ")
last_name = input("enter last name: ")

print("My Name is", first_name, last_name)

total_letters = len(first_name) + len(last_name)

print(f"First name (upper): {first_name.upper()}")
print(f"Last name (lower): {last_name.lower()}")
print("Sum of letters in first and last name:", total_letters)

print("Calculate the area of following shapes:")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")
shape = input("Find the area of : ")
if shape == 1:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.142 * radius**2
    print("area of circle is", area)
if shape == 2:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    print("area of rectangle is", area)
if shape == 3:
    side = float(input("Enter the side of the square: "))
    area = side**2
    print("area of square is", area)
if shape == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("area of triangle is", area)
else:
    print("Invalid shape")


import random

colors = ["red", "blue", "green", "yellow", "orange", "purple"]

index = random.randint(0, len(colors) - 1)

selected_color = colors[index]

password = selected_color[::-1]
print("Color:", selected_color)
print("Reversed Password:", password)
