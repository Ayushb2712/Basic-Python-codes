fn=open("C:/Users/ayush/Documents/p1.txt",'r')
b=fn.read().split()
d1={}
for i in b:
    if i.isalpha():
        d1[i[0]]=i
   
print(d1)
    
    
    
