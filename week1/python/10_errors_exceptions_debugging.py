"""
P10 — Errors, exceptions and debugging
Run: python 10_errors_exceptions_debugging.py
"""

# 1. Syntax errors: Python cannot parse the program.
# Example (commented out so this file can run):
# if True
#     print("Missing colon")

# 2. Runtime exceptions: an error occurs while the program runs.
# Uncomment one line at a time to observe the exception:
# print(10 / 0)       # ZeroDivisionError
# print(int("fast"))  # ValueError
# print([1, 2][5])    # IndexError

# 3. Handle a specific exception with try / except
user_input = "not-a-number"
try:
    speed = float(user_input)
    print("Speed:", speed)
except ValueError:
    print("Please enter a valid numeric speed.")

# 4. else runs only if no exception occurred
try:
    result = 100 / 4
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)

# 5. finally runs whether an exception happened or not
try:
    print("Attempting calculation...")
    value = 5 / 1
finally:
    print("Calculation attempt finished")

# 6. Debugging: inspect assumptions and intermediate values
speeds = [40, 50, 60]
total = sum(speeds)
count = len(speeds)
print("DEBUG total:", total)
print("DEBUG count:", count)
print("Average:", total / count)

# Quick self-check:
# A. Handle the case where a user enters text instead of a number.
# B. Handle division by zero without crashing.
# C. What information does a traceback provide?
