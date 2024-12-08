txt = "My name is Mahendra"
x = txt.encode()
print(x)
txt = 'h\te\tl\tl\t0'
x = txt.expandtabs(1)print(x)
txt = 'Demo'
print(txt.isidentifier())
print(txt.isprintable())
txt = "   "
print(txt.isspace())
myTuple = ("vignesh", "pranay", "me")
x = "#".join(myTuple)
print(x)
txt = "50"
print(txt.zfill(10))
txt = "Thank you for the music\nWelcome to the jungle"
print(txt.splitlines())
