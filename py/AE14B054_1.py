import numpy as np
import math as mat
import matplotlib.pyplot as plt
n1=6#float(input("enter the radius of patch1="))
n2=1#float(input("enter the radius of blob belonging to patch1="))
n6=int((n1**2)/(n2**2))#This will calculate number of blobs in the patch
n3=6#float(input("enter the radius of patch2="))
n4=1#float(input("enter the radius of blob belonging to patch2="))
n7=int((n3**2)/(n4**2))#This will calculate number of blobs in the patch
t=5#float(input("enter the time at which you want to plot"))
dt=0.1#float(input("enter the time step"))       
p=int(t/dt)#calculates the number of time steps.
T=50#circulation for both the blobs.
A1=np.zeros([n6,2])#x coordinates and Y coordinates of the blob1 are stores in this array
A2=np.zeros([n7,2])#x coordinates and Y coordinates of the blob2 are stores in this array
U1=np.zeros([n6,2])#x and Y component of velocity on blob1 due to other blobs 
U2=np.zeros([n7,2])#x and Y component of velocity on blob2 due to other blobs 
a1=[]
b1=[]
a2=[]
b2=[]
golden_angle=mat.pi*(3-mat.sqrt(5))

for i in range (n6):
    phi=i*golden_angle
    r=n1*mat.sqrt(i/n6)#distributes uniformly all the blobs over given radius
    A1[i,0]=0+r*mat.cos(phi)#center of the patch is at (0,0)
    A1[i,1]=0+r*mat.sin(phi)

for i in range (n6):
    a1.append(A1[i,0])
    b1.append(A1[i,1])
    
for i in range (n7):
    phi=i*golden_angle#distributes uniformly all the blobs over given radius
    r=n3*mat.sqrt(i/n7)
    A2[i,0]=500+r*mat.cos((phi*180)/(mat.pi))#center of the patch is at (80,80)
    A2[i,1]=500+r*mat.sin((phi*180)/(mat.pi))
    
for i in range (n6):
    a2.append(A2[i,0]) 
    b2.append(A2[i,1])
    
      
for i in range (p):
    for j in range (n6):       
        for k in range(n6):
            if j!=k:
                 U1[j,0]+=-T*(A1[j,0]-A1[k,0])/((A1[j,0]-A1[k,0])**2+(A1[j,1]-A1[k,1])**2)
                 U1[j,1]+=+T*(A1[j,1]-A1[k,1])/((A1[j,0]-A1[k,0])**2+(A1[j,1]-A1[k,1])**2)         
     
    for j in range (n6):
        for k in range(n7):
            U1[j,0]+=-T*(A1[j,0]-A2[k,0])/((A1[j,0]-A2[k,0])**2+(A1[j,1]-A2[k,1])**2)
            U1[j,1]+=+T*(A1[j,1]-A2[k,1])/((A1[j,0]-A2[k,0])**2+(A1[j,1]-A2[k,1])**2)
    
    for j in range (n7):       
        for k in range(n7):
            if j!=k:
                 U2[j,0]+=-T*(A2[j,0]-A2[k,0])/((A2[j,0]-A2[k,0])**2+(A2[j,1]-A2[k,1])**2)
                 U2[j,1]+=+T*(A2[j,1]-A2[k,1])/((A2[j,0]-A2[k,0])**2+(A2[j,1]-A2[k,1])**2)         
     
    for j in range (n7):
        for k in range(n6):
            U2[j,0]+=-T*(A2[j,0]-A1[k,0])/((A2[j,0]-A1[k,0])**2+(A2[j,1]-A1[k,1])**2)
            U2[j,1]+=+T*(A2[j,1]-A1[k,1])/((A2[j,0]-A1[k,0])**2+(A2[j,1]-A1[k,1])**2)
    for i in range(n6):
         A1[i,0]=U1[i,0]*dt+A1[i,0]
         A1[i,1]=U1[i,1]*dt+A1[i,1]
    for i in range(n7):
         A2[i,0]=U2[i,0]*dt+A2[i,0]
         A2[i,1]=U2[i,1]*dt+A2[i,1]

plt.scatter(A1[:,0],A1[:,1],color='red')
plt.scatter(A2[:,0],A2[:,1],color='green')
plt.show()
            
            
            
            
    

#plt.scatter(x[:,n2,0],x[:,n2,1])
#plt.show