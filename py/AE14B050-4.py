# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 22:52:05 2017

@author: Varun
"""

import numpy as np
import cmath as cm
import matplotlib.pyplot as plt

"""
Blob Class with basic class functions for usability and testing
"""
class Blob:
    blobCount = 0
    
    def __init__(self,position,velocity,strength,radius,relativeRadius,relativeVelocity):
        self.position = position
        self.velocity = velocity
        self.strength = strength
        self.radius = radius
        self.relativeRadius = relativeRadius
        self.relativeVelocity = relativeVelocity
        Blob.blobCount +=1
    
    def show_blobCount(self):
        print " Total number of Blobs are %d" % Blob.blobCount
        
    def show_data(self):
        print self.position,self.velocity,self.strength,self.radius
    

"""
INPUTS
"""
N=100#No.of blobs in each patch
dt=0.05#time interval
c=200#no.of iterations
distance=500# distance between the two Centre of masses   
Gamma=2000#total strength of each blob
Gamma2=2000#total strength of each blob
blobsize=2#radius of each blob
wallOrdinate=500
initVelocity=0+100j






"""
Dont look here this is magic 
"""
r=[]
theta=[]
r2=[]
theta2=[]
inherentV=[]
distance=distance/2
"""
Declaration of blobs by random distribution
"""

"""

for i in range(0,N):
    r.append(25*np.random.random_sample())
    theta.append(np.pi+np.pi*np.random.random_sample())
for i in range(0,N):
    r2.append(25*np.random.random_sample())
    theta2.append(np.pi+np.pi*np.random.random_sample())
"""
"""
Declaration of blobs by uniform distribution
"""
#"""
assignedPoints=0
dummyRadius=0

while (assignedPoints<N):
    dummyRadius+=2*blobsize
    dummyCircum=2*np.pi*dummyRadius
    blobs_onthis=int(dummyCircum/3*blobsize)
    phi=0
    if (N-assignedPoints<blobs_onthis):
        blobs_onthis=N-assignedPoints
    while (phi<2*np.pi):
        phi+=2*np.pi/blobs_onthis
        r.append(dummyRadius)
        theta.append(phi)
        r2.append(dummyRadius)
        theta2.append(phi)
        assignedPoints+=1   
#"""

"""
Defining blobList list that contains all the blob objects, first N centered
on(-distance,0) and next N centered about (distance,0) and so on 
"""
blobList=[]
for i in range(0,N):
    blobList.append(Blob(-distance+cm.rect(r[i], theta[i]),initVelocity,Gamma,blobsize,0+0j,0+0j))
for i in range(0,N):
    blobList.append(Blob(distance+cm.rect(r2[i], theta2[i]),initVelocity,Gamma2,blobsize,0+0j,0+0j))
for i in range(0,N):
    blobList.append(Blob(-distance+cm.rect(r[i], theta[i])+(2*(0+1j)*(wallOrdinate-distance.imag)),(1+0j)*initVelocity.real-(0+1j)*initVelocity.imag,-Gamma,blobsize,0+0j,0+0j))
for i in range(0,N):
    blobList.append(Blob(distance+cm.rect(r2[i], theta2[i])+(2*(0+1j)*(wallOrdinate-distance.imag)),(1+0j)*initVelocity.real-(0+1j)*initVelocity.imag,-Gamma2,blobsize,0+0j,0+0j))    

N=4*N#doubling the points as there are n points on each side
plotMatrix_real = np.zeros((c,N))#rectangular matrix holding all the x-axis position values of the blobs
plotMatrix_imag = np.zeros((c,N))#rectangular matrix holding all the y-axis position values of the blobs
#"""
#place holder for plotting initial positions of the randomly distributed points
for i in range(0,N):
    plotMatrix_real[0][i]=blobList[i].position.real
    plotMatrix_imag[0][i]=blobList[i].position.imag
plt.scatter(plotMatrix_real[0][0:(N/4)-1],plotMatrix_imag[0][0:(N/4)-1],color='blue',s=np.pi*blobsize**2)
plt.scatter(plotMatrix_real[0][(N/4):(N/2)-1],plotMatrix_imag[0][(N/4):(N/2)-1],color='red',s=np.pi*blobsize**2)
plt.scatter(plotMatrix_real[0][(N/2):(3*N/4)-1],plotMatrix_imag[0][(N/2):(3*N/4)-1],color='green',s=np.pi*blobsize**2)
plt.scatter(plotMatrix_real[0][(3*N/4):N-1],plotMatrix_imag[0][(3*N/4):N-1],color='black',s=np.pi*blobsize**2) 
plt.axhline(y=wallOrdinate)
plt.axhline(y=5*wallOrdinate)
plt.axhline(y=-4*wallOrdinate)
plt.axvline(x=8*wallOrdinate)
plt.axvline(x=-8*wallOrdinate)
plt.show()
plt.pause(2)
#"""

"""
Updating the position of each blob centre over c iterations and dt time interval for each iteration
"""
#"""
for i in range(0,N):
        inherentV.append(blobList[i].velocity)
for k in range(0,c):
    if(k!=0):
        for i in range(0,N):
            inherentV[i]=blobList[i].velocity
        
    for i in range(0,N):
        for j in range(0,N):        
            if (i!=j):               
                blobList[i].relativeRadius=blobList[i].position-blobList[j].position
                blobList[i].relativeVelocity=blobList[i].relativeRadius*(0+1j)*blobList[j].strength/(2*np.pi*abs(blobList[i].relativeRadius)*abs(blobList[i].relativeRadius))  
                if (abs(blobList[i].relativeRadius)<abs(blobList[j].radius)):
                    blobList[i].relativeVelocity=blobList[i].relativeVelocity*((abs(blobList[i].relativeRadius))/blobList[i].radius)**2
                blobList[i].velocity+=blobList[i].relativeVelocity
    for i in range(0,N): 
        if (i<((N/2))):
            if (i!=j):  
                if ((blobList[i].position+blobList[i].velocity*dt).imag<wallOrdinate):
                    blobList[i].position+=blobList[i].velocity*dt  
                else:
                    dummyOrdinate=-(blobList[i].position).imag+wallOrdinate
                    blobList[i].position+=(0+1j)*dummyOrdinate
                    blobList[i].position+=(1+0j)*blobList[i].velocity.real*dt  
                    inherentV[i]=(1+0j)*inherentV[i].real-(0+1j)*inherentV[i].imag

           
        else:
            if (i!=j):  
                if ((blobList[i].position+blobList[i].velocity*dt).imag>wallOrdinate):
                    blobList[i].position+=blobList[i].velocity*dt  
                else:
                    dummyOrdinate=-(blobList[i].position).imag+wallOrdinate
                    blobList[i].position+=(0-1j)*dummyOrdinate
                    blobList[i].position+=(1+0j)*blobList[i].velocity.real*dt  
                    inherentV[i]=(1+0j)*inherentV[i].real-(0+1j)*inherentV[i].imag

                    
                    
        
       
    for i in range(0,N):
        blobList[i].velocity=inherentV[i]
        plotMatrix_real[k][i]=blobList[i].position.real
        plotMatrix_imag[k][i]=blobList[i].position.imag
        
        
        #Psuedo animation ( NOT RECOMMENDED TO USE FOR PARTICLES MORE THAN 200), use only for rough visualisation
        #"""
    if ((k%1)== 0):
        plt.clf()
        plt.scatter(plotMatrix_real[k][0:(N/4)-1],plotMatrix_imag[k][0:(N/4)-1],color='blue',s=np.pi*blobsize**2)
        plt.scatter(plotMatrix_real[k][(N/4):(N/2)-1],plotMatrix_imag[k][(N/4):(N/2)-1],color='red',s=np.pi*blobsize**2)
        plt.scatter(plotMatrix_real[k][(N/2):(3*N/4)-1],plotMatrix_imag[k][(N/2):(3*N/4)-1],color='green',s=np.pi*blobsize**2)
        plt.scatter(plotMatrix_real[k][(3*N/4):N-1],plotMatrix_imag[k][(3*N/4):N-1],color='black',s=np.pi*blobsize**2) 
        plt.axhline(y=wallOrdinate)
        plt.axhline(y=5*wallOrdinate)
        plt.axhline(y=-4*wallOrdinate)
        plt.axvline(x=8*wallOrdinate)
        plt.axvline(x=-8*wallOrdinate)
        plt.show()
        plt.pause(0.00001)
        #"""
#"""

"""
Scatter plot all the blob centres after c iterations with color coded as blue for particles centered about (-50,0)
and red for particles centered about (50,0) 
"""
plt.clf()
plt.scatter(plotMatrix_real[c-1][0:(N/4)-1],plotMatrix_imag[c-1][0:(N/4)-1],color='blue',s=np.pi*blobsize**2)
plt.scatter(plotMatrix_real[c-1][(N/4):(N/2)-1],plotMatrix_imag[c-1][(N/4):(N/2)-1],color='red',s=np.pi*blobsize**2)
plt.scatter(plotMatrix_real[c-1][(N/2):(3*N/4)-1],plotMatrix_imag[c-1][(N/2):(3*N/4)-1],color='green',s=np.pi*blobsize**2)
plt.scatter(plotMatrix_real[c-1][(3*N/4):N-1],plotMatrix_imag[c-1][(3*N/4):N-1],color='black',s=np.pi*blobsize**2) 
plt.axhline(y=wallOrdinate)
plt.axhline(y=5*wallOrdinate)
plt.axhline(y=-4*wallOrdinate)
plt.axvline(x=8*wallOrdinate)
plt.axvline(x=-8*wallOrdinate)


    
    
            #
   