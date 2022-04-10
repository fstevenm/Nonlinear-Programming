'''Metode Pencari Akar'''

import numpy as np
import sympy as sym

def newton(f,dfdx,x,tol):
    n = 1
    a = 0
    while abs(x-a)>tol:
        a = x
        x = x-f(x)/dfdx(x)
        print("x"+str(n)+"= ",x)
        n+=1
    return "Akarnya adalah",x,"dengan f({0})={1}".format(x,f(x))

#print(newton(f,fprime,1000,0.001))
x = sym.symbols('x')
f_simbol = (3*x-2)**2*(2*x-3)**2
f = sym.lambdify([x],f_simbol)
dfdx_simbol = sym.diff(f_simbol,x)
dfdx = sym.lambdify([x],dfdx_simbol)

#print(f_simbol,dfdx_simbol)

print(newton(f,dfdx,1.1,0.001))


import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(-5,15,0.001)
y1 = []
for i in x1:
    y1.append((i)**3-12.2*(i)**2+7.45*(i)+42)
plt.plot(x1,y1)
plt.title("Grafik Fungsi f(x)")
plt.legend(['f(x)'],loc='best')
plt.axis([0,15,min(y1),max(y1)])
plt.xlabel('sumbu x')
plt.ylabel('sumbu y')
plt.grid()
plt.show()