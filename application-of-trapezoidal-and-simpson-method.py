import math
def f(x):										#this is the function
	return (x**3/((math.exp(x))-1))

def Trapezoidal(f,a,b,n):						#This is the integration by trapezoid method
	dx=abs(b-a)/n  								#calculates the height of the trapezoid
	x_1=a 										#the first value of x_1
	x_2=x_1+dx 									#the first value of x_2
	integral=0									#the areas of the trapezoids will be added here to get the final integral result
	for i in range (0,n): 						#repeats till i reaches n
		integral=dx*(f(x_2)+f(x_1))/2+integral 	#calculates the area and adds to integral
		x_1=x_1+dx 								#new value of x_1
		x_2=x_2+dx 								#new value of x_2
	print("Result by trapezoidal method:",integral)	


def Simpson(f,a,b,n):							#This is the integration by simpson method
	dx=abs(b-a)/n 								#calculates the distance
	x=a 										#the first value of x
	x_n=b 										#the last value of x
	s=f(x)+f(x_n) 								#calculates the value of function at both ends and adds them together
	x=a+dx 										#the new value of x
	for i in range (1,n): 						#repeats till i reaches n
		if i%2==0: 								#checks if i is even or not
			s=s+2*f(x) 							#calculates the value of the function at x and multiplies with 2 then add to s
			x=x+dx 								#the new value of x
		else: 									#if i is odd
			s=s+4*f(x) 							#calculates the value of the function at x and multiplies with 4 then add to s
			x=x+dx 								#the new value of x
	integral=dx/3*s 							#calculates the integral
	print("Result by simpson method:",integral) 

Simpson(f,0.001,100,200)
Trapezoidal(f,0.001,100,200)