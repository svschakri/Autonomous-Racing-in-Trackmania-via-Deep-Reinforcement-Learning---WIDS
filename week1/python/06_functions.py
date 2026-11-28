"""
P6 — Functions
Run: python 06_functions.py
"""

# 1. Define a function with def; call it using parentheses
def greet():
    print("Welcome to the track!")

greet()

# 2. Parameters receive values; return sends a result back
def average(values):
    return sum(values) / len(values)

times = [63.2, 61.8, 62.5]
mean_time = average(times)
print("Average lap:", mean_time)

# 3. Default arguments
def calculate_score(time, penalty=0):
    return time + penalty

print(calculate_score(60))
print(calculate_score(60, penalty=5))

# 4. Keyword arguments make calls explicit
def describe_car(name, speed, gear):
    print(f"{name}: {speed} km/h, gear {gear}")

describe_car(name="Falcon", speed=150, gear=4)

# 5. Local scope: a variable created inside a function is local
track_name = "Desert"

def show_track():
    track_name = "Forest"
    print("Inside:", track_name)

show_track()
print("Outside:", track_name)

# 6. *args collects extra positional arguments into a tuple
def total_distance(*distances):
    return sum(distances)

print("Total distance:", total_distance(100, 200, 150))

# 7. **kwargs collects extra keyword arguments into a dictionary
def show_settings(**settings):
    for key, value in settings.items():
        print(key, "=", value)

show_settings(steering=0.5, braking=0.2)

# Quick self-check:
# A. Write a function that converts km/h to m/s.
# B. Write a function with a default argument for the number of laps.
# C. What is the difference between print(result) and return result?
