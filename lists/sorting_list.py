numbers = [3, 1, 4, 1, 5, 9, 2]

# Simple sort (in-place)

numbers.sort()  # [1, 1, 2, 3, 4, 5, 9]
print("Sorted numbers:", numbers)

# Sort with custom key
words = ['banana', 'pie', 'apple', 'cherry']
words.sort(key=len) 
print("Sorted words by length:", words)
print()
# Reverse sort
numbers.sort(reverse=True)
print("Reverse sorted numbers:", numbers)