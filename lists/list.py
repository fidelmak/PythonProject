# # this is a lesson on List 
# list1 = [2,3,4,5,6,7,8]
# list2 = [2,3,4,5,6,7,8]
# print(list1)
# print(list2)

# list1.append(9)
# print(list1)

# fruits =['appple', 'banana', 'orange']
# mixed = [1,'hello',3.14, True]
# print(mixed)
# print(fruits)

# fruits = ['apple', 'banana', 'cherry']


# # accessing lists 
# # INdexing start from 0
# print(fruits[0]) # apple
# print(fruits[-2])

# #negative indexing (starts from the end which is -1)

# #List Slicing 
# numbers = [0,1,2,3,4,5,6,7,8,9 ]
# # basic slicing [start:stop:step] , their is something about this slicing the start , will commence or count from index 0 and stop will commence at index 1

# print(numbers[2:5])

# # omitting start or stop 
# print(numbers[:3])
# print(numbers[7:])

# # step parameter [start:stop:step]
# print()
# print(numbers[::2]) # this is accomplished by index , 0,1,2, then 0,1,2 and so on 

# print(numbers[1::2]) # this is another aspect of indexing ., 1,2,3 then 1,2,3 and so on 

# print()
# # Reveresed a list 
# print(numbers[::-1])
# print(numbers[5::-2]) # this is another aspect of indexing ., 1,2,3 then 1,2,3 and so on

# print()
# print()

# modifying a List 

fruits = ['apple', 'banana', 'cherry']
# Change an element
fruits[1] = 'blueberry'
print(fruits)

# Add elements
fruits.append('orange')  # Add to end
print(fruits)
fruits.insert(1, 'mango')  # Insert at specific position 
print(fruits)
# Remove elements
fruits.remove('blueberry') 
print(fruits)
popped = fruits.pop(1)  # Remove by index and return it
print(popped)  # 'mango'
print(fruits) 