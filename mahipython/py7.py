d={'a':1, 'b':2, 'c':3, 'd':4}
print("Inital dictionary is: ",d)
key=input("Enter the key to be deleted :")
if key in d:
    del d[key]
    print("updated dictionary is ",d)
else:
    print("key not found")
