# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 09:09:33 2017
@author: Varun
"""
import numpy as np
import cmath as cm
import matplotlib.pyplot as plt

"""
x - Vortex centre
p - Particle position
r - distance between two vortex centres or particle and vortex centre
"
/// only use for customization or else dont touch this 
c - number of iterations for path line of particle
"
t - small time dt 
G - vortex strength
l - vector from votex 2 to vortex 1 

T - Time from 0 for streamplot

"""
#Define t,c,x vectors, p vector, G
T=0.5
t=0.01
#c=100
x=[0+10j,0-10j]
p=10+0j
G=[2000,-6000]
Xl=[[x[0].real],[x[0].imag],[x[1].real],[x[1].imag],[p.real],[p.imag]]
#meshgrid define
"""
Meshgrid size, change accordingly, reduce no.of points to reduce computational requirements
"""
M, N = np.meshgrid(np.linspace(-20,20,100),np.linspace(-20,20,100))
stream = None
plt.ion

for i in range(0,int(T/t)) :
    l=[x[0]-x[1],x[1]-x[0]]
    pl0=p-x[0]
    pl1=p-x[1]
    rp=[abs(pl0),abs(pl1)]
    r=abs(l[0])
    x[0]=x[0]+l[0]*(0-1j)*G[1]*t/(2*np.pi*r*r)
    x[1]=x[1]+l[1]*(0-1j)*G[0]*t/(2*np.pi*r*r)
    p=p+pl0*(0-1j)*G[0]*t/(2*np.pi*rp[0]*rp[0])+pl1*(0-1j)*G[1]*t/(2*np.pi*rp[1]*rp[1])
    Rs=[np.sqrt((M-x[0].real)**2+(N-x[0].imag)**2),np.sqrt((M-x[1].real)**2+(N-x[1].imag)**2)]
    Ux=(N-x[0].imag)*G[0]/(2*np.pi*Rs[0]*Rs[0])+(N-x[1].imag)*G[1]/(2*np.pi*Rs[1]*Rs[1])
    Uy=-(M-x[0].real)*G[0]/(2*np.pi*Rs[0]*Rs[0])-(M-x[1].real)*G[1]/(2*np.pi*Rs[1]*Rs[1])
    Xl[0].append(x[0].real)
    Xl[1].append(x[0].imag)
    Xl[2].append(x[1].real)
    Xl[3].append(x[1].imag)
    Xl[4].append(p.real)
    Xl[5].append(p.imag) 

    """
    The next 5 lines of code are used to plot the streamplot and redraw it every loop. 
    Computational limits must be taken into account while doing this as all the above calculations 
    must run and if the no.of iterations is too large you might have to close the console for
    to stop the plotting. This is very inefficient in computational performance and should be used
    cautiously.
    Remove Hashtags for omitting this psuedo-animation
    """
    #"""
    if (i!=0):
        plt.clf()
    stream=plt.streamplot(M,N,Ux,Uy)
    plt.show()
    plt.pause(0.00001)
    #"""
    
"""  
  Below are the plots, remove/add hash tags for use
  
  stream plot after time T is the first one
"""  
#plt.streamplot(M,N,Ux,Uy)

"""plotting the vortex centre pathlines(line-84,85), particle path line(line-86)"""
#plt.plot(Xl[0],Xl[1])
#plt.plot(Xl[2],Xl[3])
#plt.plot(Xl[4],Xl[5])


    

    
    














