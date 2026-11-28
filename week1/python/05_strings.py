"""
P5 — Strings
Run: python 05_strings.py
"""

driver = "  Jaya Racer  "

# 1. Strings are sequences of characters
print("First character:", driver[0])
print("First five:", driver[:5])
print("Last five:", driver[-5:])
print("Length:", len(driver))

# 2. Common string methods return new strings
clean_name = driver.strip()
print("strip:", clean_name)
print("lower:", clean_name.lower())
print("upper:", clean_name.upper())
print("replace:", clean_name.replace("Racer", "Driver"))

# 3. Searching and checking
print("Contains Racer?", "Racer" in driver)
print("Starts with spaces?", driver.startswith("  "))

# 4. f-strings: insert values into readable text
speed = 142.567
lap = 3
print(f"Lap {lap}: speed = {speed:.2f} km/h")

# 5. Strings are immutable
message = "Trackmania"
# message[0] = "t"  # TypeError
message = "t" + message[1:]  # create a new string instead
print(message)

# Quick self-check:
# A. Extract "mania" from "Trackmania" using slicing.
# B. Make the string "  PYTHON  " lowercase and remove surrounding spaces.
# C. Print 3.14159 to exactly 3 decimal places using an f-string.
