txt = "one"
a = txt.center(20)
print(a)
a = txt.center(20, "0")
print(a)
print(len(a))
a = txt.ljust(20, "*")
print(a, "only")
a = txt.rjust(20, "*")
print(a)