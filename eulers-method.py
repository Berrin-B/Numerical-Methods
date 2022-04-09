import numpy as np
import pylab as pl

a=0.0							# t is between 0.0 and 1.0
b=1
N=100							# N is the steps
h=(b-a)/N 						# h is the stepsize

def f(t,v): 					# this is the differential function
	return 1-2*(v**2)-t

t=np.arange(a,b+h,h)			# t and w are arrays that will hold the values
w=np.zeros((N+1,))   
t[0]=0.0 						# initial values of t and w
w[0]=1

for i in range (1,N+1): 		# Applies euler's method
	w[i]=w[i-1]+h*f(t[i-1],w[i-1])


pl.plot(t,w,label='approximation') 		#plots the graph
pl.title("Euler's Method, N="+str(N))
pl.xlabel('t')
pl.ylabel('v(t)')
pl.legend(loc=4)
pl.grid()
pl.show()