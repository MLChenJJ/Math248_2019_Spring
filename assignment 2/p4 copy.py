import sympy as sp 
import numpy as np
import operator
x = sp.Symbol("x")
f = 2*x

def calculate_K(k):
    value = np.sqrt(2)
    result = value
    # print(type(f.subs(x,result)))
    while(k>0):
        result = f.subs(x,result).evalf(40)-int(f.subs(x,result).evalf(40))
        k-=1
    return result

iterations = 1000
res_dic = {i:calculate_K(i) for i in range(iterations)}
sorted_result = sorted(res_dic.items(),key=operator.itemgetter(1)) # sort the dictionary by values, the return value is a list of tuples
# extract the required list J
list_J = []
for item in sorted_result:
    list_J.append(item[0])
print("The list is:")
print(list_J)


