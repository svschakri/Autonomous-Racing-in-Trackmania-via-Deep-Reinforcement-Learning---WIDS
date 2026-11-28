"""
P2 — Conditional statements and Boolean logic
Run: python 02_conditionals_boolean_logic.py
"""

# 1. Comparisons produce Boolean values: True or False
speed = 145
speed_limit = 120

print("speed > speed_limit:", speed > speed_limit)
print("speed == speed_limit:", speed == speed_limit)
print("speed != speed_limit:", speed != speed_limit)

# 2. if / elif / else: exactly one matching branch is selected
if speed > speed_limit:
    print("Warning: overspeeding")
elif speed == speed_limit:
    print("At the speed limit")
else:
    print("Within the speed limit")

# 3. and, or, not combine or invert Boolean expressions
is_on_track = True
has_fuel = True
can_drive = is_on_track and has_fuel
print("Can drive:", can_drive)

if not is_on_track or not has_fuel:
    print("Stop the car")

# 4. Nested conditions
lap_time = 62.5
if is_on_track:
    if lap_time < 65:
        print("Good lap")
    else:
        print("Try to improve the lap")

# 5. Truth values: empty containers and zero are falsy
sensor_readings = []
if sensor_readings:
    print("Readings available")
else:
    print("No readings yet")

# 6. Common mistake: use == for comparison, = for assignment
# if speed = 100:  # SyntaxError — uncomment to see the error
#     print("This will not run")

# Quick self-check:
# A. What does (10 > 5) and (3 == 4) evaluate to?
# B. What is printed if speed is changed to 100?
# C. What is the difference between `if value:` and `if value is True:`?
