fn=open("C:/Users/ayush/Documents/p1.txt",'r')
n=eval(input("Enter no  of lines to display"))
b=fn.readlines()[-n]
print(b)
