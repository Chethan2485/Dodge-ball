from sympy import *
x,y,z=symbols('x y z')
f=x*y*z
A=integrate(f,(x,0,2),(y,0,sqrt(1-(z**2))),(z,0,1))
print("integration =",A)