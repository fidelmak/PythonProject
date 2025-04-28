numbers = [1, 2, 3, 4, 5]
print(numbers)
#length

print(len(numbers))  # 5
print()
# Iteration
for num in numbers:
    print(num)
print()
# With index
for index, num in enumerate(numbers):
    print(f"Index {index}: {num}")

for num in enumerate(numbers):
    print(num)