from sympy import *
r,t,a,b=symbols('r t a b')
f=r
A=integrate(f,(r,a*(1+cos(t)),b*(1+cos(t))),(t,0,pi))
area=2*A
print("area=",area)