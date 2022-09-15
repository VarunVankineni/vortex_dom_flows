# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:49:24 2017

@author: Varun
"""

import numpy as np

import matplotlib.pyplot as plt

"""
Modify t,c as such that you get a smooth enough graph and enough iterations to compensate for it, remove # in the input lines for an interactive script
"""
c = 100
t = 0.01

G1 = 2000#input ('Enter the strength of your 1st Vortex:')
G2 = 2000#input ('Enter the strength of your 2nd Vortex:')
"coordinate variables x2,x1,y2,y1 simplify coding and help readability instead of a list"
x1 = 0#input ('Enter the abscissa of your 1st Vortex from origin:')
y1 = 10#input ('Enter the ordinate of your 1st Vortex from origin:')
x2 = 0#input ('Enter the abscissa of your 2nd Vortex from origin:')
y2 = -10#input ('Enter the ordinate of your 2nd Vortex from origin:')

Xl1 = [x1]
Xl2 = [x2]
Yl1 = [y1]
Yl2 = [y2]
print "Plotting for strengths",G1,',',G2,'and intitally located at (',x1,',',y1,') and (',x2,',',y2,')'

r = np.sqrt((x2-x1)**2+(y2-y1)**2)

for i in range(0,c) :
    """calculating new positions of the vortex centres adding them to the lists and calculating the new r"""
    x2n = x2 + ((G1/(2*np.pi*r))*(y2-y1)*(t/r))
    x2=x2n
    Xl2.append(x2n)
    x1n = x1 + ((G2/(2*np.pi*r))*(y1-y2)*(t/r))
    x1=x1n
    Xl1.append(x1n)
    y2n = y2 - ((G1/(2*np.pi*r))*(x2-x1)*(t/r))
    y2=y2n
    Yl2.append(y2n)
    y1n = y1 - ((G2/(2*np.pi*r))*(x1-x2)*(t/r))
    y1=y1n
    Yl1.append(y1n)
    r = np.sqrt((x2-x1)**2+(y2-y1)**2)
"""Remove # for printing full lists/ to get point data"""    
#print Xl1,Xl2,Yl1,Yl2
plt.plot(Xl1,Yl1)
plt.plot(Xl2,Yl2)








