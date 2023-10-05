b=eval(input())
c=[[0,0,0],[0,0,0]]
for i in range(len(b)):
    for j in range(len(b[0])):
        c[j][i]=b[i][j]
print(c)
