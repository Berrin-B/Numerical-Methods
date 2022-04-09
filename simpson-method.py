import math 

def f(x):										#this is the function
	return (1/(2.8*math.sqrt(2*math.pi))*math.exp(-((x-69)**2)/5.6))


def Simpson(f,a,b,n): 							#This is the integration by simpson method
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
	print(integral) 

Simpson(f,59.06,71.65,4)