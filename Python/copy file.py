with open("C:/Users/ayush/Documents/p1.txt",'r') as firstfile, open("C:/Users/ayush/Documents/p2.txt",'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)
