import math
import numpy as np
g=9.81																#gravitational acceleration
x=300																#horizontal distance
h=61																#vertical distance
a_1=45																#the given angle
sin45=np.sin(np.deg2rad(45))
cos45=np.cos(np.deg2rad(45))

a=0; b=70															#the interval for bisection method
while ((b-a)>=0.000001):											#applies bisection method
	m=(a+b)/2
	y_m=(m*cos45/g)*(m*sin45+math.sqrt((m**2)*(sin45)**2+2*h*g))-x	#Checks if y_m and y_a satisfies the question that gives us the value of velocity
	y_a=(a*cos45/g)*(a*sin45+math.sqrt((a**2)*(sin45)**2+2*h*g))-x	
	if y_m==0:
		break
	if y_m*y_a<0:
		b=m
	else:
		a=m

t=(m*sin45+math.sqrt((m**2)*(sin45)**2+2*h*g))/g 					#gives the flight time
print("The flight time is:",t)
h_1=((m**2)*((sin45)**2)/(2*g))										#finds the maximum height when we throw it from the wall with 45 degrees
h_tot=h_1+h 														#the total height
v2s2=h_tot*2*g 														#gives the product of the velocity square and sin(theta) square where velocity is the one when we throw the ball from the groud and with angle theta										
v2c2=(m*sin45)**2  													#vcos(theta)=v_0sin45 where v is the angle from the ground and v_0 is the angle from above. We square this equation. In this one m corresponds to v_0
v=math.sqrt(v2s2+v2c2)												#we sum up the above two equations and solve it to find the velocity that is asked in the question
print("The velocity is:",v)
theta=np.rad2deg(np.arccos(x/(v*t)))								#by using x=vtcos(theta) equation we find theta by using arccos
print("The angle is:",theta)
