age = 19

txt = "My name is Mahendra, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.950
myorder = "I want {} pieces of item {} for {} ruppees."
print(myorder.format(quantity, itemno, price))
myorder = "I want to pay {2} ruppees for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
