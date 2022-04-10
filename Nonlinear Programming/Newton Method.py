'''Metode Newton'''

import numpy as np
import sympy as sym

def newton(dfdx,dfdx2,x,tol):
    n = 1
    a = 0
    while abs(x-a)>tol:
        a = x
        x = x-dfdx(x)/dfdx2(x)
        print("p"+str(n)+"= ",x)
        n+=1 
    return print("Titik nilai minimumnya adalah",x,"dengan f({0})={1}".format(x,f(x)))

#print(newton(f,fprime,1000,0.001))
x = sym.symbols('x')
#f_simbol = (1/2)*(x**2)-sym.sin(x)
f_simbol = (1/50)*(x**4+x**2+10*x)+0.5
f = sym.lambdify([x],f_simbol)
dfdx_simbol = sym.diff(f_simbol,x)
dfdx2_simbol = sym.diff(f_simbol,x,2)
dfdx = sym.lambdify([x],dfdx_simbol)
dfdx2 = sym.lambdify([x],dfdx2_simbol)

#print(f_simbol,dfdx_simbol,dfdx2_simbol)
#print(dfdx2(0.5))
#print(dfdx(0.5))

newton(dfdx,dfdx2,2.5,0.01)




import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3,3,0.01)
y = []
for i in x:
    y.append(f(i))
plt.plot(x,y)
plt.title("Grafik Fungsi f(x)")
plt.legend(['f(x)'],loc='best')
plt.axis([-3,3,min(y),max(y)])
plt.xlabel('sumbu x')
plt.ylabel('sumbu y')
plt.grid()
plt.show()

