import sympy as sp
import numpy as np

x = sp.Symbol("x") #define the symbol x
f = x**x-2 # define the function x**x -2


#define the subdivision function
def subdiv(f,x, a, b, eps):
	count = 0   # iteration count 
	lower = a   # left endpoints
	upper = b   # right endpoints
	while((upper-lower)>eps):  #check whether the interval is smaller than the eps
		count+=1   # increase the count first
		mid = (lower+upper)/2   
		f_mid = f.subs(x,mid)  # calculate the value at mid point
		f_lower = f.subs(x,lower)  
		f_upper = f.subs(x,upper)
		if(np.sign(f_mid) == np.sign(f_upper)):   #compare the sign and make decision
			lower = lower
			upper = mid
		elif(np.sign(f_mid) == np.sign(f_lower)):
			lower = mid
			upper = upper
		else:
			count -=1
			break
	return [lower, upper, count]   # return the values within a list

print("{0:2s}\t{1:22s}\t{2:22s}\t{3:15s}".format("k", "left endpoint", "right endpoint", "iteration times"))
for i in range(1,7):
	eps = sp.Integer(1)/sp.Integer(10**i)
	l = subdiv(f,x,1.0,2.0,eps)
	print("{0:1d}\t{1:22.20f}\t{2:22.20f}\t{3:8d}".format(i, l[0], l[1], l[2]))