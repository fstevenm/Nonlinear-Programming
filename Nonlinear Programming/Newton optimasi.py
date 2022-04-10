'''Metode Newton'''
import numpy as np
import sympy as sym

def newton(dgdw,dgdw2,w,alpha,tol):
    global w_data
    w_data = []
    n = 1
    a = 0
    print("w0 =",w)
    while abs(w-a)>tol:
        w_data.append(w)
        a = w
        w = w-alpha*dgdw(w)/dgdw2(w)
        print("w"+str(n)+" =",w)
        n+=1 
    return print("Titik nilai minimumnya adalah w =",w,
                 "\ndengan g({0})={1}".format(w,g(w)))

w = sym.symbols('w')
g_simbol = (1/50)*(w**4+w**2+10*w)+0.5
g = sym.lambdify([w],g_simbol)
dgdw_simbol = sym.diff(g_simbol,w)
dgdw2_simbol = sym.diff(g_simbol,w,2)
dgdw = sym.lambdify([w],dgdw_simbol)
dgdw2 = sym.lambdify([w],dgdw2_simbol)
newton(dgdw,dgdw2,2.5,1,0.01)

'''grafik'''
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-3,3,0.01)
y = []
y_data = []
for i in x: y.append(g(i))
for i in w_data: y_data.append(g(i))
plt.plot(x,y)
plt.plot(w_data,y_data,'yo-')
plt.plot(w_data[0],y_data[0],'go')
plt.plot(w_data[-1],y_data[-1],'ro')
plt.title("Grafik Fungsi $g(w)=(1/50)(x^4+x^2+10x)+0.5$")
plt.legend(['$g(w)$','hasil iterasi','titik awal iterasi'
            ,'titik akhir iterasi'],loc='best')
plt.axis([-3,3,min(y)-0.1,max(y)])
plt.xlabel('$w$')
plt.ylabel('$g(w)$')
plt.grid()
plt.show()


