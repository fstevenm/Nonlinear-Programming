'''Metode Gradient Descent 2 Variabel'''
import numpy as np
import sympy as sym

'''Iterasi gradient descent'''
def grad_desc(g,dgdw1,dgdw2,w1,w2,alpha,tol):
    global w11,w22
    a,b = 0,0
    n = 1
    w11 = []
    w22 = []
    print("(w1,w2) awal = ({0},{1})".format(w1,w2))
    while abs(w1-a)>tol or abs(w2-b)>tol:
        a = w1
        b = w2
        w11.append(w1)
        w22.append(w2)
        w1 = w1-alpha*dgdw1(w1)
        w2 = w2-alpha*dgdw2(w2)
        print("(w1,w2) ke-"+str(n)+" = ({0},{1})".format(w1,w2))
        n+=1
    return print("\nTitik nilai minimumnya adalah w1 =",
                 w1,"w2 =",w2,
                 "\ndengan g({0},{1})={2}".format(w1,w2,g(w1,w2)))

g = lambda w1,w2: w1**2+w2**2+2 #rumus f(x)
dgdw1 = lambda w1: 2*w1 #turunan f(x) thd x
dgdw2 = lambda w2: 2*w2 #turunan f(x) thd y

grad_desc(g,dgdw1,dgdw2,2,2,0.2,0.01)


'''Kontur'''
import matplotlib.pyplot as plt
w1 = np.arange(-3,3, 0.01)
w2 = np.arange(-3,3, 0.01)
W1, W2 = np.meshgrid(w1, w2)
Z = W1**2+W2**2+2

plt.contour(W1,W2,Z,70,cmap='cool')
plt.grid()
plt.axis('square')
plt.title('Kontur $g(w_1,w_2)=w_{1}^2+w_{2}^2+2$')
plt.xlabel('$w_1$')
plt.ylabel('$w_2$')
plt.plot(w11,w22,'yo-',label='hasil iterasi')
plt.plot(w11[0],w22[0],'go',label='titik awal iterasi')
plt.plot(w11[-1],w22[-1],'ro',label='titik akhir iterasi')
plt.legend()
plt.colorbar()
plt.show()

'''Surface'''
fig = plt.figure()
ax = plt.axes(projection='3d')
surface = ax.plot_surface(W1,W2,Z,cmap='viridis')

ax.set_xlabel('$w_1$')
ax.set_ylabel('$w_2$')
ax.set_zlabel('$g(w1,w2)$')
ax.plot(w11,w22,'yo-', zs=0, zdir='z',
        label='hasil iterasi')
ax.plot(w11[0],w22[0],'go', zs=0, zdir='z',
        label='titik awal iterasi')
ax.plot(w11[-1],w22[-1],'ro', zs=0, zdir='z',
        label='titik akhir iterasi')
ax.set_title('$g(w_1,w_2)=w_{1}^2+w_{2}^2+2$')
ax.legend()
fig.colorbar(surface, shrink=0.5, aspect=10)
plt.show()




#figure(1)
#CS = contour(X, Y, Z, 12, cmap=cm.coolwarm)
#clabel(CS, inline=1, fontsize=10)
#title('Kontur $f(x,y)=x^2+y^+2$')
#plot(w11,w22,'ro-')
#show()


#x = sym.symbols('x')
#y = sym.symbols('y')
#f_simbol = 0.26*(x**2+y**2)-0.48*x*y
#f = sym.lambdify([x,y],f_simbol)
#dfdx1_simbol = f_simbol.diff(x)
#dfdx1 = sym.lambdify([x,y],f_simbol)
#dfdx2_simbol = f_simbol.diff(y)
#dfdx2 = sym.lambdify([x,y],f_simbol)
#print(dfdx1_simbol,dfdx2_simbol)

