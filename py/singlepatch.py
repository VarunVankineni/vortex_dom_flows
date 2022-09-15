import math
import matplotlib.pyplot as plt
import numpy as np
import cmath
import random
import time
import sys
def CloseEvent():
	plt.close()
#x1=input('co ordinate: ')
#x1=50
#x2=100
#R=input('Radius of patch: ')

R=10
#rb=input('Radius of blobs: ')
rb=2
n=input('No of blobs in each patch: ')
#delt=input('Time step: ')
delt=0.01
#N=input('No of iterations: ')
N=100
gamma1=5000
gamma2=5000
v01,v02=input('velocity component x,y: ')
v0=v01+v02*1j
z01=0+500*1j
z01c=0-500*1j
z02=500+500*1j
z02c=500-500*1j
def scatterplot(R,N,delt):
	a=[]
	b=[]
	am=[]
	bm=[]
	vel1=[]
	vel2=[]
	r0=0
	i=0
	while(i<n):
		r0+=4
		c=2*math.pi*r0
		nb=int(c/6)
		phi=0
		if(n-i<nb):
			nb=n-i
		while (phi<2*math.pi):
			phi+=2*np.pi/nb
			z=cmath.rect(r0,phi)
			zc=cmath.rect(r0,-phi)
			a.append(z01+z)
			am.append(z01c+zc)
			vel1.append(v0)
			b.append(z02+z)
			bm.append(z02c+zc)
			vel2.append(v0)
			i+=1
	nu=len(a)
	for k in range(0,N):
		for i in range(0,nu):
			v_eq1=0
			v_eq2=0
			for j in range(0,nu):
				v=velocity_other(a,am,i,j,-gamma1)
				v_eq1+=v
				#v=velocity_other(a,b,i,j,gamma2)
				#v_eq1+=v
				v=velocity_other(b,bm,i,j,-gamma2)
				v_eq2+=v
				#v=velocity_other(b,a,i,j,gamma1)
				#v_eq2+=v
				if j!=i:
					v=velocity_self(a,i,j,gamma1)
					v_eq1+=v
					v=velocity_self(b,i,j,gamma2)
					v_eq2+=v
			a[i]=a[i]+delt*(v_eq1+vel1[i])
			b[i]=b[i]+delt*(v_eq2+vel2[i])
			wall_checker(a,vel1,i)
			wall_checker(b,vel2,i)
			am[i]=a[i].real-a[i].imag*1j
			bm[i]=b[i].real-b[i].imag*1j
		if (k%20==0):
			A=np.array(a)
			B=np.array(am)
			C=np.array(b)
			D=np.array(bm)
			plt.scatter(A.real,A.imag,color='red')
			plt.scatter(B.real,B.imag,color='blue')
			plt.scatter(C.real,C.imag,color='green')
			plt.scatter(D.real,D.imag,color='black')
			plt.axhline(y=0)
			plt.ylim(-2000,2000)
			plt.xlim(-500,1500)
			plt.ion()
			plt.close()
			plt.show()
			time.sleep(2)
			
			
def velocity_other(a,b,i,j,gamma):
	r=a[i]-b[j]
	v=(gamma/(2*math.pi*abs(r)*abs(r)))*r*1j
	return v
def velocity_self(a,i,j,gamma):
	r=a[i]-a[j]
	v=(gamma/(2*math.pi*abs(r)*abs(r)))*r*1j
	return v
def wall_checker(a,vel,i):
	if(a[i].imag<0):
		vel_temp=vel[i].real-vel[i].imag*1j
		vel[i]=vel_temp
		a_temp=a[i].real-a[i].imag*1j
		a[i]=a_temp
scatterplot(R,400,delt)



