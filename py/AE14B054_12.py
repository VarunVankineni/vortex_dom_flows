import numpy as np

n1=8#float(input("enter the radius of patch1="))
n2=1#float(input("enter the radius of blob belonging to patch1="))
n6=int((n1**2)/(n2**2))#This will calculate number of blobs in the patch
n3=9#float(input("enter the radius of patch2="))
n4=1#float(input("enter the radius of blob belonging to patch2="))
n7=int((n3**2)/(n4**2))#This will calculate number of blobs in the patch
t=5#float(input("enter the time at which you want to plot"))
dt=0.1#float(input("enter the time step"))       
p=int(t/dt)#calculates the number of time steps.
T=50#circulation for both the blobs.
A1=np.zeros((n6,2))#x coordinates and Y coordinates of the blob1 are stores in this array
A2=np.zeros([n7,2])#x coordinates and Y coordinates of the blob2 are stores in this array
U1=np.zeros([n6,2])#x and Y component of velocity on blob1 due to other blobs 
U2=np.zeros([n7,2])#x and Y component of velocity on blob2 due to other blobs 
a1=[]
b1=[]
a2=[]
b2=[]
angle=np.pi*(3-np.sqrt(5))

for i in range (n6):
    phi=i*angle
    r=n1*np.sqrt(i/n6)#distributes uniformly all the blobs over given radius
    A1[i,0]=0+r*np.cos(phi)#center of the patch is at (0,0)
    A1[i,1]=0+r*np.sin(phi)

for i in range (n6):
    a1.append(A1[i,0])
    b1.append(A1[i,1])
    
for i in range (n7):
    phi=i*angle#distributes uniformly all the blobs over given radius
    r=n3*np.sqrt(i/n7)
    A2[i,0]=100+r*np.cos((phi*180)/(np.pi))#center of the patch is at (80,80)
    A2[i,1]=100+r*np.sin((phi*180)/(np.pi))
    
for i in range (n6):
    a2.append(A2[i,0]) 
    b2.append(A2[i,1])
    
      
for i in range (p):
    for j in range (n6):       
        for k in range(n6):
            if k!=j:
                 U1[j,0]+=-T*(A1[j,0]-A1[k,0])/((A1[j,0]-A1[k,0])**2+(A1[j,1]-A1[k,1])**2)
                 U1[j,1]+=+T*(A1[j,1]-A1[k,1])/((A1[j,0]-A1[k,0])**2+(A1[j,1]-A1[k,1])**2)         
     
    for j in range (n6):
        for k in range(n7):
            U1[j,0]+=-T*(A1[j,0]-A2[k,0])/((A1[j,0]-A2[k,0])**2+(A1[j,1]-A2[k,1])**2)
            U1[j,1]+=+T*(A1[j,1]-A2[k,1])/((A1[j,0]-A2[k,0])**2+(A1[j,1]-A2[k,1])**2)
    
    for j in range (n7):       
        for k in range(n7):
            if k!=j:
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



        
                
            
            
            
            
    

#plt.scatter(x[:,n2,0],x[:,n2,1])
#plt.show