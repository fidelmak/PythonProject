my_d ={
    1: "id",
    "country": "Nigeria",
    "language": "English",
    "name": "Paul FIdelis",
    "age": 30,
    "is_student": False,
}

print(my_d['name'] )
print(my_d['country'])
print(my_d['language'])
print(my_d[1])
print(my_d['age'])
print(my_d['is_student'])
print()

for key in my_d:
    print(key, ":", my_d[key])
print()

my_d['stack']= "python"
del my_d['age']
for key in my_d:
    print(key, ":", my_d[key])
print()

# to print both the keys and value together

for key , value in my_d.items():
    print(str(key), ":", value)
print()
