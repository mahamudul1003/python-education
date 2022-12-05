"""
>> Set - Unchangeable, but we can remove items and add new items
"""
my_set = set()

a = {1, 2, 3, 4, 5, 6}
b = {4, 5, 6, 7, 8, 9}

# Union - Common + Uncommon
print(a | b)  # Shortcut -> shift + \ # Pipe / OR
print(a.union(b))

# Intersection - Common
print(a & b)
print(a.intersection(b))

# Difference
print(a - b)
print(a.difference(b))
