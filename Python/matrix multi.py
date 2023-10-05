l1=eval(input())
l2=eval(input())
ld=[[0,0,0],[0,0,0],[0,0,0]]
for ii in range(len(l1)):
    for jj in range(len(l2[0])):
        for kk in range(len(l2)):
                        ld[ii][jj]+=l1[ii][kk]*l2[kk][jj]
for r in ld:
                        print(r)
                
   
