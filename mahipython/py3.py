a=[]
n=int(input("Enter number of elements :"))
for i in range(n):
    b=int(input("Enter Element :"))
    a.append(b)
even=[]
odd=[]
for i in a:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("The even list is ",even)
print("The odd list is ",odd)
