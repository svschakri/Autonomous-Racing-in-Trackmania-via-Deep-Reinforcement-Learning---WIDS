"""
P7 — Comprehensions
Run: python 07_comprehensions.py
"""

lap_times = [63.2, 61.8, 67.1, 60.9, 65.0]

# 1. Build a new list from an iterable
seconds = [round(time) for time in lap_times]
print("Rounded:", seconds)

# 2. Add a condition to filter values
fast_laps = [time for time in lap_times if time < 63]
print("Fast laps:", fast_laps)

# 3. Transform and filter in one comprehension
fast_laps_plus_one = [round(time + 1, 1) for time in lap_times if time < 63]
print("Adjusted fast laps:", fast_laps_plus_one)

# 4. Dictionary comprehension: create key-value pairs
lap_labels = {index + 1: time for index, time in enumerate(lap_times)}
print("Lap labels:", lap_labels)

# 5. Set comprehension: duplicates are removed
first_digits = {str(time)[0] for time in lap_times}
print("First digits:", first_digits)

# 6. Equivalent loop: use whichever is clearer
squared = []
for number in range(5):
    squared.append(number ** 2)
print("Squares:", squared)

# Quick self-check:
# A. Create a list of squares of even numbers from 1 to 10.
# B. Create a dictionary mapping each lap number to its lap time.
# C. When might a normal for loop be clearer than a comprehension?
