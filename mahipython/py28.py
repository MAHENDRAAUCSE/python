file=open('abc.txt','r')
print(file.read())
file.seek(0)
print(file.read(5))
