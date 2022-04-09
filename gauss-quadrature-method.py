import math

def f(x):										#this is the function which we want to take the integral
	return math.exp(x)*math.cos(x)

def gauss_quadrature(f,a,b):					#this is the function for integral by gauss quadrature method
	c=(b-a)/2									#this is the coefficient for n=2
	x_1=(((b-a)/2)*(-1/math.sqrt(3)))+(b+a)/2	#this gives the first x value according to the method
	x_2=(((b-a)/2)*(1/math.sqrt(3)))+(b+a)/2	#this is the second x value according to the method
	integral=c*f(x_1)+c*f(x_2)					#computes the integral
	print (integral)							#prints the result

gauss_quadrature(f,0.5,1.5)