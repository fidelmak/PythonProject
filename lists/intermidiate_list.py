nums = [1, 2, 3, 4,6,3,2,1,4]
# Common methods
nums.append(5) 
print(nums)
nums.extend([6, 7])
print(nums)
nums.insert(0, 0)  
print(nums)
nums.remove(0)
print(nums)
nums.pop() # Remove last element
print(nums)
index_of_2= nums.index(3)  
print(index_of_2)
occurence_of_2= nums.count(2) # Count occurrences of 2
print(occurence_of_2)
sort_the_list = nums.sort()  
print(nums)
nums.reverse() 
print(nums)
new_list =nums.copy()  
print(new_list)
new_list.sort()
print(new_list)
nums.clear()  # Clear the list
print(nums)