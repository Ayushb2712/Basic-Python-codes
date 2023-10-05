#program to retrieve a kth column
a=int(input("enter column number "))
b=eval(input())
c=[]
z=int(a-1)
for ii in range(len(b)):
    c.append(b[ii][z])
print(c)
    
