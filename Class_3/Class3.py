# condtional statements
age = int(input("Enter your age: "))
if age >= 18:
    print(
        "You are eligible to vote"
    )  # identation is necessary for conditional statements or wherever you are defining a block of code

# print("this is not part of if statement so no need for indentation")

# if-else statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for the vote")
else:
    print("You are not eligible to vote")

# if else and elif statement
marks = 90
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Nested If statement
num = int(input("Enter a number: "))  # 10, -1
if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")

    num = 12

# [Conditions]
if num > 7:
    if num % 2 == 0:
        print(
            f"{num} number is greater than 5"
        )  # Use f"" when you need to include variables inside a string
    else:
        print(f"{num }Odd number is greater than 5")


is_adult = True
has_voter_id = False
if is_adult and has_voter_id:
    print("You are  eligible to vote")
else:
    print("You are NOT eligible to vote")


# Ternary Operator
# Shorthand way of writing the single if else statement
age = 30
message = "Adult" if age >= 18 else "Not Adult"
print(message)


# match-case statement
# Traffic Signal
color = input("Enter the color: ")
color = color.lower()
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Ready")
    case "green":
        print("go")
    case _:
        print("Invalid color")


# For Loop on list

fruits = ["Apple", "bananas", "Mango"]
for fruit in fruits:
    print(fruit)

# For Loop on string
fruits = "Apple"
for fruit in fruits:
    print(fruit)

# For Loop on Dictionary
fruits = {"Fruit": "Apple", "Car": "Suzuki", "City": "Tokyo"}
for key, value in fruits.items():
    print(f"{key}:{value}")

# range
for i in range(1, 11):  # 11 is not include in the output
    print(i)

# While Loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Run the loop infine times

while True:
    user_input = input("Enter the q letter to exit")
    if user_input == "q":
        print("Exit the loop")
        break

for i in range(10):
    if i == 5:
        continue
    print(i)

# Loop inside Loop
for i in range(3):
    for j in range(2):
        print(i, j)

        # (0,0) (0,1)
        # (1,0) (1,1)
        # (2,0) (2,1)

        # 3x2 matrix

for i in range(1, 6):  # outer loop
    for j in range(1, 11):  # inner loop
        print(f"{i} x {j} = {i * j}")
    print()

# Loop else statement
for i in range(5):
    print(i)
else:
    print("Loop completed")

# Search Functionality
num = [1, 2, 3, 4, 5]
search = 7

for nums in num:
    if nums == search:
        print(f"Found {search}")
        break
else:
    print(f"{search} number not found")


# Define Functions in Python Language
def greet():
    print("Hello, I am learning Python Language")


greet()


def greet(name):
    print(f"Hello, {name} is learning Python Language")


greet("Jonathan")


def display_info(name, age=31):
    print(f" Name:{name}, Age:{age}")


display_info(name="John", age=48)


def my_function():
    pass


result = my_function()
print(result)

# Arbitrary Arguments


def print_arg(*args):
    for arg in args:
        print(arg)


print_arg(1, 2, 3, 4, 5)


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{key}")


print_kwargs(name="Jacob", age=14)

# lambda Function
# One liner function
# difference between lamda and normal functions, lambda is for simple function doesnt includes complex functionality while def allows complex functionality

square = lambda x: x**2
print(square(5))  # x=5
