d={'A':1, 'B':2, 'C':3}
key=input("Enter a key to check :")
if key in d.keys():
    print("key is present and the value of the key is :")
    print(d[key])
else:
    print("key is absent")
