import math

def f(x):
	return x**math.cos(x)								#this is the function

m_1=[]													#m_1,m_2,m_3,m_4,m_5 and m_6 will be filled with the 
m_2=[]													#estimates of the derivative of the function										
m_3=[]
m_4=[]
m_5=[]
m_6=[]
h=0.1													#initial value of h
x=0.6													#initial value of x
N=5														#number of iterations
for i in range (0,N+1):
	m_1.append((f(x+h)-f(x-h))/(2*h))					#calculates the derivative estimations using central difference formula and 
	h=h/(2**i)											#appends to the array from D(0,0) to D(N,0)

for i in range (1,N+1):
	m_2.append(m_1[i]+(m_1[i]-m_1[i-1])/((4**i)-1))		#calculates the derivative estimations from D(1,1) to D(N,1)

for i in range (1,N):
	m_3.append(m_2[i]+(m_2[i]-m_2[i-1])/((4**i)-1))		#calculates the derivative estimations from D(2,2) to D(N,2)

for i in range (1,N-1):
	m_4.append(m_3[i]+(m_3[i]-m_3[i-1])/((4**i)-1))		#calculates the derivative estimations from D(3,3) to D(N,3)

for i in range (1,N-2):
	m_5.append(m_4[i]+(m_4[i]-m_4[i-1])/((4**i)-1))		#calculates the derivative estimations from D(4,4) to D(N,4)

for i in range (1,N-3):
	m_6.append(m_5[i]+(m_5[i]-m_5[i-1])/((4**i)-1))		#calculates the derivative estimation D(N,N)

print('The estimate of the derivative is:', m_6)		#prints the estimated value D(N,N)