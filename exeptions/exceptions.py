def divide(a,b):
    return a/b

try:
    ans = divide(1,0)
except ZeroDivisionError as e:
    print( e, "we cannot divide by zero")
    print(e.__class__)

