# Starter code
items = [1,2,3,4,5]
try:
    item = items[6]
except Exception as e:
    print(e, " : reason is that Item does not exixt in the list")