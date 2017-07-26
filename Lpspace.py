from math import fabs
from sympy import *
from matplotlib import pyplot
from time import sleep

#Formula: [\  r**L = |x|**L + y**L --> From Origin  \]
#Formula assume R = 0
#Formula set L

def drawGrid():
    pyplot.arrow(0.0,0.0,1.0,0.0)
    pyplot.arrow(0.0,0.0,0.0,1.0)
    pyplot.arrow(0.0,0.0,-1.0,0.0)
    pyplot.arrow(0.0,0.0,0.0,-1.0)
    

def circlePoints(L):
    x=[]
    y=[]
    # 1 = (x^L+y^L)^(1/L), so for y,
    #Piecwise func for y>0 and y<0#
    i = -1.00
    #First, do y>0
    while i<=1.00:
        x.append(i)
        y.append(((1-fabs(i)**L)**(1/L)) )
        i+=0.01

    while i >= -1:
        x.append(i)
        y.append( (-(1-fabs(i)**L)**(1/L)))
        i-=0.01
    pyplot.plot(x,y)
    
for i in range(1,6):
    circlePoints(i)
    drawGrid()
    pyplot.show()
    
    
