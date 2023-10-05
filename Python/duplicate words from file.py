fn=open("C:/Users/ayush/Documents/p1.txt",'r')
b=fn.read().split()
l1=[]
for i in b:
    if i not in l1:
        l1.append(i)
        print(i,end=" ")
