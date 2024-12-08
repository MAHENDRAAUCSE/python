d={'A':1, 'B':2, 'C':3}
str=input("Enter the key and value you want to enter separated by a whitespace :")
d.update({str.split()[0] : int(str.split()[1])})
print("updated dictionary is :",d)
