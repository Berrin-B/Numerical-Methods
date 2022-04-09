import numpy as np
import pylab as pl
import math
from math import e

a=0.0								# x is between 0.0 and 3						
b=3
N=10								# N is the steps					
h=(b-a)/N 							# h is the stepsize					

def f(x,u): 						# this is the differential function				
	return (x**2)*math.exp(-u-1)

x=np.arange(a,b+h,h)				# x and w are arrays that will hold the values		
u=np.zeros((N+1,))   
x[0]=0.0							# initial values of x and w				
u[0]=1

for i in range (1,N+1): 			#applies euler's method	
	u[i]=u[i-1]+h*f(x[i-1],u[i-1])


def f_1(x):							#this is the exact equation
	return np.log(((x**3)/(3*e))+e)


pl.plot(x,u,label='approximation') 	
pl.plot(x,f_1(x),label='exact')
pl.title("Euler's Method, N="+str(N))
pl.xlabel('x')
pl.ylabel('u(x)')
pl.legend(loc=4)
pl.grid()
pl.show()

