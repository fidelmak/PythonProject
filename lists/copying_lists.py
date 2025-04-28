original = [1, 2, 3]


# Shallow copy
shallow_copy = original.copy()
print("Original:", original)
print("Shallow Copy:", shallow_copy)
print()
# Deep copy (for nested lists)
import copy
nested = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested)
print("Original Nested:", nested)
print("Deep Copy Nested:", deep_copy)
