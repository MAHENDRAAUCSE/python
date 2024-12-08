txt = "Hello Mahendra!"
mytable = txt.maketrans("H", "B")
print(mytable)
print(txt.translate(mytable)) 
mydict = {83:  80}
print(txt.translate(mydict))  
txt = "Good night Mahendra!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))
