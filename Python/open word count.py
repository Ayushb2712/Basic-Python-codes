fn=open("C:/a1.txt",'r')
a=fn.readlines()
for i in range(0,len(a)):
    b=a[i].split(" ")
print(len(b))


