"""
P9 — Modules, imports and script execution
Run: python 09_modules_imports_script_execution.py
"""

# 1. Import a standard-library module
import math
print("Square root:", math.sqrt(81))
print("Pi:", math.pi)

# 2. Import selected names
from random import randint
print("Random integer:", randint(1, 6))

# 3. Give a module a shorter alias
import statistics as stats
lap_times = [63.2, 61.8, 62.5]
print("Mean lap time:", stats.mean(lap_times))

# 4. Create your own module:
# Put this in a separate file named racing_utils.py:
#
# def kmh_to_ms(speed):
#     return speed / 3.6
#
# Then, in another Python file in the same folder, write:
# import racing_utils
# print(racing_utils.kmh_to_ms(108))

# 5. __name__ is "__main__" when this file is run directly.
# When imported by another file, its __name__ is the module name.
def main():
    print("This code runs when the script is executed directly.")

if __name__ == "__main__":
    main()

# Quick self-check:
# A. Use math.ceil() and math.floor() on 4.7.
# B. Create a module with a function that calculates average speed.
# C. Why is the main guard useful when a file can be imported?
