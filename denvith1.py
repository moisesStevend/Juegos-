from sympy import *
theta_i=Symbol("theta_i")
alpha_i1=Symbol("alpha_i1")
a_i1=Symbol("a_i1")
d_i=Symbol("d_i")
T=Matrix([[cos(theta_i), -sin(theta_i), 0, a_i1],[sin(theta_i)*cos(alpha_i1),cos(theta_i)*cos(alpha_i1), -sin(alpha_i1), -sin(alpha_i1)*d_i],[sin(theta_i)*sin(alpha_i1), cos(theta_i)*sin(alpha_i1), cos(alpha_i1), cos(alpha_i1)*d_i],[0,0,0,1]])
print latex(T)
print T 