fn=open("C:/a1.txt",'r')
a=fn.readlines()
for i in range(0,len(a)):
    b=a[i].split(" ")
count=0
for i in range(len(b)):
    count+=len(b[i])
print(count)
