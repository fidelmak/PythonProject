import pandas as pd 
a = pd.DataFrame({'Animals': ['Dog','cat','lion'], 'sounds':['Barks','Neow','Roars']})
print(a)

print(a.describe())

b = pd.DataFrame({
    'letters': ['a','b','c','d'],
    'numbers': [1,2,3,4],
})

print(b.sort_values(by='numbers'))

b = b.assign(new_values = b['numbers']*3)
print(b)
