# create a new file called: week11_day1.py
# ----------------------------------------
# Day 2 Review Activity: My Personal Info Generator
# ----------------------------------------

print(" Welcome to the Python Review Activity!")
print("You’ll review variables, strings, numbers, and print formatting.\n")

# Step 1: Create Variables
# TODO: Replace the values below with your own info
first_name = "Logan"
age = 16
favorite_color = "Black"
favorite_number = 21 

#  Step 2: Practice String Operations
# 1. Print your name in uppercase

print(first_name.upper())

# 2. Print how many letters are in your name

print(len(first_name))

# 3. Combine your name and favorite color into one message

print("My name is Logan and my favorite number is 21")
print("My name is " + str(first_name) + " and my favorite number is " + str(favorite_number))

#  Step 3: Math Practice
# Use arithmetic operators with your favorite number

add_result = 7 + 7 + 7
print(str(add_result) + " is my favorite number!")

#  Step 4: User Input Practice
# Ask the user two questions and combine answers

hobby = input("What is your favorite hobby? ")
city = input("Which city do you live in? ")
print(f"Wow! I didn’t know someone who likes {hobby} lives in {city}.")

# ⚙️ Step 5: Final Challenge (combine it all)
# Use math and strings together

next_year_age = age + 1
print(f"Next year, {first_name} will be {next_year_age} years old and still love the color {favorite_color}!")
print(f"If you add your favorite number {favorite_number} to your age {age}, you get {favorite_number + age}!")
