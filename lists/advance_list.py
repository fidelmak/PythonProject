# Basic comprehension

squares = [x**2 for x in range(1,11)]
print("Squares:", squares)

# With condition

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even Squares:", even_squares)

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened Matrix:", flattened)