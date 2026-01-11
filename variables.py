# Day 2: 30 Days of python programming

first_name = "Manoj"
last_name = "Sangtani"

full_name = first_name + " " + last_name

country = "United States of America"
city = "Villa Park"

age = 44
year = 2026

is_married = True
is_true = True
is_light_on = True

x, y, z = 1, 2, 3

# Exercises: Level 2
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords


# -------------------------------
# Exercises: Level 2
# -------------------------------

# Check data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))

# Length of first name
print(len(first_name))

# Compare length of first name and last name
print(len(first_name) == len(last_name))
print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))

# Declare numbers
num_one = 5
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total, diff, product, division, remainder, exp, floor_division)

# Circle calculations
import math

radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

print(area_of_circle)
print(circum_of_circle)

# User input for radius
user_radius = float(input("Enter radius: "))
print(math.pi * user_radius ** 2)

# User input for personal info
user_first_name = input("Enter first name: ")
user_last_name = input("Enter last name: ")
user_country = input("Enter country: ")
user_age = int(input("Enter age: "))

# Python keywords
help('keywords')


  
