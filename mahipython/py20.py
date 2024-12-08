
a = "Mahendra|"
for x in a:
    print(x)
# another way of writing the above program...
for x in "ONE|AND|ONLY":
    print(x)
# to avoid printing a new line everytime a print statement is called...
for x in a:
    print(x, end="")
