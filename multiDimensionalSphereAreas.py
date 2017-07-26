from math import *
from matplotlib import pyplot
from numpy import arange

'''
    A sphere area in dimension D can be found by formula [\  V_{r} = K_{D}*r^{D}  \]
    We will find the ratio between the region r = 1 and r = 1 - \epsilon
    [\ Ratio = (V_{1} - V{1-\epsilon} ) / V_{1} \] -----> Asses for values of D and Epslon
    It becomes [\ Ratio = 1-(1-\epsilon)^{D} \]
'''

def iterEpsilons(D):
 x = []
 y = []
 ratio = lambda e: 1-(1-e)**D
 for i in arange(0,1.01, 0.01 ):
  x.append(i)
  y.append(ratio(i))
 pyplot.plot(x,y)


def main():
 for i in range(100):
  iterEpsilons(i)
 pyplot.show()

main()
 
