import numpy as np
import pylab as pl
import math

a=0.0							# x is between 0.0 and 3
b=3
N=300							# N is the steps
h=(b-a)/N 						# h is the stepsize

def f(x,u): 					# this is the differential function
	return (x**2)*math.exp(-u-1)

x=np.arange(a,b+h,h)			# x and w are arrays that will hold the values
w=np.zeros((N+1,))   
x[0]=0.0 						# initial values of x and w
w[0]=1
alpha=1

for i in range (1,N+1): 		# Applies second order runge-kutta method
	k_1=h*f(x[i-1],w[i-1])
	k_2=h*f(x[i-1]+alpha*h,w[i-1]+alpha*k_1)
	w[i]=w[i-1]+(1-1/2*alpha)*k_1+k_2/2*alpha



pl.plot(x,w,label='approximation') 		#plots the graph
pl.title("Second Order Runge-Kutta Method, h=0.01, alpha=1")
pl.xlabel('x')
pl.ylabel('u(x)')
pl.legend(loc=4)
pl.grid()
pl.show()