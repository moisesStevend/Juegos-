import numpy as np

l=np.arange(1,16).reshape(3,5)

x=0
y=0
coor=[]
for j in range(len(l)):
    for i in range(len(l[0])):
        coor.append((x,y))
        x+=70
    y+=70
    x=0


coor=np.asarray(coor)
print len(coor)
print coor,type(coor)
print coor[14]
