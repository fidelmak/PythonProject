def sum(x,y):
    print(x+y)

# print(sum(2,3))
# lets try and pass the thrid argument


print()

# lets try and pass the thrid argument
def sumof(*args):
    sum  = 0
    for item in args:
        sum += item
    return sum
       
print(sumof(2,3,4))
print(sumof(2,3,4,5))
print(sumof(2,3,4,5,6))

