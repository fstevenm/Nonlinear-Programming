'''Metode Gradient Descent 1 Variabel'''
import numpy as np
import sympy as sym
'''Iterasi gradient descent'''
def grad_desc(g,dgdx,alpha,w,toleransi):
    global x_data
    x_data = [] #untuk plot titik hasil iterasi
    n = 1
    a = 0
    print("w0 =",w)
    while abs(w-a)>toleransi:
        x_data.append(w)
        a = w
        w = w-alpha*dgdx(w)
        print("w"+str(n)+" = ",w)
        n+=1
    return print("Karena selisih dua titik terakhir sudah kurang dari",
                 toleransi,", maka"
                 "\nTitik nilai minimumnya adalah",
                 w,"dengan g({0})={1}".format(w,g(w)))

g = lambda w: np.sin(3*w)+0.3*w**2 #rumus g(w)
dgdw = lambda w: 3*(np.cos(3*w))+0.6*w #turunan g(w)
grad_desc(g,dgdw,0.05,4.5,0.001)


'''plot grafik g(w) dan titik hasil iterasi'''
import matplotlib.pyplot as plt
import numpy as np
x1 = np.arange(-5,5,0.001)
y1 = []
y_data = []
y_data0 = []
for i in x1: y1.append(g(i))
for i in x_data: y_data.append(g(i)),y_data0.append(0)
plt.plot(x1,y1,'blue', label='$f(x)=sin(3x)+0.3x^2$')
plt.plot(x_data,y_data,'yo',label='hasil iterasi')
plt.plot(x_data,y_data0,'yo')
plt.plot(x_data[0],y_data[0],'go',label='titik awal iterasi')
plt.plot(x_data[0],y_data0[0],'go')
plt.plot(x_data[-1],y_data[-1],'ro',label='titik akhir iterasi')
plt.plot(x_data[-1],y_data0[-1],'ro')
plt.title("Grafik Fungsi $f(x)=sin{(3x)}+0.3x^2$")
plt.legend(loc='best')
plt.axis([-5,5,min(y1),max(y1)])
plt.xlabel('$w$')
plt.ylabel('$g(w)$')
plt.grid()
plt.show()




#print(newton(f,fprime,1000,0.001))
#x = sym.symbols('x')
#f_simbol = x**5+5*x+6
#f = sym.lambdify([x],f_simbol)
#dfdx_simbol = sym.diff(f_simbol,x)
#dfdx = sym.lambdify([x],dfdx_simbol)
#print(f_simbol,dfdx_simbol)