"""
P4 — Core data structures
Run: python 04_core_data_structures.py
"""

# 1. Lists: ordered, mutable collections
lap_times = [63.2, 61.8, 62.5]
lap_times.append(60.9)
lap_times[0] = 64.0
print("List:", lap_times)
print("First lap:", lap_times[0])
print("Last two:", lap_times[-2:])

# Nested lists: a list containing other lists
track_sectors = [[20.1, 21.0], [19.8, 20.5]]
print("Second sector, first value:", track_sectors[1][0])

# 2. Tuples: ordered, immutable collections
track_dimensions = (1200, 800)
print("Width:", track_dimensions[0])
# track_dimensions[0] = 1000  # TypeError: tuples cannot be changed

# 3. Sets: unique elements; useful for membership tests
visited_checkpoints = {"A", "B", "A"}
visited_checkpoints.add("C")
print("Set:", visited_checkpoints)
print("Visited A?", "A" in visited_checkpoints)

# 4. Dictionaries: key-value mappings
car = {"speed": 150, "gear": 4, "on_track": True}
print("Speed:", car["speed"])
car["speed"] = 155
car["boost"] = False
print("Car:", car)
print("Missing key safely:", car.get("nitro", "unknown"))

# 5. Membership and length
print("Is 60.9 present?", 60.9 in lap_times)
print("Number of laps:", len(lap_times))

# 6. Mutability reminder: lists and dictionaries can be modified in place
# Tuples and strings cannot be modified in place.

# Quick self-check:
# A. Remove the slowest lap time from lap_times.
# B. Store three checkpoint names in a tuple.
# C. Count how many unique checkpoint names are in a list using a set.
