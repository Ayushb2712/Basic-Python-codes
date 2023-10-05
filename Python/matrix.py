l1=eval(input())
l2=eval(input())
la=[]
lb=[]
ld=[]
mul=1
for ii in range(len(l1)):
    la=l1[ii]
    lb=l2[ii]
    lc=[]
    for jj in range(len(la)):
        mul*=la[jj]*lb[jj]
        lc.append(mul)
        mul=1
        
    ld.append(lc)
for j in ld:
    print(j)
