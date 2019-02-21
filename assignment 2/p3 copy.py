import sympy as sp 
import matplotlib.pyplot as plt
import numpy as np
from mpmath import *
import matplotlib.cm as cm
# %matplotlib inline

# define the symbolic function f(z)
f = sp.Function("f")
z = sp.Symbol("z")
N = z - f(z)/f(z).diff(z) #define newton function

#define Newton iterator for F = z**3-1
Nsq = N.subs(f(z),z**3-1)

Nsq = sp.simplify(Nsq.doit()) #notice .diff(z) is passive

IT = sp.lambdify(z,Nsq) # use the lambdify， use format IT(number) you can get the result

# sp.pprint(IT(5))





k_range = 10

dic_F = [[0]]
def cal_roots(k):
	total_roots = []
	for item in dic_F[k-1]:
		roots = polyroots([2,-3*item,0,1])
		for r in roots:
			total_roots.append(r)
	# print(total_roots)
	dic_F.append(total_roots)

for i in range(1,k_range+1):
	cal_roots(i)
# print(dic_F)

colors = cm.rainbow(np.linspace(0, 1, len(dic_F)))
plt.figure(figsize=(12,12))
plt.xlabel("real")
plt.ylabel("imag")
k_list = [i for i in range(k_range+1)]
for k, y, c in zip(k_list, dic_F,colors):
	plt.scatter( [j.real for j in y], [j.imag for j in y], s= 5,color = c, label = str(k))


# dom = np.linspace(-2,2,1000)
# plt.plot(dom,[x**3-1 for x in dom], color = "green", label='$z^3-1$')
plt.legend()
plt.show()












