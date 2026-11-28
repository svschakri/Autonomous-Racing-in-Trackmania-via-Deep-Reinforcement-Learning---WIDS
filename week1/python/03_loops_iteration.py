"""
P3 — Loops and iteration
Run: python 03_loops_iteration.py
"""

# 1. for loop: visit each item in an iterable
speeds = [40, 55, 70, 65]
for speed in speeds:
    print("Speed:", speed)

# 2. range(start, stop, step): stop is excluded
for lap in range(1, 4):
    print("Lap", lap)

for number in range(10, 0, -2):
    print(number)

# 3. while loop: repeat while a condition remains True
battery = 3
while battery > 0:
    print("Battery:", battery)
    battery -= 1

# 4. break exits the loop; continue skips to the next iteration
for reading in [20, 25, -1, 30]:
    if reading == -1:
        print("Invalid reading; skipping")
        continue
    if reading > 24:
        print("Threshold reached; stopping")
        break
    print("Accepted:", reading)

# 5. Nested loops
for row in range(2):
    for column in range(3):
        print(f"({row}, {column})", end=" ")
    print()

# 6. pass is a placeholder that does nothing
for _ in range(2):
    pass

# 7. Iterating over a string
for character in "RACING":
    print(character)

# Quick self-check:
# A. How many times does range(2, 10, 2) run?
# B. Rewrite the battery example using a for loop.
# C. What happens if you forget battery -= 1?
