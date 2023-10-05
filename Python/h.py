import random 
import matplotlib.pyplot as plt
import pdb

l1=[]
plt.ion()
plt.figure(1)
plt.subplot(111)
for ii in range(100):
    #pdb.set_trace()
    l1.append(random.uniform(5,500))
    plt.plot(l1)
    plt.pause(0.1)
    plt.draw()
            