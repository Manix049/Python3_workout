my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

# to print alphabet at a particular index
print(my_string[-1])

# to check index of a particular alphaabet
print(my_string.index("B"))

# to check count of occurance of an alphabets
print(my_string.count("o"))

# uppercase
#print(my_string.upper()) # 1 way
v1=my_string.upper()
print(v1)  #2 way

# index at which word bitcoin starts
print(my_string.find("Bitcoin"))

#starts with
print(my_string.startswith("X"))

# swapcase
print(my_string.swapcase())
#remove all whitespace
print(my_string.replace(" ", ""))

#joins elements of list1 by '&' and stores in sting s
print("&".join(my_string))

