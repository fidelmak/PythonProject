# file = open("/home/pf/PycharmProjects/PythonProject/handlingfiles/text.txt", mode="r")

# data = file.readline()

# print(data)
# file.close()



with open("/home/pf/PycharmProjects/PythonProject/handlingfiles/text.txt", mode="r") as file:
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)