fn=open("C:/Users/ayush/Documents/p1.txt",'r')
k=int(input("Enter k"))
b=fn.read().split()
for i in b:
    if len(i)==k:
        print(i)
