txt = "I can do this python all day"
x = txt.partition("python")
print(x)
txt = "I can do this python all day"
x = txt.partition("java")
print(x)
txt = "I can do this python all day, python is my favorite language"
x = txt.rpartition("python")
print(x)
