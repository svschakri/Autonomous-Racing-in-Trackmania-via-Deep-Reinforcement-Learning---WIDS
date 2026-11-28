"""
WIDS — Week 1: Python Fundamentals
Topic: Variables and Data Types

Purpose
-------
This file is a guided demonstration, not a worksheet.
Run it from top to bottom, change the values, and observe how Python behaves.

Suggested command:
    python variables_and_datatypes.py

Learning goals
--------------
By the end, you should be able to:
1. Create variables and understand assignment.
2. Recognise the basic built-in data types.
3. Inspect values using type().
4. Convert between common types.
5. Understand the difference between = and ==.
6. Use input() and understand that it returns a string.
"""

# ============================================================
# 1. VARIABLES AND ASSIGNMENT
# ============================================================

# A variable is a name that refers to an object/value.
# The assignment operator (=) binds the name on the left to
# the value/expression on the right.

student_name = "Alex"
age = 19
height_in_metres = 1.72

print("Student:", student_name)
print("Age:", age)
print("Height:", height_in_metres)

# Python is dynamically typed: you do not declare the type
# of a variable before assigning a value.
value = 10
print("\nvalue =", value, "| type:", type(value))

value = "now I am a string"
print("value =", value, "| type:", type(value))

# Multiple assignment
x, y, z = 10, 20, 30
print("\nMultiple assignment:", x, y, z)

# Assigning the same value to multiple names
first_score = second_score = 0
print("Initial scores:", first_score, second_score)


# ============================================================
# 2. IDENTIFIERS AND NAMING
# ============================================================

# Valid names are case-sensitive and cannot start with a digit.
# Use descriptive snake_case names for ordinary variables.

lap_time_seconds = 52.8
number_of_attempts = 3

print("\nLap time:", lap_time_seconds)
print("Attempts:", number_of_attempts)

# These are different names:
speed = 100
Speed = 120
print("\nspeed:", speed)
print("Speed:", Speed)

# Examples of invalid names (kept as comments):
# 2nd_lap = 52.0       # Cannot start with a digit
# lap-time = 52.0      # Hyphens are not allowed in identifiers
# class = "Python"     # 'class' is a reserved keyword


# ============================================================
# 3. BASIC BUILT-IN DATA TYPES
# ============================================================

# int: whole numbers
laps_completed = 4
temperature = -5

# float: numbers with a fractional component
top_speed = 243.75
fuel_level = 0.5

# str: text
track_name = "Coastal Run"
message = 'The race has started!'

# bool: logical truth values (True or False)
is_finished = False
has_checkpoint = True

# NoneType: represents the absence of a value
best_lap_time = None

examples = [
    ("integer", laps_completed),
    ("float", top_speed),
    ("string", track_name),
    ("boolean", is_finished),
    ("None", best_lap_time),
]

print("\nBasic data types:")
for label, item in examples:
    print(f"{label:10} -> {item!r:20} type: {type(item).__name__}")


# ============================================================
# 4. OPERATIONS AND EXPRESSIONS
# ============================================================

a = 17
b = 5

print("\nInteger arithmetic:")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division: result is a float
print("a // b =", a // b) # Floor division
print("a % b =", a % b)   # Remainder
print("a ** b =", a ** b) # Exponentiation

# The + operator behaves differently for strings.
given_name = "Ada"
family_name = "Lovelace"
full_name = given_name + " " + family_name
print("\nString concatenation:", full_name)

# f-strings insert values into formatted text.
lap_time = 51.237
print(f"Formatted lap time: {lap_time:.2f} seconds")


# ============================================================
# 5. TYPE INSPECTION
# ============================================================

score = 95
print("\nType inspection:")
print(type(score))
print(isinstance(score, int))
print(isinstance(score, (int, float)))


# ============================================================
# 6. TYPE CONVERSION (CASTING)
# ============================================================

# Explicit conversion creates a value of another type.
number_as_text = "42"
number_as_integer = int(number_as_text)
number_as_float = float(number_as_text)
integer_as_text = str(number_as_integer)

print("\nType conversion:")
print(number_as_text, type(number_as_text).__name__)
print(number_as_integer, type(number_as_integer).__name__)
print(number_as_float, type(number_as_float).__name__)
print(integer_as_text, type(integer_as_text).__name__)

# Be careful: not every string can be converted to a number.
# int("hello") would raise a ValueError.
decimal_text = "3.14"
decimal_value = float(decimal_text)
print("Converted decimal:", decimal_value)

# int() applied to a float truncates the fractional part;
# it does not round to the nearest integer.
print("int(7.9) =", int(7.9))


# ============================================================
# 7. INPUT AND OUTPUT
# ============================================================

# input() always returns a string.
# Uncomment these lines when running interactively:
#
# user_name = input("Enter your name: ")
# user_age_text = input("Enter your age: ")
# user_age = int(user_age_text)
# print(f"Hello, {user_name}. Next year you will be {user_age + 1}.")
#
# If the user enters non-numeric text for age, int() raises
# ValueError. We will study exception handling in a later topic.


# ============================================================
# 8. COMMON BEGINNER PITFALLS
# ============================================================

# '=' means assignment.
# '==' means comparison.
target_speed = 200
is_at_target = (target_speed == 200)
print("\nAssignment vs comparison:")
print("target_speed =", target_speed)
print("target_speed == 200 ->", is_at_target)

# Combining a string and an integer directly with + is invalid.
# print("Age: " + 19)  # TypeError
print("Age: " + str(19))  # Convert the integer to a string first.

# Variable names are case-sensitive.
lap_count = 2
Lap_count = 5
print("lap_count:", lap_count, "| Lap_count:", Lap_count)


# ============================================================
# 9. QUICK SELF-CHECK — TRY BEFORE LOOKING ANYTHING UP
# ============================================================

# 1. Create variables for a Trackmania player's name, current
#    speed, number of completed laps, and whether the race ended.
#
# 2. Print each value and its type.
#
# 3. Store the string "120" in a variable. Convert it to an
#    integer, add 30, and print the result.
#
# 4. Ask the user for a lap time (as text), convert it to float,
#    and print it rounded to two decimal places.
#
# 5. Predict the output before running:
#       a = 8
#       b = 3
#       print(a / b)
#       print(a // b)
#       print(a % b)
#
# Try writing your answers in a separate file rather than
# changing the demonstration code above.
