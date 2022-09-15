
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 23:19:56 2017

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
N=100
dt=0.1
c=100
r=[]
theta=[]

"""
Declaration of blobs by random distribution
"""
"""

r2=[]
theta2=[]
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
    dummyRadius+=4
    dummyCircum=2*np.pi*dummyRadius
    blobs_onthis=int(dummyCircum/6)
    phi=0
    if (N-assignedPoints<blobs_onthis):
        blobs_onthis=N-assignedPoints
    while (phi<2*np.pi):
        phi+=2*np.pi/blobs_onthis
        r.append(dummyRadius)
        theta.append(phi)
        assignedPoints+=1
    
    
    
#"""

"""
Defining blobList list that contains all the blob objects, first N centered
on(-50,0) and next N centered about (50,0)
"""
blobList=[]
for i in range(0,N):
    blobList.append(Blob(-50+cm.rect(r[i], theta[i]),0+0j,2000,2,0+0j,0+0j))
for i in range(0,N):
    blobList.append(Blob(50+cm.rect(r[i], theta[i]),0+0j,2000,2,0+0j,0+0j))
    

N=2*N#doubling the points as there are n points on each side
plotMatrix_real = np.zeros((c,N))#rectangular matrix holding all the x-axis position values of the blobs
plotMatrix_imag = np.zeros((c,N))#rectangular matrix holding all the y-axis position values of the blobs
#"""
#place holder for plotting initial positions of the  distributed points
for k in range(0,c): 
    for i in range(0,N):
        plotMatrix_real[k][i]=blobList[i].position.real
        plotMatrix_imag[k][i]=blobList[i].position.imag
#"""

plt.scatter(plotMatrix_real[c-1][0:(N/2)-1],plotMatrix_imag[c-1][0:(N/2)-1],color='blue')
plt.scatter(plotMatrix_real[c-1][(N/2):N-1],plotMatrix_imag[c-1][(N/2):N-1],color='red')