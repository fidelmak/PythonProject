# kwargs is a key value pair in function found in python 

def sumOfTax(**kwargs):
    sum =0
    for key, item in kwargs.items():
        sum += item
       
    print()
    return round(sum,2)
    # for item in kwargs:
    #     sum += kwargs[item]
    # return sum
print(sumOfTax(tax1=2, tax2=3, tax3=4.5678, tax4=5.78))
print(sumOfTax(tax1=2, tax2=3, tax3=4, tax4=5, tax5=6))
print(sumOfTax(tax1=2, tax2=3, tax3=4, tax4=5, tax5=6, tax6=7))