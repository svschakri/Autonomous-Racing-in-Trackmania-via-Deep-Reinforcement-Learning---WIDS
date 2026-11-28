"""
P8 — Mutability, references and copying
Run: python 08_mutability_references_copying.py
"""

# 1. Two names can refer to the same list (aliasing)
original = [10, 20, 30]
alias = original
alias.append(40)
print("Original after alias change:", original)
print("Are they the same object?", original is alias)

# 2. Assignment does not automatically copy a list
numbers = [1, 2, 3]
other_name = numbers
other_name[0] = 99
print("numbers:", numbers)

# 3. Make a shallow copy with copy() or slicing
numbers = [1, 2, 3]
copied = numbers.copy()
copied[0] = 99
print("Original:", numbers)
print("Copy:", copied)

# 4. Shallow-copy limitation: nested objects are still shared
grid = [[1, 2], [3, 4]]
grid_copy = grid.copy()
grid_copy[0][0] = 100
print("Original nested list:", grid)

# 5. Immutable values behave differently
x = 10
y = x
y = y + 5
print("x:", x, "y:", y)

# 6. is checks identity; == checks equality
a = [1, 2]
b = [1, 2]
print("a == b:", a == b)
print("a is b:", a is b)

# Quick self-check:
# A. Predict the output when a list is assigned to another variable and mutated.
# B. Copy a list so changing the copy does not change the original.
# C. Why does a shallow copy not fully separate nested lists?
