a=[]
n=int(input("Enter number of elements "))
for i in range(0,n):
    b=int(input("Enter element :"))
    a.append(b)
a.sort()
a.reverse()
i=0
while a[i]==a[i+1]:
    i+=1;
print(a[i+1])
