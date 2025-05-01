seta = {1,2,3,4,5,6,7,8,9,9}


# to add a new element
seta.add(10)
# to remove an element
seta.remove(1)
# using discard to remove an element
seta.discard(2)

# performing mathematical operations

setb = {2,3,4,5,6,7,11,12,13,14,15,16,17,18,19,20}
seta.add(20)
# union
# setc = seta.union(setb)
setc = seta | setb # this also works as above 
# intersection

#setd = seta.intersection(setb)
# abother way to do intersection
setd= seta & setb
# difference
#sete = seta.difference(setb)
# another way to do difference
sete = seta - setb
# symmetric difference
setf = seta.symmetric_difference(setb)
# another way to do symmetric difference
setf = seta ^ setb
print("seta:", seta)
print("setb:", setb)
print("setc:", setc)
print("setd:", setd)
print("sete:", sete)        
print("setf:", setf)

# you cannot use indexing in sets