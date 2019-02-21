
import matplotlib.pyplot as plt
import numpy as np
#define a function to calculate the iteration that is needed to find the integer 1
def func_f(n):
	if n ==1:
		return 0
	else:
		count = 0
		result = n
		while(result!=1):
			count+=1
			if result%2 == 0:
				result = result//2
			else:
				result = result*3+1
		return count

#define a function that return the dictionary L, where L[k] is the number of times one needs to apply f to turn k into 1
def func_L_k(k):
	L = {}
	for i in range(1,k+1):
		L[i] = func_f(i)
	return L

def func_T_k(k):
	dic_L = func_L_k(k)
	sum = 0
	for item in dic_L:
		sum+=dic_L[item]
	return sum

def plot_fun(k):
	X = [i for i in range(1,k+1)]
	Y = [func_T_k(item) for item in X]
	plt.xlabel("k")
	plt.ylabel("T(k)")


	#fitting with linear and quadratic
	linear_A = np.matrix([[1.0,x] for x in X]).T
	quadratic_A = np.matrix([[1.0,x,x**2] for x in X]).T
	y = np.matrix(Y).T

	linear_c = np.linalg.inv(linear_A*linear_A.T)*linear_A*y
	quadratic_c = np.linalg.inv(quadratic_A*quadratic_A.T)*quadratic_A*y


	dom = np.linspace(min(X), max(X), 1000)
	linear_ran = [linear_c[0,0] + linear_c[1,0]*x  for x in dom]
	quadratic_ran = [quadratic_c[0,0] + quadratic_c[1,0]*x + quadratic_c[2,0]*x**2 for x in dom]
	plt.plot(dom, linear_ran, 'b-', label='y=$%2.2fx+%2.2f$' %(linear_c[1,0], linear_c[0,0]))
	plt.plot(dom, quadratic_ran, 'r-', label='y=$%2.6fx^2+%2.2fx+%2.2f$' %(quadratic_c[2,0],quadratic_c[1,0], quadratic_c[0,0]))
	plt.legend()

	# plt.plot(x,y)
	plt.scatter(X,Y,alpha = 0.1)
	plt.show()

def main():
	# plot_fun(500)
	for i in range(1,11):
		print(func_f(i))

	# print the value of T(10), T(100), T(1000), T(10000), T(100000)   
	# test_k = [10, 100, 1000, 10000, 100000]
	# result = [func_T_k(x) for x in test_k]
	# print("The result of T(10), T(100), T(1000), T(10000), T(100000) in a list is: ",result)



if __name__ == '__main__':
	main()